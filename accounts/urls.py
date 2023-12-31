from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("profile/<str:username>", views.ProfileView.as_view(), name="profile"),
    path("profile/set/bio", views.SetBioView.as_view(), name="setbio")
]
