from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework import status


class UserRegister(APIView):
    """
        User registration with api : <br>
        register user like below
            user : test <br>
            email : test@email.com <br>
            password : test <br>
            password2 : test <br>
    """

    def post(self, request):

        ser_data = UserRegisterSerializer(data=request.POST)

        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            # if user register successfully then show user data
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        
        # if user data not valid show errors
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
