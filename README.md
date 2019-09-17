# Django Build Your First App
> Following [this](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) guide.
>
>Only for educational use.

### Enviroment
- VMWare Ubuntu 18.04
- Python 3.6.8

### Required - Quick Start Guide
`sudo apt update`<br>
`sudo apt upgrade`

`sudo apt install python3 python3-pip`<br>
`sudo pip3 install django`

### Creating the First Project
`django-admin startproject mysite` <br>
`python3 manage.py runserver 0:8000`

### Create an App
`python3 manage.py startapp polls`

### Creating Views
**polls/view.py**<br>
```python
from django.http import HttpResponse
    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
```
