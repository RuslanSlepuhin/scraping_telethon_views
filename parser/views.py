from django.db.models import Max
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from parser.models import MexModel, CurrentSession, AdminLastSession, PatternModel
from parser.serializers import MexSerializer, AdminLastSessionSerializer, PatternSerializer, ProfSerializer, \
    PatternChangeSerializer


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

class GetFromAdminView(generics.GenericAPIView):
    serializer_class = MexSerializer
    queryset = AdminLastSession.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for i in request.data['results']:
            print(i)
        return Response({'success': serializer.data})

class PatternView(generics.GenericAPIView):

    serializer_class = PatternSerializer
    queryset = PatternModel.objects.all()

    def get(self, request):
        queryset = PatternModel.objects.all()
        self.how_pattern_dict: dict
        self.show_pattern_dict = {}
        keys = []
        for i in queryset:
            print(i.key)
            keys.append(i.key)
        keys = set(keys)
        for i in keys:
            self.show_pattern_dict[i] = {'ma': [], 'mex': []}

        for i in queryset:
            if i.ma:
                self.show_pattern_dict[i.key]['ma'].append(i.value)
            elif i.mex:
                self.show_pattern_dict[i.key]['mex'].append(i.value)

        return Response({'pattern': self.show_pattern_dict})

    def post(self, request):
        serializer = PatternSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.validated_data())
        PatternModel.objects.create(
            key = serializer.validated_data['key'],
            ma = serializer.validated_data['ma'],
            mex = serializer.validated_data['mex'],
            value = serializer.validated_data['value']
        )

        return Response({'pattern': self.show_pattern_dict})

class BackendView(viewsets.ModelViewSet):
    serializer_class = ProfSerializer
    queryset = AdminLastSession.objects.filter(profession__icontains='backend').order_by('time_of_public')
    permission_classes = [permissions.AllowAny]

class PatternChangeView(viewsets.ModelViewSet):
    serializer_class = PatternChangeSerializer
    queryset = PatternModel.objects.all().order_by('key')
    permission_classes = [permissions.AllowAny]
