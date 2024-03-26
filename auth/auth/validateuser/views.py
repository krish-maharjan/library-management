from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from knox.auth import TokenAuthentication

class ValidateTokenAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # If the request reaches this point, the token is valid
        # and the user is authenticated
        return JsonResponse({"valid": True, "user": str(request.user)}, status=200)
