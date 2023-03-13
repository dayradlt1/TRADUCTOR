from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('carga/',views.upload_view,name='carga'),
    path("video/<int:l_s>",views.video_loader,name="video"),
	path("mask/<int:l_s>",views.mask_loader,name="mask"),
	path("sistema/",views.video_feed,name="sistema"),
]
