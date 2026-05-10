

# views.py (arranged in logical order)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.conf import settings
from django import forms
from django.db.models import Q, Sum
import razorpay 
import datetime
# at top of views.py
import threading
from .utils import send_welcome_email
from .image_utils import compress_image, compress_images_batch

import os
from pathlib import Path
import pickle
import joblib
import pandas as pd
import numpy as np
from decimal import Decimal
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import (
    Product, ProductImage, Review, CartItem, Order,
    UserProfile, FarmerProfile, BuyerProfile, Crop, CropPrice,
    QualityInput, QualityInputImage, QualityInputReview, QualityInputCartItem, QualityInputOrder
)
from .forms import (
    OrderForm, ProductSearchForm, UserRegistrationForm,
# ... (rest of imports remain same) ...

    FarmerProfileForm, BuyerProfileForm, ContactForm,
    CropInputForm, YieldPredictionForm, ProductForm,
    QualityInputForm, QualityInputOrderForm, QualityInputSearchForm, QualityInputReviewForm
)

# ========== AUTHENTICATION ==========
def home(request):
    return render(request, 'marketplace/index.html')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


def send_welcome_email(user, request=None):
    """
    Sends HTML + plain text welcome email to new user.
    """
    if not user.email:
        return False

    context = {
        "username": user.username,
        "login_url": request.build_absolute_uri(reverse("login")) if request else reverse("login"),
        "year": datetime.datetime.now().year,
    }

    subject = "Welcome to Farm Market — Account Created"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]

    html_content = render_to_string("emails/welcome_email.html", context)
    text_content = render_to_string("emails/welcome_email.txt", context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")

    try:
        msg.send()
        return True
    except Exception as e:
        print("Email send failed:", e)
        return False



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            role = request.POST.get('role')
            if not role:
                messages.error(request, "Please select a role (Farmer or Buyer).")
                return redirect('register')
            user.set_password(raw_password)
            user.save()
            UserProfile.objects.create(user=user, role=role)
           
            # ✅ Send welcome email in background
            threading.Thread(
                target=send_welcome_email, args=(user, request), daemon=True
            ).start()

            messages.success(request, "Account created successfully. Please login.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'marketplace/register.html', {'user_form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             role = UserProfile.objects.get(user=user).role
#             return redirect('farmer_dashboard' if role == 'farmer' else 'buyer_dashboard')
#         else:
#             messages.error(request, "Invalid credentials")
#     return render(request, 'marketplace/login.html', {'form': ''})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            try:
                role = UserProfile.objects.get(user=user).role
                if role == 'farmer':
                    messages.success(request, "Welcome back! You are now logged in.")
                    return redirect('home')
                elif role == 'buyer':
                    messages.success(request, "Welcome back! You are now logged in.")
                    return redirect('home')
                else:
                    messages.error(request, "Unknown role")
            except UserProfile.DoesNotExist:
                messages.error(request, "User profile not found")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'marketplace/login.html', {'form': ''})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# ========== HOMEPAGE & DASHBOARDS ==========



@login_required
def farmer_dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role != 'farmer':
            messages.error(request, "You are not authorized to access the farmer dashboard.")
            return redirect('home')
    except UserProfile.DoesNotExist:
        messages.error(request, "User profile not found. Please complete your profile setup.")
        return redirect('home')
    
    # Dashboard Stats for New UI
    my_products = Product.objects.filter(seller=request.user)
    total_listings = my_products.count()
    
    orders_received = Order.objects.filter(product__seller=request.user)
    total_orders = orders_received.count()
    active_orders = orders_received.filter(status='Pending').count()
    
    total_revenue = orders_received.filter(payment_status='Paid').aggregate(Sum('total_price'))['total_price__sum'] or 0
    
    context = {
        'is_farmer': True,
        'total_listings': total_listings,
        'total_orders': total_orders,
        'active_orders': active_orders,
        'total_revenue': total_revenue,
        'my_products': my_products[:5], # Recent listings
        'recent_orders': orders_received.order_by('-created_at')[:5]
    }
    return render(request, 'marketplace/farmer_dashboard.html', context)



@login_required
def buyer_dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role != 'buyer':
            messages.error(request, "You are not authorized to access the buyer dashboard.")
            return redirect('home')
    except UserProfile.DoesNotExist:
        messages.error(request, "User profile not found. Please complete your profile setup.")
        return redirect('home')
    orders = Order.objects.filter(buyer=request.user)
    total_spent = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0
    active_orders = orders.filter(status='pending').count()
    
    context = {
        'total_spent': total_spent,
        'active_orders': active_orders,
        'recent_orders': orders.order_by('-created_at')[:5],
        'is_farmer': False
    }
    return render(request, 'marketplace/buyer_dashboard.html', context)

# ========== PRODUCT MANAGEMENT ==========

@login_required
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            
            # Get and compress images before saving
            images = request.FILES.getlist('images')
            compressed_images = compress_images_batch(images)
            
            for img in compressed_images:
                ProductImage.objects.create(product=product, image=img)
            
            messages.success(request, "Product uploaded successfully with optimized images!")
            return redirect('farmer_dashboard')
    else:
        form = ProductForm()
    return render(request, 'direct-selling/upload_product.html', {'form': form})

@login_required
def my_products(request):
    products = Product.objects.filter(seller=request.user)
    return render(request, 'direct-selling/my_products.html', {'products': products})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('my_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'direct-selling/edit_product.html', {'form': form, 'product': product})

def product_list(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.select_related('seller').prefetch_related('images').all()
    if form.is_valid() and form.cleaned_data['q']:
        query = form.cleaned_data['q']
        products = products.filter(
            Q(name__icontains=query) |
            Q(seller__username__icontains=query)
        )
    return render(request, 'direct-selling/product_list.html', {'products': products, 'form': form})


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    product.delete()
    return redirect('my_products')  # make sure 'my_products' is your name in urls.py

@login_required
@require_http_methods(["GET", "POST"])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    images = product.images.all()
    reviews = product.reviews.order_by('-created_at')
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if rating and comment:
            Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)
            messages.success(request, 'Review submitted successfully.')
            return redirect('product_detail', pk=pk)
    return render(request, 'direct-selling/product_detail.html', {'product': product, 'images': images, 'reviews': reviews})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user == request.user:
        review.delete()
        messages.success(request, 'Review deleted successfully.')
    else:
        messages.error(request, 'You can only delete your own review.')
    return redirect('product_detail', pk=review.product.pk)

# ========== CART AND ORDER ==========

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, _ = CartItem.objects.get_or_create(user=request.user, product=product)
    cart_item.unit = request.POST.get("unit", product.unit)
    cart_item.quantity = cart_item.quantity or 1
    cart_item.save()
    return redirect(request.GET.get('next') or 'product_list')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product').prefetch_related('product__images')
    for item in cart_items:
        item.item_total_price = (item.product.price_per_unit or Decimal('0.00')) * (item.quantity or 0)
    total_price = sum(item.item_total_price for item in cart_items)
    amount_in_paise = int(total_price * Decimal('100'))

    form = OrderForm()
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form,
        'RAZORPAY_KEY_ID': getattr(settings, 'RAZORPAY_KEY_ID', ''),
        'amount_in_paise': amount_in_paise
    }
    return render(request, 'direct-selling/cart.html', context)
    # return render(request, 'direct-selling/cart.html', {'cart_items': cart_items, 'total_price': total_price, 'form': OrderForm()})

@login_required
@require_POST
def update_cart(request):
    for item in CartItem.objects.filter(user=request.user):
        try:
            qty = int(request.POST.get(f'quantity_{item.id}', '').strip() or 1)
            item.quantity = qty
            item.unit = request.POST.get(f'unit_{item.id}', '').strip() or item.unit
            item.save()
        except (ValueError, TypeError):
            continue
    messages.success(request, "Cart updated successfully.")
    return redirect('cart')

@login_required
@csrf_exempt
def create_razorpay_order(request):
    """
    AJAX endpoint to create a Razorpay order. Expects JSON: {"amount": <amount_in_paise>}
    Returns: order JSON from Razorpay.
    """
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    try:
        data = json.loads(request.body.decode('utf-8') or '{}')
        amount = int(data.get('amount', 0))
    except Exception:
        return HttpResponseBadRequest("Invalid request data")

    if amount <= 0:
        return HttpResponseBadRequest("Invalid amount")

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    try:
        razorpay_order = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': 1
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse(razorpay_order)




# @login_required
# @require_POST
# def place_order(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     if not cart_items.exists():
#         messages.error(request, "Your cart is empty.")
#         return redirect('cart')
#     form = OrderForm(request.POST)
#     if form.is_valid():
#         for item in cart_items:
#             Order.objects.create(
#                 buyer=request.user,
#                 product=item.product,
#                 quantity=item.quantity,
#                 total_price=item.product.price_per_unit * item.quantity,
#                 **form.cleaned_data
#             )
#         cart_items.delete()
#         messages.success(request, "✅ Your order has been placed successfully.")
#         return redirect('order_success')
#     messages.error(request, "❌ Please correct the errors in the shipping form.")
#     return render(request, 'direct-selling/cart.html', {'cart_items': cart_items, 'total_price': sum(item.item_total_price for item in cart_items), 'form': form})

@login_required
@require_POST
def place_order(request):
    """
    Handles both COD and Online payments.
    - For COD: create Order entries and clear cart.
    - For Online: verify Razorpay signature, save payment ids in Order, mark paid, clear cart.
    """
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect('cart')

    form = OrderForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Please correct the errors in the form.")
        # re-render cart with form errors
        # compute total again
        total_price = sum((ci.product.price_per_unit or Decimal('0.00')) * ci.quantity for ci in cart_items)
        return render(request, 'direct-selling/cart.html', {
            'cart_items': cart_items,
            'total_price': total_price,
            'form': form,
            'RAZORPAY_KEY_ID': getattr(settings, 'RAZORPAY_KEY_ID', '')
        })

    payment_method = form.cleaned_data['payment_method']
    total_price = sum((ci.product.price_per_unit or Decimal('0.00')) * ci.quantity for ci in cart_items)

    if payment_method == 'cod':
        # create an Order per item (you can change to aggregated order if you prefer)
        for item in cart_items:
            Order.objects.create(
                buyer=request.user,
                product=item.product,
                quantity=item.quantity,
                address=form.cleaned_data['address'],
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                payment_method='cod',
                total_price=item.product.price_per_unit * item.quantity,
                status='Pending',
                payment_status='Pending'
            )
        cart_items.delete()
        messages.success(request, "✅ Order placed successfully (Cash on Delivery).")
        return redirect('my_orders')

    elif payment_method == 'online':
        # verify Razorpay signature posted by client after checkout
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        if not (razorpay_payment_id and razorpay_order_id and razorpay_signature):
            messages.error(request, "Missing payment details. Please try again.")
            return redirect('cart')

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)
        except razorpay.errors.SignatureVerificationError:
            messages.error(request, "Payment verification failed. Please contact support.")
            return redirect('cart')
        except Exception:
            messages.error(request, "Payment verification failed. Please contact support.")
            return redirect('cart')

        # signature verified — save Orders with payment info
        for item in cart_items:
            Order.objects.create(
                buyer=request.user,
                product=item.product,
                quantity=item.quantity,
                address=form.cleaned_data['address'],
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                payment_method='online',
                total_price=item.product.price_per_unit * item.quantity,
                status='Pending',
                payment_status='Paid',
                razorpay_order_id=razorpay_order_id,
                razorpay_payment_id=razorpay_payment_id,
                razorpay_signature=razorpay_signature
            )
        cart_items.delete()
        messages.success(request, "✅ Payment successful and order placed.")
        return redirect('my_orders')

    # fallback
    messages.error(request, "Unknown payment method.")
    return redirect('cart')




