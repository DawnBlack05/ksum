from dataclasses import field
from django.forms import ModelForm
from .models import User, borrow

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class BorrowForm(ModelForm):
    class Meta:
        model = borrow
        fields = "__all__"