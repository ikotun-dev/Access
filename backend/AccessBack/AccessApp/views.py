from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Task, App_user
from .serializers import Task_serializer, User_serializer
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
            if users:
                refresh = RefreshToken.for_user(users)
                access_token = refresh.access_token
                response = {
                    'success' : 'Login Worked',
                    'refresh' : str(refresh),
                    'access' : str(access_token)
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({'Failure': 'didnt work'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:

            return Response({'Invalid data inputed'}, status=status.HTTP_400_BAD_REQUEST)

#View for adding task througth the API 
class AddTask(APIView):
    #posting - adding a new task
    def post(self, request, format=None):
        serializer = Task_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            print("TASK ADDED SUCCESSFULLY")
            return Response({'success'  : 'task added successfully'}, status=status.HTTP_201_CREATED)

        else :
            return Response({'Failure'  : 'task couldnt be added '}, status=status.HTTP_406_NOT_ACCEPTABLE)



#view for getting tasks 
class get_task(APIView):

    #getter for getting the tasks :
    def get(self, request):
        all_tasks = Task.objects.all()
        serializer = Task_serializer(all_tasks, many=True)

        print("Get tasks successful")
        return Response(serializer.data, status=status.HTTP_200_OK)

#view for deleteing task
class delete_task(APIView):
    #deleter for deleting the task 
    def delete(self, request, id):
        #task to delete
        task_to_delete = Task.objects.get(id=id)
        task_to_delete.delete()

        return Response({'info' : 'Task has been deleted'}, status=status.HTTP_200_OK)


class Sign_up(APIView):
    def post(self, request):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success' : 'User has been created'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'failure' : 'Invalid'}, status=status.HTTP_406_NOT_ACCEPTABLE)


