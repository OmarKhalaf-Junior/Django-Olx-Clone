from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('register/', views.register, name= "register"),
    path('register/confirm/', views.confirmregister, name= "confirm_register"),
    path('login/', views.userlogin, name= "login"),
    path('logout/', views.userlogout, name= "logout"),

    path('dashboard/', views.userdashboard, name= "dashboard"),
    
    path('change_password/',views.change_password,name='change_password'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/reset.html'),name='reset_password'),
    path('reset_password/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_done.html'),name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'),name='password_reset_complete'),
]