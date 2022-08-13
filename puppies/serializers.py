from rest_framework import serializers
from .models import Puppy


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = (
            'id',
            'name',
            'age',
            'breed',
            'color',
            'get_created_at',
            'get_updated_at'
        )



