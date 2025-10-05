from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(required=True)

    class Meta:
        model = CustomUser
        fields = ["id", "name", "email", "age"]

    def validate_age(self, value):
        if value < 0 or value > 120:
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return value


class CSVUploadResponseSerializer(serializers.Serializer):
    saved_records = serializers.IntegerField()
    rejected_records = serializers.IntegerField()
    errors = serializers.ListField()
