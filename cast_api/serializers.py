from rest_framework import serializers
from .models import Cast
class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ('id', 'name', 'age', 'first_episode', 'status', 'relationship_status', 'image_link')