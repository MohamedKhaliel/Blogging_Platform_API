from rest_framework import serializers
from .models import Blog , Category , Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

    def create(self, validated_data):
        tag = Tag.objects.create(**validated_data)
        return tag

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category
    
class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True ,queryset=Tag.objects.all())
    category = Categoryserializer(required=False)
    class Meta:

        model = Blog
        fields = ['title', 'content', 'author', 'tags' , 'category']

        def create(self, validated_data):
            tags = validated_data.pop('tags', [])
            blog = self.Meta.model.objects.create(**validated_data)
            for tag in tags:
                blog.tags.add(tag.id)
            return blog