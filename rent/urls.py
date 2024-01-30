

from django.urls import path
from .views import *


urlpatterns = [
    path("", registerpage),
    path("register/", registerdata, name="registerData")
]
