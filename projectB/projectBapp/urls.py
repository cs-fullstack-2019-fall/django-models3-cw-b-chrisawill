from django.urls import path

from . import views

urlpatterns = [
    path('', views.library, name='index'),
    path('library/all/', views.allbooks),
    path('librarry/add/', views.fictionbooks),

]