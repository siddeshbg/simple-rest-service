from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import HistorySerializer
from .models import History
from .utils import vowel_count


class VowelCountView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to Vowel Count API service!"})

    def post(self, request):
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.data['length'] = len(serializer.data.get("word"))
            serializer.data['vowels'] = vowel_count(serializer.data.get("word"))
            history_instance = History.objects.create(**serializer.data)
            return Response({
                                "word": serializer.data.get("word"),
                                "vowels": vowel_count(serializer.data.get("word"))
            })
        else:
            return Response({"error": serializer.errors})


class HistoryViewSet(ModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()