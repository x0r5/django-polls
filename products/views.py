from django.shortcuts import render, redirect
from products.models import Product
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.contrib.auth import authenticate, login, logout

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_products = Product.objects.all().count()
    all_products = Product.objects.all()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    #num_authors = Author.objects.count()
    
    context = {
        'num_products': num_products,
        'all_products': all_products,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'  # Specify your own template name/location this is the default

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'

def loginUser(request):
    email= request.POST.get('email')
    password = request.POST.get('password')
	# stayloggedin = request.GET.get('stayloggedin')
	# if stayloggedin == "true":
	  #  pass
	# else:
	  #  request.session.set_expiry(0)
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse(json.dumps({"message": "Success"}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": "invalid"}),content_type="application/json")
    return HttpResponse(json.dumps({"message": "denied"}),content_type="application/json")

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')

def manage(request, cat='all'):

    all_products = Product.objects.all()
    # filter products based on arg: cat
    if cat == 'all':
        filtered_products = all_products
    elif cat == 'bio' or cat == 'reform':
        filtered_products = all_products.filter(category__name__icontains=cat)
    else:
        filtered_products = all_products

    

    context = {
        'products': filtered_products,
    }
    return render(request, 'manage.html', context)


def manage_product(request, id):
    selected = Product.objects.get(pk=id)

    context = {
        'product': selected,
    }
    return render(request, 'manage_product.html', context)