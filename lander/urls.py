from django.urls import path

from .views import LanderView

urlpatterns = [
    path('', LanderView.as_view(), name='lander'),
]