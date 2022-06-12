from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserRegistrationForm


# # Example 2, how to handle password
# def user_logout(request):
#     logout(request)
#     return redirect('index')
#
#
# def user_login(request):
#     return redirect('index')
#
#
# def user_registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             email = form.cleaned_data.get('email')
#             user = User.objects.create(
#                 username=username,
#                 # password=raw_password,
#                 email=email,
#             )
#             user.set_password(raw_password=raw_password)
#             user.save()
#             print(raw_password)
#             # user = authenticate(username=username, password=raw_password)
#             # login(request, user)
#             return redirect('index')
#     else:
#         form = UserRegistrationForm()
#     return render(request, "registration/registration.html", {'form': form})

# Example 2, django solution
class UserLoginView(LoginView):
    def get_default_redirect_url(self):
        return reverse("index")

#
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:user_login')


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")
