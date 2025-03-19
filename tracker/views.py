from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobApplicationForm  # Make sure JobForm exists

def job_list(request):
    jobs = Job.objects.all()
    return render(request, "tracker/job_list.html", {"jobs": jobs})

def add_job(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tracker:job_list")  # Ensure namespace is correct
    else:
        form = JobApplicationForm()
    
    return render(request, "tracker/add_job.html", {"form": form})
