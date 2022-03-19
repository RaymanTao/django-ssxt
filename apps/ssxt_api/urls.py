from django.urls import include
from django.conf.urls import url

app_name = 'ssxt_api'

urlpatterns = [
    url(r'^sssq/', include('apps.ssxt_api.sssq.urls', namespace='sssq')),
]
