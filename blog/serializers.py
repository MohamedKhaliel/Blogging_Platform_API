from rest_framework import serializers
from .models import Blog

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']

        def create(self, validated_data):
            blog = Blog.objects.create(**validated_data)
            return blog
        
      