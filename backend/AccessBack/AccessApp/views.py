from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Task, App_user
from .serializers import Task_serializer, User_serializer, Task_send_serializer
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
                    'user_last_task' : get_last_task(),

                }
                return Response(response, status=status.HTTP_200_OK)
            #else statement 
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

    def get(self, request, id):
        # Get the App_user object with the given id
        # try:
        #     app_user = App_user.objects.get(pk=id)
        # except App_user.DoesNotExist:
        #     return Response({"message": f"User with id {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Filter tasks by the owner field
        tasks = Task.objects.filter(owner__id=id)
        
        # Serialize the filtered tasks
        serializer = Task_send_serializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#function to get the latest task 
def get_last_task():
    try:
        task = Task.objects.latest('id')
   
        return task.description
        
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


class Sign_up(APIView):
    def post(self, request):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success' : 'User has been created'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'failure' : 'Invalid'}, status=status.HTTP_406_NOT_ACCEPTABLE)


