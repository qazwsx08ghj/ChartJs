from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from chart.api.views import (
    api_datas_view,
    api_create_datas_view
)

app_name = 'chart'

urlpatterns = [
    path('', csrf_exempt(api_datas_view.as_view()), name="data"),
    path('create', api_create_datas_view, name="create"),
]