@login_required
def delete_cart_item(request, item_id):
    get_object_or_404(CartItem, id=item_id, user=request.user).delete()
    return redirect('cart')

@login_required
def order_success(request):
    return render(request, 'direct-selling/order_success.html')

@login_required
def my_orders(request):
    orders = Order.objects.filter(buyer=request.user).order_by('-created_at')
    return render(request, 'direct-selling/my_orders.html', {'orders': orders})

@login_required
def farmer_orders(request):
    orders = Order.objects.filter(product__seller=request.user).order_by('-created_at')
    return render(request, 'direct-selling/farmer_orders.html', {'orders': orders})


# # ================== RAZORPAY PAYMENT ==================
# @login_required
# def checkout_payment(request):
#     """
#     Buyer checkout page with Razorpay payment integration
#     """
#     if UserProfile.objects.get(user=request.user).role != 'buyer':
#         messages.error(request, "Only buyers can checkout.")
#         return redirect('home')

#     cart_items = CartItem.objects.filter(user=request.user)
#     if not cart_items.exists():
#         messages.error(request, "Your cart is empty.")
#         return redirect('cart')

#     # Calculate total price
#     total_amount = sum(
#         (item.product.price_per_unit or Decimal('0.00')) * (item.quantity or 0)
#         for item in cart_items
#     )
#     amount_in_paise = int(total_amount * 100)

