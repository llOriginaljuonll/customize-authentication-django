from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):

    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = False
    template_name = "accounts/login.html"