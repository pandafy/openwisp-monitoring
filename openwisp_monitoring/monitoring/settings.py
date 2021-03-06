from django.conf import settings

INFLUXDB_HOST = getattr(settings, 'INFLUXDB_HOST', 'localhost')
INFLUXDB_PORT = getattr(settings, 'INFLUXDB_PORT', '8086')
INFLUXDB_USER = getattr(settings, 'INFLUXDB_USER')
INFLUXDB_PASSWORD = getattr(settings, 'INFLUXDB_PASSWORD')
INFLUXDB_DATABASE = getattr(settings, 'INFLUXDB_DATABASE', 'openwisp2')

ADDITIONAL_CHARTS = getattr(settings, 'OPENWISP_MONITORING_CHARTS', {})
