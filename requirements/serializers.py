from rest_framework import serializers

class ProgressSerializer(serializers.Serializer):
    by_category = serializers.ListField()
    totals = serializers.DictField()
