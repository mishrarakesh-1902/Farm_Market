from django.contrib import admin
from .models import (
    FarmerProfile, Crop, BuyerProfile, CropPrice, Contact,
    Product, ProductImage, Order, CartItem, Review,
    QualityInput, QualityInputImage, QualityInputOrder, QualityInputCartItem, QualityInputReview
)

# Inline admin to allow uploading multiple images for a product from the admin panel
class ProductImageInline(admin.TabularInline):  # You can use StackedInline for a vertical layout
    model = ProductImage
    extra = 1  # Show one extra blank image form
    max_num = 10  # Optional: limit to 10 images per product

# Customize the Product admin view
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price_per_unit', 'quantity', 'unit', 'location', 'posted_on')
    list_filter = ('seller', 'location', 'posted_on')
    search_fields = ('name', 'description', 'location', 'seller__username')
    inlines = [ProductImageInline]

# Customize the Order admin view
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'product', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('buyer__username', 'product__name')

# Customize the Review admin view
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'comment')

# Inline admin for QualityInputImages
class QualityInputImageInline(admin.TabularInline):
    model = QualityInputImage
    extra = 1
    max_num = 10

# Customize the QualityInput admin view
class QualityInputAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'category', 'price_per_unit', 'quantity', 'unit', 'location', 'posted_on')
    list_filter = ('category', 'seller', 'location', 'posted_on')
    search_fields = ('name', 'description', 'location', 'seller__username')
    inlines = [QualityInputImageInline]

# Customize the QualityInputOrder admin view
class QualityInputOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'quality_input', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('buyer__username', 'quality_input__name')

# Customize the QualityInputReview admin view
class QualityInputReviewAdmin(admin.ModelAdmin):
    list_display = ('quality_input', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('quality_input__name', 'user__username', 'comment')

# Register all models
admin.site.register(FarmerProfile)
admin.site.register(Crop)
admin.site.register(BuyerProfile)
admin.site.register(CropPrice)
admin.site.register(Contact)
admin.site.register(Product, ProductAdmin)         # Custom admin with image inline
admin.site.register(ProductImage)                  # Standalone image model (optional)
admin.site.register(Order, OrderAdmin)             # Custom Order admin
admin.site.register(CartItem)
admin.site.register(Review, ReviewAdmin)           # Custom Review admin

# Register QualityInput models
admin.site.register(QualityInput, QualityInputAdmin)
admin.site.register(QualityInputImage)
admin.site.register(QualityInputOrder, QualityInputOrderAdmin)
admin.site.register(QualityInputCartItem)
admin.site.register(QualityInputReview, QualityInputReviewAdmin)
