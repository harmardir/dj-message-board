from django.urls import path
from .views import HomePafeView

urlpatterns = [
    path('',HomePafeView.as_view(), name='home'),
]