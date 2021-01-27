from rest_framework import serializers
from api.models import AppInfo

class ApplicationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    package_name = serializers.ReadOnlyField()
    package_version_code = serializers.ReadOnlyField()
    class Meta:
        model = AppInfo
        fields = ['id', 'application', 'package_name', 'package_version_code']