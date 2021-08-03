from rest_framework import viewsets
from calculator.models import Post
from calculator.serializer import CalculatorSerializer
from django.http import JsonResponse

class CalculatorViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CalculatorSerializer
