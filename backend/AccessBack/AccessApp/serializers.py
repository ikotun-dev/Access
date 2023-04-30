from .models import App_user, Task
from rest_framework import serializers

#serializer for Appusers
class User_serializer(serializers.ModelSerializer):
    class Meta :
        model = App_user
        fields = ('user_name', 'password')




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        user_id = self.context.get('user_id')
        owner = App_user.objects.get(id=user_id)
        validated_data['owner'] = owner
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner_id'] = instance.owner.id
        return representation

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        user_id = self.context.get('user_id')
        internal_value['owner'] = App_user.objects.get(id=user_id)
        return internal_value
