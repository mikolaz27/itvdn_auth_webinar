from django.urls import path
from accounts.views import  UserLoginView, UserLogoutView, UserRegistrationView
# from accounts.views import user_login, user_registration, user_logout

app_name = "accounts"

urlpatterns = [
    # path(
    #     "login/",
    #     user_login,
    #     name="user_login"
    # ),
    # path(
    #     "user-logout/",
    #     user_logout,
    #     name="user_logout"
    # ),
    # path(
    #     "user-registration/",
    #     user_registration,
    #     name="user_registration"
    # ),

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
]
