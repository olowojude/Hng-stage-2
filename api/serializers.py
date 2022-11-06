from pyexpat import model
from rest_framework import serializers
from .models import Fields

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fields
        fields = "__all__"