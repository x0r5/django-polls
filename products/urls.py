from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list-all/', views.ProductListView.as_view(), name = 'productlist'), #class called as a view
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]