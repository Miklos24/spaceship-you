from rest_framework import serializers
from .models import ZoneTimes

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneTimes
        fields = ('user', 'couch_alotted', 'couch_used', 'exercise_alotted',
        'exercise_used', 'creative_allotted', 'creative_used',
        'sleep_alotted', 'sleep_used')
