
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tags
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Story
        fields = ["name","description","created_date"]

class PostimageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostImage
        fields = "__all__"
    

class PoststatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostStatus
        fields = "__all__"

