from django.db import models
import subprocess
import os
import re

class AppInfo(models.Model):
    application = models.FileField()
    package_name = models.CharField(max_length = 127)
    package_version_code = models.CharField(max_length = 20)