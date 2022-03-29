from rest_framework import serializers

class PriceSerializer(serializers.Serializer):
    price = serializers.IntegerField()