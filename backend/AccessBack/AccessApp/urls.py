from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    
    path('login/', views.Login_view.as_view()),
    path('signup/', views.Sign_up.as_view()),
    path('add-task/', views.AddTask.as_view()),


]
