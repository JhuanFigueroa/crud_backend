from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView, View



from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView)


from .models import User

from .serializers import UserSerializer

# Create your views here.


class InicioView(TemplateView):
    template_name = "index.html"


class getUsers(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class detailUser(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset=User.objects.all()
    


class createUser(CreateAPIView):
    serializer_class = UserSerializer


class updateUser(RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class deleteUser(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

#subir imagen