#     # Create Razorpay order
#     client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#     payment_order = client.order.create({
#         "amount": amount_in_paise,
#         "currency": "INR",
#         "payment_capture": 1
#     })

#     context = {
#         "cart_items": cart_items,
#         "total_amount": total_amount,
#         "amount_in_paise": amount_in_paise,
#         "api_key": settings.RAZORPAY_KEY_ID,
#         "order_id": payment_order["id"]
#     }
#     return render(request, "direct-selling/checkout_payment.html", context)


# @require_POST
# @login_required
# def payment_success(request):
#     """
#     Handle payment success callback from Razorpay
#     """
#     params_dict = {
#         'razorpay_order_id': request.POST.get('razorpay_order_id'),
#         'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
#         'razorpay_signature': request.POST.get('razorpay_signature')
#     }

#     client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

#     try:
#         # Verify signature to ensure payment is authentic
#         client.utility.verify_payment_signature(params_dict)
#     except razorpay.errors.SignatureVerificationError:
#         messages.error(request, "Payment verification failed. Please contact support.")
#         return redirect('cart')

    # Save the order in DB
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        Order.objects.create(
            buyer=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.product.price_per_unit * item.quantity,
            shipping_address="Payment done via Razorpay"
        )
    cart_items.delete()

    messages.success(request, "✅ Payment successful! Your order has been placed.")
    return redirect('my_orders')


