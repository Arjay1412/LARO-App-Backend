from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"