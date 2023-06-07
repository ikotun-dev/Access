from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Task, App_user
from .serializers import TaskSerializer, User_serializer
from rest_framework_simplejwt.tokens import RefreshToken


a_user = App_user.objects.all()

class Login_view(APIView):
    #FOR GET REQUEST 
    def post(self, request, format=None):

        serializer = User_serializer(data=request.data)

        if serializer.is_valid():
            i_username = serializer.validated_data['user_name']
            i_password = serializer.validated_data['password']

            users = App_user.objects.get(user_name=i_username, password=i_password)
            #if statement
            if users:
                refresh = RefreshToken.for_user(users)
                access_token = refresh.access_token
                print(users.id)
                response = {
                    'success' : 'Login Worked',
                    'refresh' : str(refresh),
                    'access' : str(access_token),
                    'user' : i_username,
                    'user_id': users.id,
                    'user_last_task' : get_last_task(users.id),

                }
                return Response(response, status=status.HTTP_200_OK)
            #else statement 
            else:
                return Response({'Failure': 'didnt work'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        else:
            return Response({'Invalid data inputed'}, status=status.HTTP_400_BAD_REQUEST)


class AddTask(APIView):
    """
    View to add a new Task object.
    """
   # def post(self, request, id, format=None):
    def post(self, request, id, format=None):
        serializer = TaskSerializer(data=request.data, context={'user_id': id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#view for getting tasks 
class get_task(APIView):

    def get(self, request, id, format=None):
        tasks = Task.objects.filter(owner=id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


#function to get the latest task 
def get_last_task(id):
    try:
        task = Task.objects.filter(owner__id=id)
        tasky = task.latest('id')
   
        return tasky.description

    except Task.DoesNotExist:
        return None


#view for deleteing task
class delete_task(APIView):
    #deleter for deleting the task 
    def delete(self, request, id):
        #task to delete
        task_to_delete = Task.objects.get(id=id)
        task_to_delete.delete()

        return Response({'info' : 'Task has been deleted'}, status=status.HTTP_200_OK)


#update a task
class update_task(APIView):
    def put(self, request, id) :
    
        try:
            task_to_update = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task_to_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Sign_up(APIView):
    def post(self, request):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success' : 'User has been created'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'failure' : 'Invalid'}, status=status.HTTP_406_NOT_ACCEPTABLE)


