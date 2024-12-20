from django.shortcuts import render
from rest_framework.views import  APIView
from .serializers import BlogSerializer , TagSerializer , Categoryserializer
from .models import Blog 
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Q

# Create your views here.
class BlogCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class BlogDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=200)
    
class BlogUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        serializer = BlogSerializer(blog, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    

class BlogDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        blog.delete()
        return Response(status=204)
    
class TagcreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class CategorycreateView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        serializer = Categoryserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query_key', '')
        blog = Blog.objects.filter(Q(title__icontains=query)|Q(content__icontains=query)|Q(author__username__icontains=query)|Q(tags__name__icontains=query))
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=200)   

class BlogfilterationView(APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category', '')
        author = request.query_params.get('author', '')
        blog = Blog.objects.filter(Category__name=category, author__username=author)
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=200)