from dataclasses import fields
from rest_framework import serializers
from .models import PostTest


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostTest
        fields='__all__'