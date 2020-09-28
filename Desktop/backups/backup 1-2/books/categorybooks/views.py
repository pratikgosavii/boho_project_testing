from django.shortcuts import render
from home.models import books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.



def categorybooks(request, name):

    if name == 'trending':
        request.session['name']= name
        name=request.session['name']
        posts = books.objects.filter(trending = True)

    elif name == 'bestselling':
        request.session['name']= name
        name=request.session['name']
        posts = books.objects.filter(bestseller = True)

    elif name == all:
        posts = books.objects.all()

    else:
        request.session['name']= name
        name=request.session['name']
        posts = books.objects.filter(category = name)

    paginator = Paginator(posts, 9)

    page = request.GET.get('page')

    request.session['name']= name
    name=request.session['name']

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})
