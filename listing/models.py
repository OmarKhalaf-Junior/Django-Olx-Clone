from django.db import models
from core.models import User
from datetime import datetime

# Create your models here.
class Listing(models.Model):
    owner= models.ForeignKey(User, on_delete= models.CASCADE)
    title= models.CharField(max_length= 100)
    category= models.CharField(max_length= 100)
    address= models.CharField(max_length= 100)
    city= models.CharField(max_length= 100)
    state= models.CharField(max_length= 100)
    zipcode= models.CharField(max_length= 100)
    description= models.TextField()
    price= models.IntegerField()
    main_photo= models.ImageField(upload_to= 'listing/%Y/%m/%d/')
    photo_1= models.ImageField(upload_to= 'listing/%Y/%m/%d/', null= True, blank= True)
    photo_2= models.ImageField(upload_to= 'listing/%Y/%m/%d/', null= True, blank= True)
    photo_3= models.ImageField(upload_to= 'listing/%Y/%m/%d/', null= True, blank= True)
    photo_4= models.ImageField(upload_to= 'listing/%Y/%m/%d/', null= True, blank= True)
    photo_5= models.ImageField(upload_to= 'listing/%Y/%m/%d/', null= True, blank= True)
    photo_6= models.ImageField(upload_to= 'listing/%Y/%m/%d/', null= True, blank= True)
    favourites= models.ManyToManyField(User, blank= True, related_name= "favourites")
    is_published= models.BooleanField(default= True)
    list_date= models.DateTimeField(default= datetime.now)


    def __str__(self):
        return self.title