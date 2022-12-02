from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'autor', 'date', 'update')


class UserSeializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')