from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import AnalyticsSerializer
from work.models import Analytics

'''
Class based view for analytics api
'''
class AnalyticsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
