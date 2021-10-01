from django.shortcuts import render
from listing.models import Listing

# Create your views here.
def index(request):
    query_set= Listing.objects.order_by('-list_date')[0:6]

    if 'description' in request.GET:
        description= request.GET['description']
        if description:
            query_set= query_set.filter(description__icontains= description)

    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            query_set= query_set.filter(city__iexact= city)

    if 'title' in request.GET:
        title= request.GET['title']
        if title:
            query_set= query_set.filter(title__icontains= title)

    if 'category' in request.GET:
        category= request.GET['category']
        if category:
            query_set= query_set.filter(category__icontains= category)


    context= {
        'listings': query_set,
    }
    return render(request, 'pages/index.html', context= context)

def about(request):
    return render(request, 'pages/about.html', context= None)