from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, RedirectView

from accounts.forms import UserRegistrationForm
from accounts.services.emails import send_registration_email

from accounts.utils.token_generators import TokenGenerator


class UserLoginView(LoginView):
    def get_default_redirect_url(self):
        return reverse("index")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:user_login')


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        # send email or sms notification
        send_registration_email(
            request=self.request,
            user_instance=self.object
        )
        return super().form_valid(form)


class ActivateUserView(RedirectView):
    url = reverse_lazy('index')

    def get(self, request, uuid64, token, *args, **kwargs):
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            current_user = get_user_model().objects.get(pk=pk)
        except (get_user_model().DoesNotExist, TypeError, ValueError):
            return HttpResponse("Wrong data")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()

            login(request, current_user)
            return super().get(request, *args, **kwargs)

        return HttpResponse("Wrong data")
