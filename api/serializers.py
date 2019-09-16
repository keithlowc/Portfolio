from rest_framework import serializers

from work.models import Analytics

'''
Serializer class for analytics
'''
class AnalyticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analytics
        fields = ['type', 'headers', 'date']
