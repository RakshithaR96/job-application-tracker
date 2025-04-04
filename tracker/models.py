from django.db import models

class JobApplication(models.Model):
    # creates below table in database
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview Scheduled'),
        ('offer', 'Offer Received'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    ]

    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    notes = models.TextField(blank=True, null=True)
    applied_date = models.DateField(auto_now_add=True)
    reminder_date = models.DateField(blank=True, null=True)  # New field

    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    cover_letter = models.FileField(upload_to="cover_letters/", blank=True, null=True)


    def __str__(self):
        return f"{self.position} at {self.company}"
