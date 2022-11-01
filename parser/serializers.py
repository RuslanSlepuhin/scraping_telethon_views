from rest_framework import serializers

from parser.models import MexModel, CurrentSession, AdminLastSession, PatternModel


class MexSerializer(serializers.ModelSerializer):
    class Meta:
        model = MexModel
        fields = ['tag', 'value']


class AdminLastSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLastSession
        fields = '__all__'

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatternModel
        fields = '__all__'

