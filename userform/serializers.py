from rest_framework import serializers
from .models import Sector, Input

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class InputSerializer(serializers.ModelSerializer):
    sectors = SectorSerializer(many=True, read_only=True)
    class Meta:
        model = Input
        fields = ['id', 'username', 'sectors', 'date', 'month', 'year']