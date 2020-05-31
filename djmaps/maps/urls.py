from django.conf.urls import url
from . import views

app_name = 'maps'
urlpatterns = [
    url(r'VulnerabilityIndex', views.vulIndex_map, name="vulIndex"),
    url(r'MedianHouseholdIncome', views.medIncome_map, name="medIncome"),
    url(r'TotalPopulation', views.totalPop_map, name="totalPop"),
    url(r'UnderlyingHealthIssues', views.underlyHealth_map, name="underlyHealth"),
    url(r'HealthInfrastructure', views.healthInfra_map, name="healthInfra"),
    url(r'', views.default_map, name="default"),
]