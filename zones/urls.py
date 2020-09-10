from django.urls import path
from . import views

urlpatterns = [
    path('api/zone/', views.ZoneListCreate.as_view() ),
]
