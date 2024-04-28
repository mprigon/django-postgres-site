from django.contrib.auth.forms import UserChangeForm
from core.models import User

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'skills', 'mobile_phone']
