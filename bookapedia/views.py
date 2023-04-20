from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Book
from .serializers import *
from django.shortcuts import get_object_or_404

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

@api_view(['POST'])
def save_book(request):
    serializer = BookSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        book = serializer.save()
        book.saved_by = request.user
        print("In if statement")
        print(request.user)
        book.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class BookList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        user = self.request.user
        if user.is_authenticated:
            queryset = Book.objects.filter(saved_by=user)
        else:
            queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class Read(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        user = self.request.user
        if user.is_authenticated:
            queryset = Book.objects.filter(marked_read=True, saved_by=self.request.user)
        else:
            queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class Unread(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        user = self.request.user
        if user.is_authenticated:
            queryset = Book.objects.filter(marked_read=False, saved_by=self.request.user)
        else:
            queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)