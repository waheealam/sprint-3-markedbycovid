from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'address', 'city', 'state', 'zipcode', 'is_staff', 'is_active',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'address', 'city', 'state', 'zipcode', 'is_staff', 'is_active',)
