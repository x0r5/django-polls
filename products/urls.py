from django.urls import path, include
from django.conf.urls import url
from products import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'), # home page for webshop
    path('list-all/', views.ProductListView.as_view(), name = 'list-all'), #class called as a view
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    url('login/', views.loginUser, name='login'),
    path('manage/', views.manage, name='manage'),
    path('manage/<str:cat>/', views.manage),
    path('manage/product/<int:id>', views.manage_product),
    url(r'^logout/$', views.logout_view, name='logout'),
    
]