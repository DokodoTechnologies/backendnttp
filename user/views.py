from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Custom permission (assuming you created it)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        if self.request.user.role == 'ADMIN':
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    @action(detail=False, methods=['post'])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully!", "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({
            "error": "Invalid data format"
        }, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if not user.is_active:
                    return Response({'error': 'Account is inactive'}, status=status.HTTP_403_FORBIDDEN)

                refresh = RefreshToken.for_user(user)
                refresh['role'] = user.role if hasattr(user, 'role') else None

                return Response({
                    'message': 'Logged In Successfully',
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'role': user.role if hasattr(user, 'role') else None,
                    'username': user.username,
                    'id': user.id
                }, status=status.HTTP_200_OK)

            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
