from django.shortcuts import render
from rest_framework import generics
from .serializers import (
    UserSerializer,
    ProfileProgressSerializer,
)
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import (
    CustomUser,
    ProfileProgress,
)

# Create your views here.
class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
# class for ProfileProgress
class ProfileProgressListCreateView(generics.ListCreateAPIView):
    serializer_class = ProfileProgressSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ProfileProgress.objects.filter(id_user=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(id_user=self.request.user)
        else:
            print(serializer.errors)

class ProfileProgressDeleteView(generics.DestroyAPIView):
    serializer_class = ProfileProgressSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ProfileProgress.objects.filter(id_user=user)
