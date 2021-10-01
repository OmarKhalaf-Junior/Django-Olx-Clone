from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('You Have To Add A Valid Username')

        email= self.normalize_email(email)
        user= self.model(username= username, email= email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, username, password, email= None):
        user= self.create_user(username, email, password)
        user.is_staff= True
        user.is_superuser= True
        user.save()
        
        return user



class User(AbstractBaseUser, PermissionsMixin):
    username= models.CharField(max_length= 50, unique= True)
    email= models.EmailField(max_length= 255, unique= True)
    first_name= models.CharField(max_length= 50)
    last_name= models.CharField(max_length= 50)
    phone= models.CharField(max_length= 13, unique= True)
    # favourites = models.CharField(max_length=200,default='')
    is_active= models.BooleanField(default= True)
    is_staff= models.BooleanField(default= False)

    objects= UserManager()
    USERNAME_FIELD= 'username'
