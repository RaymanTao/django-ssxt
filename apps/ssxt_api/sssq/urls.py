from django.conf.urls import url
from apps.ssxt_api.sssq import views

app_name = 'sssq'

urlpatterns = [
    url(r'^index/', views.index, name='index'),
]
