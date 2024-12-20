from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

class CustomLoginView(LoginView):

    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = False
    template_name = "accounts/login.html"

    def dispatch(self, request, *args, **kwargs):
        """
        ถ้า user ทำการ login อยู่ ให้ทำการ redirect ไปที่หน้า homepage
        """
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class CustomUserCreationView(CreateView):

    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("home")