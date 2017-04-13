# This file overrides the default behavior of collectstatic command, ignoring
# some files specified in ignore_patterns

from django.contrib.staticfiles.apps import StaticFilesConfig

class CustomStaticFilesConfig(StaticFilesConfig):
    ignore_patterns = [
        'CVS', '.*', '*~',
        'node_modules',
        'src',
        'public',
        'package.json',
    ]