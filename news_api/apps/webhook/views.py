from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsWebhookSerializer

class NewsWebhookView(APIView):
    def post(self, request):
        serializer = NewsWebhookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "News queued for processing"},
                status=status.HTTP_202_ACCEPTED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)