from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widget'lara özel CSS sınıfları ekleme
        self.fields['username'].widget.attrs.update({'id': 'id_username', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'id': 'id_password1', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'id': 'id_password2', 'class': 'form-control'})

        # Help text'leri özelleştirme
        self.fields['username'].help_text = "Your username can only include letters and numbers."
        self.fields[
            'password1'].help_text = "Your password must be at least 8 characters long and not entirely numeric."
        self.fields['password2'].help_text = "Enter the password again."

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
