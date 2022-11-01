from django.urls import include, path
from .views import indexPageView, createPageView, editPageView 

urlpatterns = [
    path('', indexPageView, name="index"),
    path('create/', createPageView, name="about"),
    path('edit/', editPageView , name='edit')
]
