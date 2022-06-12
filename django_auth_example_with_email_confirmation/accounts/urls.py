from django.urls import path
from accounts.views import UserLoginView, UserLogoutView, UserRegistrationView, \
    ActivateUserView

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        UserLoginView.as_view(),
        name="user_login"
    ),
    path(
        "user-logout/",
        UserLogoutView.as_view(),
        name="user_logout"
    ),
    path(
        "user-registration/",
        UserRegistrationView.as_view(),
        name="user_registration"
    ),
    path(
        "activate/<str:uuid64>/<str:token>/",
        ActivateUserView.as_view(),
        name="activate"
    ),
]
