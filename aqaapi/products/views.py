import copy
import json

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication

# from .models import Product
# from .serializers import ProductSerializer
# from .pagination import ProductPageNumberPagination

class HomeView(APIView):
    
    def get(self, request):
        return Response({"nice": "nice"}, status=status.HTTP_200_OK)