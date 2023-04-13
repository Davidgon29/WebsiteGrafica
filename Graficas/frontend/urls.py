from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('log',views.log, name="log"),
    path('charts', views.charts, name="charts")
]