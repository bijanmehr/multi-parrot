from rest_framework import serializers
from parrot_control import models


class ParrotCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParrotCommand
        fields = ('id', 'name', 'title', 'category_id', 'tag', 'perform_time', 'priority', 'parrot_0', 'parrot_1')
        read_only_fields = ('id', 'name', 'title', 'category_id', 'tag', 'perform_time', 'priority', 'parrot_0', 'parrot_1')
