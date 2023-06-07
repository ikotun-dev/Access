from django.contrib import admin
from django.urls import path
from . import views 


#urlspatterns 
urlpatterns = [
    path('login/', views.Login_view.as_view()),
    path('signup/', views.Sign_up.as_view()),
    path('add-task/<int:id>/', views.AddTask.as_view()),
    path('get-tasks/<int:id>/', views.get_task.as_view()),
    path('delete-task/<int:id>', views.delete_task.as_view()),
    path('edit', views.get_task.as_view()),
    path('update/<int:id>/', views.update_task.as_view()),


]

