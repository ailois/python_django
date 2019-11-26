from django.urls import path
from apps.oneToone import views

urlpatterns = [
    path('show',views.getUser),
    path('update',views.update),
    path('insert',views.insert),
]