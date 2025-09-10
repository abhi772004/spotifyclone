from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SignupAPI(APIView):
    def post(self, request):
        print(request.data,'11111111111')

        print(request.user)


        


        return Response({"message": "User signed up successfully!"}, status=status.HTTP_201_CREATED)
