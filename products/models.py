from django.db import models
from django.utils.translation import ugettext_lazy as _
import os

# Create your models here.
# Many-to-Many relationship: 
# Cascade on delete: If a record in the parent table is deleted, then the corresponding records in the child table will automatically be deleted.

class Category(models.Model):
    name        = models.CharField(_('category name'),max_length=255)
    parent      = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name=_('parent category'), null=True, blank=True, related_name='children')
    description = models.TextField(_('category description'),null=True, blank=True)
    photo       = models.CharField(max_length=255, blank=True, null=True)
    is_published= models.BooleanField(_('is category published'))
    code        = models.CharField(max_length=128, null=True, blank=True, help_text='Kategória kódja')
    custom     = models.CharField(max_length=255, null=True, blank=True)

    # objects = CategoryManager()

    def __unicode__(self): # for python 2
        return self.name

    def __str__(self):
        return self.name

    def __copy__(self):
        copy_fields = ['name', 'parent', 
                'description', 'photo', 'code', 
                'is_published', 'custom']
        return self.__class__(**dict([(f, getattr(self,f))
            for f in copy_fields]))


class Attribute(models.Model):
    name        = models.CharField(_('attribute name'), max_length=255)
    ext_code    = models.CharField(max_length=128, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    
class Group(models.Model): 
    symbol = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
    

# Product class
class Product(models.Model):
    symbol      = models.CharField(max_length=128, blank=True) # ???
    category    = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE, related_name='products')
    name        = models.CharField(_('name'),max_length=255)
    short_desc  = models.TextField(_('short description'),null=True, blank=True)
    long_desc   = models.TextField(_('long description'),null=True, blank=True)
    is_published= models.BooleanField(_('is product published'))
    ext_code    = models.CharField(max_length=128, null=True, blank=True)
    price_net   = models.IntegerField(null=True, blank=True) #net price without taxes
    custom2     = models.CharField(max_length=255, null=True, blank=True)
    custom3     = models.CharField(max_length=255, null=True, blank=True)
    custom4     = models.CharField(max_length=255, null=True, blank=True)
    groups      = models.ManyToManyField(Group, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    

    def __copy__(self):
        copy_fields = ['symbol', 'name', 'short_desc',
            'long_desc', 'ext_code', 'is_published',
            'price_net', 'custom2', 'custom3', 'custom4']
        return self.__class__(**dict([(f, getattr(self,f))
            for f in copy_fields]))

    def photo(self):
        try: 
            return self.photos.all()[0]
        except IndexError:
            return None

    def intro(self):
        return self.short_desc or self.long_desc


class ProductPhoto(models.Model):
    product     = models.ForeignKey(Product, verbose_name=_('product'), related_name='photos', on_delete=models.CASCADE)
    image       = models.CharField(max_length=255, null=False, blank=False)
    display_order = models.PositiveIntegerField(null=False, blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
