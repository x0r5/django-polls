from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # home page for products
    path('list-all/', views.ProductListView.as_view(), name = 'list-all'), #class called as a view
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]