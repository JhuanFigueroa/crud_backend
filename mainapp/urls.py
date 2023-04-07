from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name='mainapp_app'
urlpatterns = [
    path('',views.InicioView.as_view(),name='inicio'),
    path('api/users',views.getUsers().as_view()),
    path('api/users/detail/<pk>',views.detailUser().as_view()),
    path('api/users/create',views.createUser().as_view()),
    path('api/users/update/<pk>',views.updateUser().as_view()),
    path('api/users/delete/<pk>',views.deleteUser().as_view()),
  
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)