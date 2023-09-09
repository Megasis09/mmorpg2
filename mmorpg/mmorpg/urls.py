from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_ads, name='view_ads'),
    path('<int:ad_id>/', views.view_ad, name='view_ad'),
    path('<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),
    path('create/', views.create_ad, name='create_ad'),
    path('responses/', views.view_responses, name='view_responses'),
]