@login_required
@require_POST
def mark_order_completed(request, order_id):
    order = get_object_or_404(Order, id=order_id, product__seller=request.user)
    if order.status != 'Completed':
        order.status = 'Completed'
        order.save()
        messages.success(request, f"Order #{order.id} marked as completed.")
    return redirect('farmer_orders')


# ========== QUALITY INPUTS MARKETPLACE ==========

@login_required
def upload_quality_input(request):
    if request.method == 'POST':
        form = QualityInputForm(request.POST, request.FILES)

        if form.is_valid():
            quality_input = form.save(commit=False)
            quality_input.seller = request.user
            quality_input.save()
            
            # Get and compress images before saving
            images = request.FILES.getlist('images')
            compressed_images = compress_images_batch(images)
            
            for img in compressed_images:
                QualityInputImage.objects.create(quality_input=quality_input, image=img)
            
            messages.success(request, "Quality input uploaded successfully with optimized images!")
            return redirect('farmer_dashboard')
    else:
        form = QualityInputForm()
    return render(request, 'quality-inputs/upload_quality_input.html', {'form': form})


@login_required
def quality_input_list(request):
    form = QualityInputSearchForm(request.GET or None)
    quality_inputs = QualityInput.objects.select_related('seller').all()
    if form.is_valid() and form.cleaned_data['q']:
        query = form.cleaned_data['q']
        quality_inputs = quality_inputs.filter(
            Q(name__icontains=query) |
            Q(seller__username__icontains=query)
        )
    return render(request, 'quality-inputs/quality_input_list.html', {'quality_inputs': quality_inputs, 'form': form})


