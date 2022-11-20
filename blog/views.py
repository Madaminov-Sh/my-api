from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
# from .permissions import IsAuthorOrRead
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

class PostAPIListView(ListCreateAPIView):
    # permission_classes = (IsAuthorOrRead,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostAPCreateView(RetrieveUpdateAPIView):
    # permission_classes = (IsAuthorOrRead,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers