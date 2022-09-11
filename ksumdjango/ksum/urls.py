from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_or_create, name='login'),
    path('umbrella_borrow/<int:Snum>', views.umbrella_borrow, name='umbrella_borrow'),
    path('umbrella_return/<int:Snum>', views.umbrella_return, name = 'umbrella_return'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)