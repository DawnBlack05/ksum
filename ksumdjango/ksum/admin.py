from django.contrib import admin

# Register your models here.
from .models import User, borrow
admin.site.register(User)
admin.site.register(borrow)