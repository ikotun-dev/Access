from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Task, App_user
from .serializers import Task_serializer, User_serializer




# Create your views here.
class Login_view(APIView):
    #FOR GET REQUEST 
    def get(request):
        pass

    #FOR POST REQUEST
    def post(request):
        pass

    