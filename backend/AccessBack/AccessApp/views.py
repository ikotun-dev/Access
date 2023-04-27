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

class AddTask(APIView):
    #posting - adding a new task
    def post(self, request, format=None):
        serializer = Task_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            




class Sign_up(APIView):
    def post(self, request):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success' : 'User has been created'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'failure' : 'Invalid'}, status=status.HTTP_406_NOT_ACCEPTABLE)


