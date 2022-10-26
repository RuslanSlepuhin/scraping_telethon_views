from django.db.models import Max
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from parser.models import MexModel, CurrentSession, AdminLastSession
from parser.serializers import MexSerializer, AdminLastSessionSerializer


class MexView(viewsets.ModelViewSet):
    serializer_class = MexSerializer
    queryset = MexModel.objects.all().order_by('tag')
    permission_classes = [permissions.AllowAny]


class AdminLastSessionView(viewsets.ModelViewSet):
    serializer_class = AdminLastSessionSerializer
    # querysetMax = CurrentSession.objects.all().aggregate(Max('session'))
    # last_session = querysetMax['session__max']
    # queryset = AdminLastSession.objects.filter(session=last_session)
    queryset = AdminLastSession.objects.filter()

    permission_classes = [permissions.AllowAny]
