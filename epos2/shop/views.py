from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.core.paginator import  Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def index(request):
    text_var = 'Nothing to see here!'
    return HttpResponse(text_var) 

# Category Views
def allProdCat(request, c_slug = None):
    catPage = None
    products = None
    if c_slug != None:
        catPage = get_object_or_404(Category, slug = c_slug)
        productsList = Product.objects.filter(Category=catPage,available=True)
    else:
        productsList = Product.objects.all().filter(available=True)

    pr = Paginator(productsList, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = pr.page(page)
    except(EmptyPage, InvalidPage):
        products = pr.page(pr.num_pages)
    return render(request, 'shop/category.html',{'Category' : catPage, 'products' : products})

def ProductCategoryDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(Category__slug = c_slug, slug = product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product': product})

def signupView(request):
    f = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if f.is_valid():
            f.save()
            username = f.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
        else:
            f = SignUpForm(request.POST)
    return render(request, 'accounts/signup.html', {'form': f})

def signinView(request):
    f = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST': 
        if f.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('shop:allProdCat')
            else:
                return redirect('signup')
    else:
        f = AuthenticationForm()
    return render(request, 'accounts/signin.html',{'form': f})

def signoutView(request):
    logout(request)
    return redirect('signin')