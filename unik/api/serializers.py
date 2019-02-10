from rest_framework import serializers
from .models import Quiz


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'date',)
        model = Quiz