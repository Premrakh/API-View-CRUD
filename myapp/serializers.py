from rest_framework import serializers
from .models import *

class DataCon(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields='__all__'