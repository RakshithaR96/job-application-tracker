from django.urls import path
from .views import job_list, add_job  # Import your views

app_name = "tracker"  # This must match the namespace in your template

urlpatterns = [
    path('', job_list, name='job_list'),
    path('add/', add_job, name='add_job'),
]
