import io
from rest_framework import serializers
from .models import Material
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class MaterialSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Material
        fields = "__all__"