@login_required
def my_quality_inputs(request):
    quality_inputs = QualityInput.objects.filter(seller=request.user)
    return render(request, 'quality-inputs/my_quality_inputs.html', {'quality_inputs': quality_inputs})


@login_required
def edit_quality_input(request, quality_input_id):
    quality_input = get_object_or_404(QualityInput, id=quality_input_id, seller=request.user)
    if request.method == 'POST':
        form = QualityInputForm(request.POST, request.FILES, instance=quality_input)
        if form.is_valid():
            form.save()
            return redirect('my_quality_inputs')
    else:
        form = QualityInputForm(instance=quality_input)
    return render(request, 'quality-inputs/edit_quality_input.html', {'form': form, 'quality_input': quality_input})


@login_required
def delete_quality_input(request, quality_input_id):
    quality_input = get_object_or_404(QualityInput, id=quality_input_id, seller=request.user)
    quality_input.delete()
    return redirect('my_quality_inputs')


@login_required
@require_http_methods(["GET", "POST"])
def quality_input_detail(request, pk):
    quality_input = get_object_or_404(QualityInput, pk=pk)
    images = quality_input.images.all()
    reviews = quality_input.reviews.order_by('-created_at')
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if rating and comment:
            QualityInputReview.objects.create(quality_input=quality_input, user=request.user, rating=rating, comment=comment)
            messages.success(request, 'Review submitted successfully.')
            return redirect('quality_input_detail', pk=pk)
    return render(request, 'quality-inputs/quality_input_detail.html', {'quality_input': quality_input, 'images': images, 'reviews': reviews})


@login_required
def delete_quality_input_review(request, review_id):
    review = get_object_or_404(QualityInputReview, id=review_id)
    if review.user == request.user:
        review.delete()
        messages.success(request, 'Review deleted successfully.')
    else:
        messages.error(request, 'You can only delete your own review.')
    return redirect('quality_input_detail', pk=review.quality_input.pk)


# ========== QUALITY INPUT CART AND ORDER ==========

@login_required
def add_quality_input_to_cart(request, quality_input_id):
    quality_input = get_object_or_404(QualityInput, id=quality_input_id)
    cart_item, _ = QualityInputCartItem.objects.get_or_create(user=request.user, quality_input=quality_input)
    cart_item.unit = request.POST.get("unit", quality_input.unit)
    cart_item.quantity = cart_item.quantity or 1
    cart_item.save()
    return redirect(request.GET.get('next') or 'quality_input_list')


@login_required
def quality_input_cart(request):
    cart_items = QualityInputCartItem.objects.filter(user=request.user)
    for item in cart_items:
        item.item_total_price = (item.quality_input.price_per_unit or Decimal('0.00')) * (item.quantity or 0)
    total_price = sum(item.item_total_price for item in cart_items)
    amount_in_paise = int(total_price * Decimal('100'))

    form = QualityInputOrderForm()
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form,
        'RAZORPAY_KEY_ID': getattr(settings, 'RAZORPAY_KEY_ID', ''),
        'amount_in_paise': amount_in_paise
    }
    return render(request, 'quality-inputs/quality_input_cart.html', context)


@login_required
@require_POST
def update_quality_input_cart(request):
    for item in QualityInputCartItem.objects.filter(user=request.user):
        try:
            qty = int(request.POST.get(f'quantity_{item.id}', '').strip() or 1)
            item.quantity = qty
            item.unit = request.POST.get(f'unit_{item.id}', '').strip() or item.unit
            item.save()
        except (ValueError, TypeError):
            continue
    messages.success(request, "Cart updated successfully.")
    return redirect('quality_input_cart')


@login_required
def delete_quality_input_cart_item(request, item_id):
    get_object_or_404(QualityInputCartItem, id=item_id, user=request.user).delete()
    return redirect('quality_input_cart')


