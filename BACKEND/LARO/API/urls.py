from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserCreate.as_view(), name="user-create"),
    path("users/<int:pk>/", views.UserRetrieveUpdateDestroy.as_view(), name="user-update")

]