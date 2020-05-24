from django.shortcuts import render,redirect
from categories.models import Category
from sub_categories.models import SubCategory
from .models import Entertainment
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def subcategories(request,pk):
    query_set = SubCategory.objects.all().filter(category=pk)
    try:
        cat = query_set[0].category
    except:
        cat = "None"
    context = {
        'categories': query_set,
        'category':cat
    }
    return render(request, 'pages/subcategories.html',context)

def seasons(request,pk):
    query_set = SubCategory.objects.all().filter(id=pk)
    
    try:
        sub = query_set[0].category
    except:
        sub = "None"
    try:
        title = query_set[0].title
    except:
        title = "None"
    for i in query_set:
            l = [x+1 for x in range(i.seasons)]
    # l = [i for i in range(query_set.seasons)]
    context = {
        'categories': query_set,
        'list': l,
        'sub': sub,
        'category': title
    }
    return render(request, 'pages/seasons.html',context)

def listview(request,pk):
    query_set = Entertainment.objects.all().filter(season=pk)
    if 'subcategory' in request.GET:
        subcategory = request.GET['subcategory']
        if subcategory:
            query_set = query_set.filter(category=subcategory)
            try:
                sub = query_set[0].category.category
            except:
                sub = "None"
            try:
                sub1 = query_set[0].category
            except:
                sub1 = "None"
    context = {
        'posts': query_set,
        'sub': sub,
        'category': 'Episodes',
        'sub1': sub1
    }
    return render(request, 'pages/listview.html',context)

@login_required
def detail(request,pk):
    query_set = Entertainment.objects.all().filter(id=pk)
    context = {
        'posts': query_set,
    }
    return render(request, 'pages/detail.html',context)

def index(request):
    category = Category.objects.all()
    return render(request, 'pages/index.html',{'categories':category})

def user_login(request):
    user = User
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return render(request, 'pages/login.html')
