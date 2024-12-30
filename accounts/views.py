from rest_framework.views import  APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer , UserSerializer
from .models import CustomUser
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAdminUser , IsAuthenticated 
from django.contrib.auth import logout
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args,**kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return  Response(serializer.errors, status=400)


class UserLoginView(APIView):
    permission_classes =[AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
        

class UserListView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data, status=200)
    
class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get_object(self, user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise NotFound("User not found")
        
    def put(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):

        # delete user's auth_token
        request.user.auth_token.delete()

        # update user's is_active status
        user = request.user
        user.save()

        # log out user
        logout(request)

        return Response({"detail": "Successfully logged out."}, status=200)