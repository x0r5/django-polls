# Django ENV / letreform testsite

## Django App Structure: Model View Template
- urls.py: sends the request to the view
- views.py: loads the template (if any) and gets the data from the model
- models.py


## URLS.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('catalog/', include('catalog.urls')),
    re_path(r'^([0-9]+)/$', views.best),
]
```

