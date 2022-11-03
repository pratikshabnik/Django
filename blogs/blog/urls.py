from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.home),
   path('home/',views.home, name ="home"),
   path('posts/<id>',views.posts, name="posts"),
   path('profile/<id>', views.profile, name="profile"),
   path('createprofile/', views.createprofile,name= "createprofile"),
   path('profile_form/', views.profile_form, name="profile_form"),
   path('createblog/', views.createblog,name= "createblog"),
   path('editprofile/<id>', views.editprofile, name='editprofile'),
   path('updateprofile/<id>', views.updateprofile, name='updateprofile'),
   path('myblog/<id>', views.myblog, name='myblog'),
   path('editblog/<id>', views.editblog, name='editblog'),
   path('updateblog/<id>', views.updateblog, name='updateblog'),
]