@login_required
@require_POST
def place_quality_input_order(request):
    """
    Handles both COD and Online payments for quality inputs.
    """
    cart_items = QualityInputCartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect('quality_input_cart')

    form = QualityInputOrderForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Please correct the errors in the form.")
        total_price = sum((ci.quality_input.price_per_unit or Decimal('0.00')) * ci.quantity for ci in cart_items)
        return render(request, 'quality-inputs/quality_input_cart.html', {
            'cart_items': cart_items,
            'total_price': total_price,
            'form': form,
            'RAZORPAY_KEY_ID': getattr(settings, 'RAZORPAY_KEY_ID', '')
        })

    payment_method = form.cleaned_data['payment_method']
    total_price = sum((ci.quality_input.price_per_unit or Decimal('0.00')) * ci.quantity for ci in cart_items)

    if payment_method == 'cod':
        for item in cart_items:
            QualityInputOrder.objects.create(
                buyer=request.user,
                quality_input=item.quality_input,
                quantity=item.quantity,
                address=form.cleaned_data['address'],
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                payment_method='cod',
                total_price=item.quality_input.price_per_unit * item.quantity,
                status='Pending',
                payment_status='Pending'
            )
        cart_items.delete()
        messages.success(request, "✅ Order placed successfully (Cash on Delivery).")
        return redirect('quality_input_my_orders')

    elif payment_method == 'online':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        if not (razorpay_payment_id and razorpay_order_id and razorpay_signature):
            messages.error(request, "Missing payment details. Please try again.")
            return redirect('quality_input_cart')

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)
        except razorpay.errors.SignatureVerificationError:
            messages.error(request, "Payment verification failed. Please contact support.")
            return redirect('quality_input_cart')
        except Exception:
            messages.error(request, "Payment verification failed. Please contact support.")
            return redirect('quality_input_cart')

        for item in cart_items:
            QualityInputOrder.objects.create(
                buyer=request.user,
                quality_input=item.quality_input,
                quantity=item.quantity,
                address=form.cleaned_data['address'],
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                payment_method='online',
                total_price=item.quality_input.price_per_unit * item.quantity,
                status='Pending',
                payment_status='Paid',
                razorpay_order_id=razorpay_order_id,
                razorpay_payment_id=razorpay_payment_id,
                razorpay_signature=razorpay_signature
            )
        cart_items.delete()
        messages.success(request, "✅ Payment successful and order placed.")
        return redirect('quality_input_my_orders')

    messages.error(request, "Unknown payment method.")
    return redirect('quality_input_cart')


@login_required
def quality_input_my_orders(request):
    orders = QualityInputOrder.objects.filter(buyer=request.user).order_by('-created_at')
    return render(request, 'quality-inputs/quality_input_my_orders.html', {'orders': orders})


@login_required
def quality_input_farmer_orders(request):
    orders = QualityInputOrder.objects.filter(quality_input__seller=request.user).order_by('-created_at')
    return render(request, 'quality-inputs/quality_input_farmer_orders.html', {'orders': orders})


@login_required
@require_POST
def mark_quality_input_order_completed(request, order_id):
    order = get_object_or_404(QualityInputOrder, id=order_id, quality_input__seller=request.user)
    if order.status != 'Completed':
        order.status = 'Completed'
        order.save()
        messages.success(request, f"Order #{order.id} marked as completed.")
    return redirect('quality_input_farmer_orders')


# ========== OTHER FEATURES ==========

# @login_required
# def profile(request):
#     profile = FarmerProfile.objects.filter(user=request.user).first()
#     return render(request, 'marketplace/profile.html', {'profile': profile})
# aaj yaha pe change kiye h 
@login_required
def profile(request):
    user = request.user
    role = user.userprofile.role  # Assuming you have a UserProfile model connected to User

    if role == "farmer":
        profile = FarmerProfile.objects.filter(user=user).first()
    elif role == "buyer":
        profile = BuyerProfile.objects.filter(user=user).first()
    else:
        profile = None

    return render(request, 'marketplace/profile.html', {
        'user': user,
        'role': role,
        'profile': profile
    })




