from .models import App_user, Task
from rest_framework import serializers

#serializer for Appusers
class User_serializer(serializers.ModelSerializer):
    class Meta :
        model = App_user
        fields = ('user_name', 'password')


class Task_serializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(source='owner', queryset=App_user.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'owner_id', 'description', 'detail', 'date', 'reminder')