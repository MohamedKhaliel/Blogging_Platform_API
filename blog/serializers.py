from rest_framework import serializers
from .models import Blog , Category , Tag 
from django.utils.timezone import now 

class TagSerializer(serializers.ListField):
    class Meta:
        model = Tag
        fields = ['name']

    def create(self, validated_data):
        tag = Tag.objects.create(**validated_data)
        return tag
    
    def create(self, validated_data):
        instance = self.Meta.model
        tag = instance.objects.create(**validated_data)
        return tag
    
    def to_representation(self, data):
         return data.values_list('name', flat=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category
    
class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(required=False)
    publish_now = serializers.BooleanField(default=False, write_only=True, required=False) 
    published_date = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'tags' , 'category' , 'published_date', 'publish_now']

    def get_published_date(self, obj):
        if obj.published_date:
            return obj.published_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
             return None
    
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])if "tags" in validated_data else []
        published_now= validated_data.pop('publish_now', False)

        if published_now:
            validated_data['published_date'] = now()
        else:
            validated_data['published_date'] = None 

        blog = self.Meta.model.objects.create(**validated_data)

        if tags:
            tag_names = []
            for name in tags:
                tag, _ = Tag.objects.get_or_create(name=name)
                tag_names.append(tag)
                
            blog.tags.set(tag_names)

        return blog

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', []) if "tags" in validated_data else []
        published_now= validated_data.pop('publish_now', False)

        if published_now:
            validated_data['published_date'] = now()
        else:
            validated_data['published_date'] = None 

        blog = super().update(instance, validated_data)
        
        if tags:
            tag_names = []
            for name in tags:
                tag, _ = Tag.objects.get_or_create(name=name)
                tag_names.append(tag)
                
            blog.tags.set(tag_names)

        return blog
                
    def to_representation(self, instance):
        # Override to_representation to display tag names instead of IDs
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data if instance.category else None
        return representation
        
