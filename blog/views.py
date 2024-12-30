from rest_framework.views import  APIView
from .serializers import BlogSerializer ,  CategorySerializer
from .models import Blog , Tag
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser ,BasePermission
from django.db.models import Q
from .pagination import BlogPagination
from rest_framework.filters import OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author

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
    permission_classes = [IsOwner]

    def get_object(self,  id):
        try:
            obj = Blog.objects.get(id=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except Blog.DoesNotExist:
            raise NotFound("Blog not found")
        
    def put(self, request, *args, **kwargs):
        blog = Blog.objects.get(id=kwargs['id'])
        serializer = BlogSerializer(blog, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    

class BlogDeleteView(APIView):
    permission_classes = [IsOwner | IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_object(self, id):
        try:
            obj = Blog.objects.get(id=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except Blog.DoesNotExist:
            raise NotFound("Blog not found")
        
    def delete(self, request, *args, **kwargs):
        blog = self.get_object(kwargs['id'])
        blog.delete()
        return Response(status=204)
    

class BlogFilterationView(APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category', '')
        author = request.query_params.get('author', '')
        blog = Blog.objects.filter(Q(category__name=category)|Q(author__username=author))
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=200)


class BlogListView(APIView):
    pagination_class = BlogPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['pablished_date', 'category']

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.filter(published_date__isnull=False).all()
        paginator = self.pagination_class()
        sort_by = request.query_params.get('sort', '')
        if sort_by:
            blog = blog.order_by(sort_by)
        page = paginator.paginate_queryset(blog, request, view=self)
        if page is not None:
            serializer = BlogSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data, status=200)
   
class TagDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        tag = Tag.objects.get(id=kwargs['id'])
        tag.delete()
        return Response(status=204)
    
class CategorycreateView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
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
