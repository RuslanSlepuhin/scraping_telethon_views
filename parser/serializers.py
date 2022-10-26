from rest_framework import serializers

from parser.models import MexModel, CurrentSession, AdminLastSession


class MexSerializer(serializers.ModelSerializer):
    class Meta:
        model = MexModel
        fields = ['tag', 'value']


class AdminLastSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLastSession
        fields = '__all__'

