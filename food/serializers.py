from rest_framework import serializers


class FoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    color = serializers.CharField(max_length=30)
    value = serializers.IntegerField()
    