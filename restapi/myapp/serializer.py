from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
        # fields = ['username','email']
        # exclude = ['email']

    def validate(self, attrs):
        
        if attrs['age'] <18:
            raise serializers.ValidationError("Age must be greater than 18")

        return attrs
    
class AuthorSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1
    
    def to_representation(self, instance):
        resp =  super().to_representation(instance)
        resp['author'] = AuthorSeralizer(instance.author).data
        return resp