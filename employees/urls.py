from django.urls import path
from .views import *

urlpatterns = [
    path(
        'employees/',
        EmployeeListCreateView.as_view(),
        name='employees'
    ),

    path(
        'employees/<int:pk>/',
        EmployeeRetrieveUpdateDeleteView.as_view(),
        name='employee-detail'
    ),
]