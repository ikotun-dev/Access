from django.contrib import admin
from django.urls import path
from . import views 


#urlspatterns 
urlpatterns = [
    path('login/', views.Login_view.as_view()),
    path('signup/', views.Sign_up.as_view()),
    path('add-task/', views.AddTask.as_view()),
    path('get-tasks/', views.get_task.as_view()),
    path('delete-task/<int:id>', views.delete_task.as_view()),

]

