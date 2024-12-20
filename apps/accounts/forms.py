from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'input-primary',
        })
        self.fields['username'].label = 'Your username'
        self.fields['password'].label = 'Your password'
        self.fields['username'].label_suffix = False
        self.fields['password'].widget.attrs.update({
            'class': 'input-primary',
        })

class CustomUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'input-primary',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'input-primary',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input-primary',
        })
        self.fields['username'].label_suffix = False