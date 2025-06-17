from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsWebhookSerializer

class NewsWebhookView(APIView):
    def post(self, request):
        serializer = NewsWebhookSerializer(data=request.data)
        if serializer.is_valid():
            news = serializer.save()
            return Response(
                {"message": "News created successfully", "id": news.id},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
