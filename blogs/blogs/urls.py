from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('blog.urls'), name="home"),
    path('register/', views.Register.as_view(),name="register"),
]
