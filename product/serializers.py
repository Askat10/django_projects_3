from rest_framework import serializers

class CitiesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    square = serializers.DecimalField(max_digits=7, decimal_places=2)
    people_quantity = serializers.IntegerField()