from django.urls import path
from apps.message import views

urlpatterns = [
    path('show',views.getform),
    path('update',views.update)
]