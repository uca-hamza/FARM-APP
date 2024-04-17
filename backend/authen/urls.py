from django.urls import path , include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", views.UserCreateView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("create/", views.ProfileProgressListCreateView.as_view(), name="profileprogress"),
    path("delete/<int:pk>/", views.ProfileProgressDeleteView.as_view(), name="delete"),
    path("auth/", include("rest_framework.urls")),
]