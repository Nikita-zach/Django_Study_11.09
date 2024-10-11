from django.urls import path
from manager.models import user_reservation

app_name = 'manager'
urlpatterns = [
    path("user_reservation/", user_reservation, name="user_reservation"),
]