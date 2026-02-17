from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Users registered Sucessfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=400)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serialzer = LoginSerializer(data = request.data)
        serialzer.is_valid(raise_exception=True)
        data = serialzer.validated_data

        return Response({
             "user":{
                "id":data['user'].id,
                'name':data['user'].name,
                'email':data['user'].email,
            },
            'refresh': data['refresh'],
            'access': data['access']

        }, status=status.HTTP_200_OK)
    


