from rest_framework import serializers
from .models import Blog , Category , Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name' , 'blog']

    def create(self, validated_data):
        tag = Tag.objects.create(**validated_data)
        return tag

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True ,required=False)
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'tags']

        def create(self, validated_data):
            blog = Blog.objects.create(**validated_data)
            return blog
        
class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category
    
