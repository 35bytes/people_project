from django.urls import path
from .views import *

urlpatterns = [
    path('drugs', DrugsAPIView.as_view()),
    path('drugs/<int:pk>', DrugsAPIView.as_view()),
    path('drug', DrugAPIView.as_view()),
    path('drug/<int:pk>', DrugAPIView.as_view()),
    path('vaccinations', VaccinationsAPIView.as_view()),
    path('vaccinations/<int:pk>', VaccinationsAPIView.as_view()),
]