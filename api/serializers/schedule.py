from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)

        timestamp_start, timestamp_end = attrs['timestamp_start'], attrs['timestamp_end']

        exists = Schedule.objects.filter(
            timestamp_start__lte=timestamp_start,
            timestamp_end__gte=timestamp_start
        ).exists()

        if exists:
            raise ValidationError("У нас есть накладка")