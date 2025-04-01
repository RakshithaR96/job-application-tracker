from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company', 'position', 'status', 'notes', 'reminder_date','resume','cover_letter']  # Include reminder_date
        widgets = {
            'reminder_date': forms.DateInput(attrs={'type': 'date'})  # HTML date picker
        }
