from django.urls import path

from .views import UserOwnAccountView, UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("me/", UserOwnAccountView.as_view()),
]
