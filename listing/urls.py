from django.urls import path
from . import views

urlpatterns= [
    path('', views.listings, name= "listings"),
    path('<int:pk>/', views.listing, name= "listing"),
    path('search/', views.search, name= "search"),

    path('create/', views.create_listing, name= "create"),
    path('<int:pk>/update/', views.update_listing, name= "update"),
    path('<int:pk>/delete/', views.delete_listing, name= "delete"),
        
]