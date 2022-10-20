from rest_framework import serializers

from parser.models import MexModel, CurrentSession, Backend, AdminLastSession


class MexSerializer(serializers.ModelSerializer):
    class Meta:
        model = MexModel
        fields = ['tag', 'value']

class LastSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backend
        fields = '__all__'

class AdminLastSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLastSession
        fields = '__all__'

