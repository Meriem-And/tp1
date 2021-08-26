from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path("response.html", views.test),

]
