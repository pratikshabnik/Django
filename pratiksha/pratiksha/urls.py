from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(),name="register")

]
