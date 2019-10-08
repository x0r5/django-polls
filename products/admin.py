from django.contrib import admin
from products.models import Category, Attribute, Group, Product, ProductPhoto
# Register your models here.
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Group)
admin.site.register(Product)
admin.site.register(ProductPhoto)
