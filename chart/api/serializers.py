from rest_framework import serializers
from chart.models import datas


class DatasSerialzer(serializers.ModelSerializer):
    class Meta:
        model = datas
        fields = ['number', 'value']
