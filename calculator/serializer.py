from calculator.models import Post
from rest_framework import serializers

class CalculatorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post 
        fields = ['firstNumber', 'secondNumber']