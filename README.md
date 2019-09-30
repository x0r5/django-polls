# Django Tutorial
Following: [link](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

## Tools Needed
- Ubuntu Server (18.04 LTS)
- Python 3 with pip3
	- `sudo apt install python3`
	- `sudo apt install python3-pip`
- Django
	- `pip3 install django`

## Init
1 `django-admin startproject mysite`
2 `python3 manage.py runserver 0:8000`
3 `puthon3 manage.py startapp polls`


## Create Views
- polls/views.py
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

- polls/urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- mysite/urls.py
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
