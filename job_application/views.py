from django.shortcuts import render
from django.contrib import messages
from .forms import ApplicationForm
from datetime import datetime
from .models import Form


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ApplicationForm()
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = datetime.strptime(form.cleaned_data["date"], "%Y-%m-%d")

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date)
            messages.success(request, "Form submitted successfully")
    return render(request, "index.html")
