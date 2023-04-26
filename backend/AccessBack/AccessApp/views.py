from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Task, App_user
from .serializers import Task_serializer, User_serializer
from rest_framework_simplejwt.tokens import RefreshToken


a_user = App_user.objects.all()

# Create your views here.
class Login_view(APIView):
    #FOR GET REQUEST 
    def post(self, request, format=None):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            try : 
                i_username = serializer.validated_data['user_name']
                i_password = serializer.validated_data['password']

                users = App_user.objects.get(user_name=i_username, password=i_password)
                if users : 
                    return Response({'success' : 'Login worked'}, status=status.HTTP_200_OK)
                else :
                    return Response({'Failure' : 'didnt work'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


            except Exception:
                return Response({'Failure' : 'login failed'}, status=status.HTTP_401_UNAUTHORIZED)
    
        else :
            return Response({'Invalid data inputed'}, status=status.HTTP_400_BAD_REQUEST)
            
class Sign_up(APIView):
    def post(self, request):
        serializer = User_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success' : 'User has been created'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'failure' : 'Invalid'}, status=status.HTTP_406_NOT_ACCEPTABLE)


