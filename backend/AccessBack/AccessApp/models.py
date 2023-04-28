from django.db import models

# Create your models here.

##the app user 
class App_user(models.Model):
    user_name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

    def __str__(self):
        return f"self.user_name"
    
##the TASK 
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=400)
    detail = models.CharField(max_length=400)
    reminder = models.BooleanField(default=False)



    