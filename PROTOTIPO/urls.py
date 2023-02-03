from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name="home"),
    path('sistema/', views.sistema, name="sistema"),
]
