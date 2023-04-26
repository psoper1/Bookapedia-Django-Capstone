"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from bookapedia import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('bookapedia.urls')),
    path('save-book/', views.save_book, name='save_book'),
    path('my-books/', views.BookList.as_view({'get': 'list'}), name='my_books'),
    path('my-books/', views.BookList.as_view({'get': 'read'}), name='read-books'),
    path('read-books/', views.Read.as_view({'get': 'list'}), name='read'),
    path('unread-books/', views.Unread.as_view({'get': 'list'}), name='unread'),
    
]
