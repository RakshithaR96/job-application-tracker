from django.contrib import admin
from .models import JobApplication  # Import the model

# Register the JobApplication model so it appears in the admin panel
admin.site.register(JobApplication)
