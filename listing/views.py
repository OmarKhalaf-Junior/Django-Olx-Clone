from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from django.core.paginator import Paginator
from .forms import CreateListingForm, UpdateListingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def listings(request):
    listings= Listing.objects.order_by('-list_date').filter(is_published= True)
    paginator= Paginator(listings, 1)
    page= request.GET.get('page')
    page_listings= paginator.get_page(page)

    context= {
        'listings': page_listings,
    }
    return render(request, 'listing/listings.html', context= context)

def listing(request, pk):
    listing= get_object_or_404(Listing, pk=pk)
    is_favourite= False
    if request.method == 'POST':
        if Listing.objects.filter(pk= pk, favourites= request.user).exists():
            is_favourite= True
            listing.favourites.remove(request.user)
        else:
            is_favourite= False
            listing.favourites.add(request.user) 
    
    context= {
        'listing': listing,
        'is_favourite': is_favourite,
    }
    return render(request, 'listing/listing.html', context= context)


def search(request):
    query_set= Listing.objects.order_by('-list_date')


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
        'query_set': query_set,
    }
    return render(request, 'listing/search.html', context)


@login_required
def create_listing(request):
    if request.method == 'POST':
        form= CreateListingForm(request.POST, request.FILES)
        if form.is_valid():
            myform= form.save(commit= False)
            myform.owner= request.user
            myform.save()
            return redirect('index')

    else:
        form= CreateListingForm()

    context= {
        'form': form,    
    }
    return render(request, 'listing/create.html', context= context)


def update_listing(request, pk):
    listing= get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        form= UpdateListingForm(request.POST, request.FILES, instance= listing)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form= UpdateListingForm(instance= listing)
    context= {
        'form': form,
    }
    return render(request, 'listing/update.html', context= context)


def delete_listing(request, pk):
    listing= get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('index')

    context= {
        'listing': listing,    
    }

    return render(request, 'listing/delete.html', context)