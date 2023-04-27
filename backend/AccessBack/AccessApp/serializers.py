from .models import App_user, Task
from rest_framework import serializers

#serializer for Appusers
class User_serializer(serializers.ModelSerializer):
    class Meta :
        model = App_user
        fields = ('user_name', 'password')


#serializer for Task
class Task_serializer(serializers.ModelSerializer):
    class Meta :
        model = Task
        fields = ('description', 'detail', 'reminder')
        