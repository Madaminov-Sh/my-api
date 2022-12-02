from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers, UserSeializers
from django.contrib.auth import get_user_model
# from .permissions import IsAuthorOrRead
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSeializers