"""trydjango1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from restaurants.views import restaurant_listview, TemplateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from restaurants.views import (
    restaurant_listview,
    RestaurantListView, RestaurantCreateView, RestaurantDetailView, restaurant_createview

)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'),name='home'),
    path('restaurants/', include('restaurants.urls',namespace='restaurants')),# this include allows for url file in apps
    path('login/', LoginView.as_view(), name='login'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetDoneView.as_view(), name='password_reset_complete'),
    # path('restaurants/', RestaurantListView.as_view(),name='restaurants'),
    # path('restaurants/create/', RestaurantCreateView.as_view(),name='restaurants-create'),
    # path('restaurants/<slug>', RestaurantListView.as_view()),
    # path('restaurants/<slug>/', RestaurantDetailView.as_view(),name='restaurant_detail'),
    path('about/', TemplateView.as_view(template_name='About.html'),name='about'),
    path('contact/', TemplateView.as_view(template_name='Contact.html'),name='contact'),
]
