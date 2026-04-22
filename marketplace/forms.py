from django import forms
from django.contrib.auth.models import User
from .models import (
    FarmerProfile, BuyerProfile, Crop, Contact,
    Product, Order, ProductImage, Review,
    QualityInput, QualityInputOrder, QualityInputImage, QualityInputReview
)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    ROLE_CHOICES = (('farmer', 'Farmer'), ('buyer', 'Buyer'))
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    # Farmer Fields
    farm_name = forms.CharField(required=False)
    location = forms.CharField(required=False)
    farmer_contact = forms.CharField(required=False, label="Farmer Contact Number")

    # Buyer Fields
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False, widget=forms.Textarea)
    company_name = forms.CharField(required=False)
    buyer_contact = forms.CharField(required=False, label="Buyer Contact Number")

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


# ✅ Farmer Profile Form
class FarmerProfileForm(forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ['farm_name', 'location', 'contact_number']
        widgets = {
            'farm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

# ✅ Buyer Profile Form (✅ FIXED)
class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model = BuyerProfile
        fields = ['phone', 'address', 'company_name', 'contact_number']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

# ✅ Crop Prediction Form
class CropInputForm(forms.Form):
    nitrogen = forms.FloatField(label='Nitrogen (%)')
    phosphorus = forms.FloatField(label='Phosphorus (%)')
    potassium = forms.FloatField(label='Potassium (%)')
    pH = forms.FloatField(label='pH Level')
    temperature = forms.FloatField(label='Temperature (°C)', required=False)
    humidity = forms.FloatField(label='Humidity (%)', required=False)
    rainfall = forms.FloatField(label='Rainfall (mm)', required=False)

# ✅ Yield Prediction Choices
STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')
]

SEASON_CHOICES = [
    ('Autumn', 'Autumn'), ('Kharif', 'Kharif'), ('Rabi', 'Rabi'), ('Summer', 'Summer'), ('Whole Year', 'Whole Year'), ('Winter', 'Winter')
]

CROP_YIELD_CHOICES = [
    ('Arecanut', 'Arecanut'), ('Arhar/Tur', 'Arhar/Tur'), ('Bajra', 'Bajra'), ('Banana', 'Banana'), ('Barley', 'Barley'),
    ('Black pepper', 'Black pepper'), ('Cardamom', 'Cardamom'), ('Cashewnut', 'Cashewnut'), ('Castor seed', 'Castor seed'),
    ('Coconut', 'Coconut'), ('Coriander', 'Coriander'), ('Cotton(lint)', 'Cotton(lint)'), ('Cowpea(Lobia)', 'Cowpea(Lobia)'),
    ('Dry chillies', 'Dry chillies'), ('Garlic', 'Garlic'), ('Ginger', 'Ginger'), ('Gram', 'Gram'), ('Groundnut', 'Groundnut'),
    ('Guar seed', 'Guar seed'), ('Horse-gram', 'Horse-gram'), ('Jowar', 'Jowar'), ('Jute', 'Jute'), ('Khesari', 'Khesari'),
    ('Linseed', 'Linseed'), ('Maize', 'Maize'), ('Masoor', 'Masoor'), ('Mesta', 'Mesta'), ('Moong(Green Gram)', 'Moong(Green Gram)'),
    ('Moth', 'Moth'), ('Niger seed', 'Niger seed'), ('Oilseeds total', 'Oilseeds total'), ('Onion', 'Onion'),
    ('Other Rabi pulses', 'Other Rabi pulses'), ('Other Cereals', 'Other Cereals'), ('Other Kharif pulses', 'Other Kharif pulses'),
    ('Other Summer Pulses', 'Other Summer Pulses'), ('Peas & beans (Pulses)', 'Peas & beans (Pulses)'), ('Potato', 'Potato'),
    ('Ragi', 'Ragi'), ('Rapeseed &Mustard', 'Rapeseed &Mustard'), ('Rice', 'Rice'), ('Safflower', 'Safflower'),
    ('Sannhamp', 'Sannhamp'), ('Sesamum', 'Sesamum'), ('Small millets', 'Small millets'), ('Soyabean', 'Soyabean'),
    ('Sugarcane', 'Sugarcane'), ('Sunflower', 'Sunflower'), ('Sweet potato', 'Sweet potato'), ('Tapioca', 'Tapioca'),
    ('Tobacco', 'Tobacco'), ('Turmeric', 'Turmeric'), ('Urad', 'Urad'), ('Wheat', 'Wheat'), ('other oilseeds', 'other oilseeds')
]

class YieldPredictionForm(forms.Form):
    state = forms.ChoiceField(label='State', choices=STATE_CHOICES)
    crop = forms.ChoiceField(label='Crop Type', choices=CROP_YIELD_CHOICES)
    season = forms.ChoiceField(label='Season', choices=SEASON_CHOICES)
    year = forms.IntegerField(label='Crop Year')
    area = forms.FloatField(label='Area (Hectares)')
    rainfall = forms.FloatField(label='Annual Rainfall (mm)')
    fertilizer = forms.FloatField(label='Fertilizer Used (kg)')
    pesticide = forms.FloatField(label='Pesticide Used (kg)')
    historical_yield = forms.FloatField(label='Previous Production per Area (Optional)', required=False, initial=0)


# ✅ Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# ✅ Product Form with Multiple Images
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'price_per_unit', 'unit', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

# ✅ Order Form
PAYMENT_CHOICES = [
    ('cod', 'Cash on Delivery'),
    ('online', 'Online Payment'),
]

class OrderForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter delivery address'})
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'payment_method']

# ✅ Cart Quantity Update Form
class CartQuantityForm(forms.Form):
    quantity = forms.IntegerField(
        required=True,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control text-center',
            'placeholder': 'Enter quantity',
        })
    )

# ✅ Product Search Form
class ProductSearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by product name or seller username',
            'class': 'form-control'
        })
    )

# ✅ Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'Write your feedback...'}),
        }


# ✅ Quality Input Form (for uploading quality inputs)
class QualityInputForm(forms.ModelForm):
    class Meta:
        model = QualityInput
        fields = ['name', 'category', 'description', 'manufacturer', 'certification', 'quantity', 'price_per_unit', 'unit', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'certification': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }


# ✅ Quality Input Order Form
class QualityInputOrderForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter delivery address'})
    )
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = QualityInputOrder
        fields = ['full_name', 'email', 'phone', 'address', 'payment_method']


# ✅ Quality Input Search Form
class QualityInputSearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by product name or seller username',
            'class': 'form-control'
        })
    )


# ✅ Quality Input Review Form
class QualityInputReviewForm(forms.ModelForm):
    class Meta:
        model = QualityInputReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'Write your feedback...'}),
        }
