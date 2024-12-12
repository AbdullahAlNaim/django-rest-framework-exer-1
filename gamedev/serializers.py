from rest_framework import serializers
from .models import IndieGame

class IndieGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndieGame
        fields = '__all__'