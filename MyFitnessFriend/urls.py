"""MyFitnessFriend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Calorie import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('pay/',views.pay,name='pay'),

    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('reset/', views.reset, name="reset"),
    path('additem/<int:id>/', views.detailfood, name="additem"),
    path('bmi/', views.bmi, name="bmi"),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('product/',views.fooditem,name='fooditem'),
    path('createfooditem/',views.createfooditem,name='createfooditem'),
    path('profile/update/<id>',views.editprofile,name='edit-profile'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form.html", success_url = reverse_lazy("password_reset_complete")), 
     name="password_reset_confirm"),  # 3
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "registration/password_reset.html", success_url = reverse_lazy("password_reset_done"), email_template_name = 'registration/forgot_password_email.html'), 
    name="reset_password"),     # 1
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), 
    name="password_reset_done"),    # 2
    
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done.html"), 
    name="password_reset_complete"),   # 4
    # change password
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
       name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html', success_url = reverse_lazy("password_change_done")), 
        name='password_change'),
]
