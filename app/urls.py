from django.urls import path
from .views import view_chart

urlpatterns = [
    path("",view_chart, name="Chart")
]