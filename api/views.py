from django.shortcuts import render
from .models import AppInfo
from .serializers import ApplicationSerializer
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import os
import re
from rest_framework.exceptions import ValidationError

# Create your views here.

class ApplicationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = AppInfo.objects.all()
    serializer_class = ApplicationSerializer

    def get_package_name_version(self):
        application = self.request.FILES.get('application')
        all_apk_info = os.popen("aapt dump badging %s" % application.temporary_file_path()).read()
        package_name = re.compile(r"package: name='(\S+)'").findall(all_apk_info)
        package_version_code = re.compile(r"versionCode='(\S+)'").findall(all_apk_info)
        return application, package_name, package_version_code

    def perform_update(self, serializer):
        application, package_name, package_version_code = self.get_package_name_version()
        if package_name and package_version_code:
            serializer.save(application=application, package_name=package_name[0], package_version_code=package_version_code[0])
        else:
            raise ValidationError()

    def perform_create(self, serializer):
        application, package_name, package_version_code = self.get_package_name_version()
        if package_name and package_version_code:
            serializer.save(application=application, package_name=package_name[0], package_version_code=package_version_code[0])
        else:
            raise ValidationError()
