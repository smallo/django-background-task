import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'
INSTALLED_APPS = [ 'background_task' ]


# http://pypi.python.org/pypi/django-coverage

INSTALLED_APPS.append('django_coverage')
COVERAGE_REPORT_HTML_OUTPUT_DIR = 'html_coverage'
COVERAGE_MODULE_EXCLUDES = []