@login_required
def ai_intelligence_hub(request):
    return render(request, 'marketplace/ai_suite.html')

@login_required
def crop_price_view(request):
    crop_prices = CropPrice.objects.all().order_by('crop_name')
    return render(request, 'marketplace/crop_price.html', {'crop_prices': crop_prices})

import joblib

# Crop Prediction Global Variables
_crop_scaler = None
_crop_model = None
_crop_label_encoder = None

def get_crop_models():
    global _crop_scaler, _crop_model, _crop_label_encoder
    if _crop_model is None:
        try:
            _crop_scaler = joblib.load(os.path.join(settings.BASE_DIR, 'ml_models', 'scaler.pkl'))
            _crop_model = joblib.load(os.path.join(settings.BASE_DIR, 'ml_models', 'crop_model.pkl'))
            _crop_label_encoder = joblib.load(os.path.join(settings.BASE_DIR, 'ml_models', 'label_encoder.pkl'))
        except Exception as e:
            _crop_scaler = _crop_model = _crop_label_encoder = None
            print(f'Warning: Could not load crop models: {e}')
    return _crop_scaler, _crop_model, _crop_label_encoder

@login_required
def predict_crop(request):
    result, input_values, top_recommendations = None, None, None
    best_confidence = 0
    
    if request.method == 'POST':
        form = CropInputForm(request.POST)
        if form.is_valid():
            input_values = form.cleaned_data
            # Safety check for loaded models
            crop_scaler, crop_model, crop_label_encoder = get_crop_models()
            if not all([crop_scaler, crop_model, crop_label_encoder]):
                messages.error(request, 'Crop recommendation model is currently unavailable.')
                return render(request, 'marketplace/predict_crop.html', {'form': form})

            data = [
                input_values['nitrogen'], 
                input_values['phosphorus'],
                input_values['potassium'], 
                input_values.get('temperature', 0),
                input_values.get('humidity', 0),
                input_values['pH'],
                input_values.get('rainfall', 0)
            ]
            scaled = crop_scaler.transform([data])
            
            # Extract probabilities for all classes
            probs = crop_model.predict_proba(scaled)[0]
            
            # Get indices of top 3 probabilities
            top_3_indices = probs.argsort()[-3:][::-1]
            
            # Decode indices to crop names and format percentages
            top_recommendations = []
            for idx in top_3_indices:
                crop_name = crop_label_encoder.inverse_transform([idx])[0].capitalize()
                confidence = round(probs[idx] * 100, 2)
                top_recommendations.append({
                    'name': crop_name,
                    'confidence': confidence
                })
            
            # Set the primary result
            result = top_recommendations[0]['name']
            best_confidence = top_recommendations[0]['confidence']
            form = CropInputForm()
    else:
        form = CropInputForm()
        
    context = {
        'form': form, 
        'result': result, 
        'input_values': input_values,
        'top_recommendations': top_recommendations,
        'best_confidence': best_confidence
    }
    return render(request, 'marketplace/predict_crop.html', context)

# Yield Prediction

def load_model_asset(filename, description):
    model_path = Path(settings.BASE_DIR) / 'ml_models' / filename
    try:
        if not model_path.exists():
            print(f"Error: {description} file NOT FOUND at {model_path}")
            return None
        return joblib.load(model_path)
    except Exception as e:
        print(f'Critical Error: Could not load {description} from {model_path}: {e}')
        # Log the specific error type to help diagnosis
        import traceback
        traceback.print_exc()
        return None

# Yield Prediction Global Variables
_yield_model = None
_yield_scaler = None
_le_crop = None
_le_season = None
_le_state = None

