from rest_framework import serializers

from .models import *


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ('title', 'content', 'price_per_day')