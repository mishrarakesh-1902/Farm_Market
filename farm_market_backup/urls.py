# from django.contrib import admin
# from django.urls import path
# from marketplace import views
# from marketplace.views import contact_view
# from django.conf import settings
# from django.conf.urls.static import static
# # from django.conf import settings
# # from django.conf.urls.static import static

# urlpatterns = [
#     path('admin12/', admin.site.urls),
#     path('', views.home, name='home'),  # Homepage
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('', views.product_list, name='product_list'),     
#     path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
#     path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
#     path('profile/', views.profile, name='profile'),  # User Profile 
#     path('predict-crop/', views.predict_crop, name='predict_crop'),
#     path('yeild-predict/', views.yeild_predict, name='yeild_predict'),
#     path('contact/', views.contact_view, name='contact'),
#     path('crop_price/', views.crop_price_view, name='crop_prices'),
#     path('direct-selling/upload/', views.upload_product, name='upload_product'),
#     path('direct-selling/', views.product_list, name='product_list'),
#     path('direct-selling/<int:pk>/', views.product_detail, name='product_detail'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/', views.cart, name='cart'),
    
#     path('order/success/', views.order_success, name='order_success'),
#     path('order/<int:order_id>/complete/', views.mark_order_completed, name='mark_order_completed'),

#     path('my_orders/', views.my_orders, name='my_orders'),
#     path('farmer_orders/', views.farmer_orders, name='farmer_orders'),
    
#     path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
#     path('farmer/my-products/', views.my_products, name='my_products'),

#     path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),

# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path
from marketplace import views
from marketplace.views import contact_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('admin12/', admin.site.urls),

    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboards
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),

    # Profile & Contact
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact_view, name='contact'),

    # Crop Prediction & Prices
    path('ai-suite/', views.ai_intelligence_hub, name='ai_intelligence_hub'),
    path('predict-crop/', views.predict_crop, name='predict_crop'),
    path('yeild-predict/', views.yeild_predict, name='yeild_predict'),
    path('crop_price/', views.crop_price_view, name='crop_prices'),


    # Product CRUD & Listing
    path('direct-selling/', views.product_list, name='product_list'),
    path('direct-selling/upload/', views.upload_product, name='upload_product'),
    path('direct-selling/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),

    # urls.py
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),

    # Cart & Order 
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('cart/update/', views.update_cart, name='update_cart'),  # POST update
    path('order/place/', views.place_order, name='place_order'),  # POST place order
    path('order/success/', views.order_success, name='order_success'),
    path('order/<int:order_id>/complete/', views.mark_order_completed, name='mark_order_completed'),

    # Orders Views
    path('my_orders/', views.my_orders, name='my_orders'),
    path('farmer_orders/', views.farmer_orders, name='farmer_orders'),
    # path('checkout-payment/', views.checkout_payment, name='checkout_payment'),
    # path('payment-success/', views.payment_success, name='payment_success'),
    # path('payment-failed/', views.payment_failed, name='payment_failed'),        # Failure redirect
    path('create-razorpay-order/', views.create_razorpay_order, name='create_razorpay_order'),
    # Product Management
    path('farmer/my-products/', views.my_products, name='my_products'),

    # ✅ New route for deleting a review
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),

    # ========== QUALITY INPUTS MARKETPLACE ==========
    
    # Quality Inputs CRUD & Listing
    path('quality-inputs/', views.quality_input_list, name='quality_input_list'),
    path('quality-inputs/upload/', views.upload_quality_input, name='upload_quality_input'),
    path('quality-inputs/<int:pk>/', views.quality_input_detail, name='quality_input_detail'),
    path('quality-inputs/edit/<int:quality_input_id>/', views.edit_quality_input, name='edit_quality_input'),
    path('quality-inputs/delete/<int:quality_input_id>/', views.delete_quality_input, name='delete_quality_input'),
    path('quality-inputs/my-products/', views.my_quality_inputs, name='my_quality_inputs'),

    # Quality Inputs Cart & Order
    path('quality-inputs/add-to-cart/<int:quality_input_id>/', views.add_quality_input_to_cart, name='add_quality_input_to_cart'),
    path('quality-inputs/cart/', views.quality_input_cart, name='quality_input_cart'),
    path('quality-inputs/cart/delete/<int:item_id>/', views.delete_quality_input_cart_item, name='delete_quality_input_cart_item'),
    path('quality-inputs/cart/update/', views.update_quality_input_cart, name='update_quality_input_cart'),
    path('quality-inputs/order/place/', views.place_quality_input_order, name='place_quality_input_order'),
    path('quality-inputs/my-orders/', views.quality_input_my_orders, name='quality_input_my_orders'),
    path('quality-inputs/seller-orders/', views.quality_input_farmer_orders, name='quality_input_farmer_orders'),
    path('quality-inputs/order/<int:order_id>/complete/', views.mark_quality_input_order_completed, name='mark_quality_input_order_completed'),

    # Quality Inputs Review
    path('quality-inputs/review/delete/<int:review_id>/', views.delete_quality_input_review, name='delete_quality_input_review'),

     # ✅ Password Reset URLs
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="auth/password_reset.html"), name="password_reset"),

    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(
        template_name="auth/password_reset_done.html"), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="auth/password_reset_confirm.html"), name="password_reset_confirm"),

    path("reset_done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="auth/password_reset_complete.html"), name="password_reset_complete"),



]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


