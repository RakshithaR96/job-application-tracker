from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobApplicationForm  # Ensure this exists

def job_list(request):
    status_filter = request.GET.get('status', '')  
    jobs = JobApplication.objects.all()

    if status_filter:
        jobs = jobs.filter(status__iexact=status_filter)

    print(f"Selected Status: {status_filter}")  # Debugging
    print(f"Filtered Jobs Count: {jobs.count()}")  # Debugging

    statuses = JobApplication.objects.values_list('status', flat=True).distinct()

    return render(request, 'tracker/job_list.html', {
        'jobs': jobs,
        'statuses': list(statuses),  
        'selected_status': status_filter  
    })


def add_job(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect("tracker:job_list")  
    else:
        form = JobApplicationForm()
    
    return render(request, "tracker/add_job.html", {"form": form})
