from .models import App_user, Task
from rest_framework import serializers

#serializer for Appusers
class User_serializer(serializers.ModelSerializer):
    class Meta :
        model = App_user
        fields = ('user_name', 'password')


#serializer for Task
class Task_serializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(source='owner', queryset=App_user.objects.all())

    class Meta :
        model = Task
        fields = ('id', 'description', 'owner_id', 'detail', 'reminder')

class Task_send_serializer(serializers.ModelSerializer):
    class Meta :
        model = Task
        fields = ('id', 'description', 'detail', 'reminder')