def get_yield_models():
    global _yield_model, _yield_scaler, _le_crop, _le_season, _le_state
    if _yield_model is None:
        try:
            # Prioritize the lightweight XGBoost model (400KB) to completely avoid Render OOM crashes
            # Fallback to the compressed ensemble (189MB) or original (715MB) if lite model is missing
            model_path = Path(settings.BASE_DIR) / 'ml_models'
            if (model_path / 'yield_model_lite.pkl').exists():
                model_file = 'yield_model_lite.pkl'
            elif (model_path / 'yield_model_compressed.pkl').exists():
                model_file = 'yield_model_compressed.pkl'
            else:
                model_file = 'yield_model.pkl'
            
            _yield_model = load_model_asset(model_file, 'yield model')
            _yield_scaler = load_model_asset('yield_scaler.pkl', 'yield scaler')
            _le_crop = load_model_asset('le_crop.pkl', 'crop label encoder')
            _le_season = load_model_asset('le_season.pkl', 'season label encoder')
            _le_state = load_model_asset('le_state.pkl', 'state label encoder')
        except Exception as e:
            print(f'Warning: Could not load yield models: {e}')
    return _yield_model, _yield_scaler, _le_crop, _le_season, _le_state

@login_required
def yeild_predict(request):
    prediction, entered_data = None, None
    total_production, conf_low, conf_high = None, None, None
    if request.method == 'POST':
        form = YieldPredictionForm(request.POST)
        if form.is_valid():
            entered_data = form.cleaned_data
            
            # 1. Encode Categorical variables
            yield_model, yield_scaler, le_crop, le_season, le_state = get_yield_models()
            try:
                # Extra safety checks for encoders
                crop_val = entered_data['crop']
                season_val = entered_data['season']
                state_val = entered_data['state']

                crop_enc = le_crop.transform([crop_val])[0] if le_crop else 0
                season_enc = le_season.transform([season_val])[0] if le_season else 0
                state_enc = le_state.transform([state_val])[0] if le_state else 0
            except Exception as e:
                # Fallback if encoder fails
                print(f"Encoding failed for yield prediction: {e}")
                crop_enc = season_enc = state_enc = 0

            # 2. Extract Numerical variables
            crop_year = entered_data['year']
            area = entered_data['area']
            rainfall = entered_data['rainfall']
            fertilizer = entered_data['fertilizer']
            pesticide = entered_data['pesticide']
            historical_yield = entered_data.get('historical_yield', 0)

            # 3. Feature Engineering
            # Features: [Crop_enc, Season_enc, State_enc, Crop_Year, Area, Annual_Rainfall, Fertilizer, Pesticide, 
            #           Fertilizer_per_Area, Pesticide_per_Area, Production_per_Area, Rain_Fertilizer]
            
            fert_per_area = fertilizer / area if area > 0 else 0
            pest_per_area = pesticide / area if area > 0 else 0
            rain_fert = rainfall * fertilizer
            
            features = [
                crop_enc, season_enc, state_enc, crop_year, area, 
                rainfall, fertilizer, pesticide,
                fert_per_area, pest_per_area, historical_yield, rain_fert
            ]

            if not yield_model or not yield_scaler:
                messages.error(request, 'Yield prediction model assets are unavailable. Please try again later.')
            else:
                try:
                    X_scaled = yield_scaler.transform([features])
                    log_pred = yield_model.predict(X_scaled)[0]
                    
                    # 5. Inverse Log Transform (log1p -> expm1)
                    prediction = round(np.expm1(log_pred), 2)
                    
                    # 6. Farm Scale Projections
                    total_production = round(prediction * area, 2)
                    # Statistical confidence band (simulated based on model R2 of 99.7%)
                    conf_margin = prediction * 0.05
                    conf_low = round(max(0, prediction - conf_margin), 3)
                    conf_high = round(prediction + conf_margin, 3)
                except Exception as e:
                    messages.error(request, 'Unable to generate yield prediction at this time.')
                    print(f'Yield prediction failed: {e}')
            
            form = YieldPredictionForm()
    else:
        form = YieldPredictionForm()
    return render(request, 'marketplace/yield_predict.html', {
        'form': form, 
        'prediction': prediction, 
        'entered_data': entered_data,
        'total_production': total_production,
        'conf_low': conf_low,
        'conf_high': conf_high
    })

@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for contacting us. We will get back to you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'marketplace/contact.html', {'form': form})

