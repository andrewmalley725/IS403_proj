from django.urls import include, path
from .views import indexPageView, createPageView, editPageView, deletePageView, submitChanges

urlpatterns = [
    path('', indexPageView, name="index"),
    path('create/', createPageView, name="about"),
    path('edit/<int:sid>', editPageView , name='edit'),
    path('submitchanges/<int:sid>', submitChanges, name='submit'),
    path('delete/<int:sid>', deletePageView, name='delete')
    
]
