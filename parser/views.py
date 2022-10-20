from django.db.models import Max
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from parser.models import MexModel, Backend, Qa, CurrentSession, AdminLastSession
from parser.serializers import MexSerializer, LastSessionSerializer, AdminLastSessionSerializer


class MexView(viewsets.ModelViewSet):
    serializer_class = MexSerializer
    queryset = MexModel.objects.all().order_by('tag')
    permission_classes = [permissions.AllowAny]

class LastSessionView(generics.ListAPIView):
    queryset = Backend.objects.all()
    serializer_class = LastSessionSerializer

    def get(self, request):
        results_dict = []
        querysetMax = CurrentSession.objects.all().aggregate(Max('session'))
        last_session = querysetMax['session__max']
        querysetQA = Qa.objects.filter(session=last_session)

        querysetBackend = Backend.objects.filter(session=last_session)
        for i in querysetBackend:
            i = LastSessionSerializer(i).data
            for field in i:
                print(field, i[field])
                results_dict.append(i)

        # serializer = self.get_serializer(data=querysetBackend)
        # serializer.is_valid(raise_exception=True)

        return Response(
            {"last_session": results_dict},
        )

class AdminLastSessionView(viewsets.ModelViewSet):
    serializer_class = AdminLastSessionSerializer
    querysetMax = CurrentSession.objects.all().aggregate(Max('session'))
    last_session = querysetMax['session__max']
    queryset = AdminLastSession.objects.filter(session=last_session)
    permission_classes = [permissions.AllowAny]
