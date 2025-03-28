from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_obituary, name='submit_obituary'),
    path('', views.view_obituaries, name='view_obituaries'),
    path('<slug:slug>/', views.obituary_detail, name='obituary_detail'),
]