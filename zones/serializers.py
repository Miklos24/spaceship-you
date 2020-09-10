from rest_framework import serializers
from .models import ZoneTimes

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneTimes
        fields = ('user', 'couch_a', 'couch_u', 'exe_a', 'exe_u', 'creat_a', 'creat_u', 'sleep_a', 'sleep_u')
