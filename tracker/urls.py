from django.urls import path
from . import views

app_name = "tracker"  # This must match the namespace in your template

urlpatterns = [
    path('job_list/', views.job_list, name='job_list'),
    path('add/', views.add_job, name='add_job'),

]

