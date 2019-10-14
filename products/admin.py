from django.contrib import admin
from products.models import Category, Attribute, Group, Product, ProductPhoto
# Register your models here.
#admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Group)
# admin.site.register(Product)
#admin.site.register(ProductPhoto)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published', 'code', 'price_net', 'created_at', 'updated_at')
    list_filter = ('category', 'is_published', 'groups')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_published')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'product', 'display_order')
    list_filter = ('product')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductPhoto, PhotoAdmin)
