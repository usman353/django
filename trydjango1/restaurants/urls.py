from django.urls import path
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from .views import (
    RestaurantListView, RestaurantCreateView, RestaurantDetailView, TemplateView

)
app_name='restaurants'

urlpatterns = [
    path('', RestaurantListView.as_view(), name='list'),
    path('create/', RestaurantCreateView.as_view(), name='create'),
    path('<slug>/', RestaurantDetailView.as_view(), name='detail'),

]
