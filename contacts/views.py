from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Inquiry
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def inquiries(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        
        owner_id = request.POST['owner_id']
        owner_mail = request.POST['owner_mail']
        
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        
        phone = request.POST['phone']
        message = request.POST['message']
        
        if request.user.is_authenticated():
            user_id= request.user.id
            has_inquiried= Inquiry.objects.all().filter(listing_id= listing_id, user_id= user_id)
            if has_inquiried:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('index')

            make_inquiry= Inquiry(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id, owner_id=owner_id)
            make_inquiry.save()
            send_mail(
                'Inquiry for '+ listing,
                'There has been an inquiry for '+ listing +'.Sign in to your dashboard for further info',
                settings.EMAIL_HOST_USER,
                [owner_mail],
                fail_silently=False,
            )
            messages.success(request, "your inquiry has been made, the owner of the post will get back to you asap")
            return redirect('index')