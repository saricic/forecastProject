from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Explicitly set widget id attributes so labels reference valid ids
        self.fields['username'].widget.attrs.update({'id': 'id_username'})
        self.fields['password1'].widget.attrs.update({'id': 'id_password1'})
        self.fields['password2'].widget.attrs.update({'id': 'id_password2'})

        # Override the default help texts
        self.fields['username'].help_text = "Your username can only include letters and numbers."
        self.fields[
            'password1'].help_text = "Your password must be at least 8 characters long and not entirely numeric."
        self.fields['password2'].help_text = "Please enter the same password as above."

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
