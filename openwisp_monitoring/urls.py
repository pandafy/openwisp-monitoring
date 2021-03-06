from django.conf import settings
from django.conf.urls import include, url

url_metadata = [
    # openwisp_monitoring.monitoring
    {
        'regexp': r'^',
        'app': 'openwisp_monitoring.device',
        'include': {'module': '{app}.api.urls', 'namespace': 'monitoring'},
    },
]

urlpatterns = []

for meta in url_metadata:
    module = meta['include'].pop('module')
    if 'app' in meta:
        # if app attribute is specified, ensure the app is installed, or skip otherwise
        # this allows some flexibility during development or when trying custom setups
        if meta['app'] not in settings.INSTALLED_APPS:
            continue
        # DRY python module path
        module = module.format(**meta)
    urlpatterns.append(url(meta['regexp'], include(module, **meta['include'])))
