# core/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import ApplicationForm, StudentLoginForm
from .models import Programs, Departments, Faculty, Admission
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy


# Create your views here.
def index(req):
    return render(req, "core/index.html")


def about(req):
    return render(
        req,
        "core/about.html",
        {"departments": Departments.objects.all(), "faculty": Faculty.objects.all},
    )


def academics(request):
    return render(
        request,
        "core/academics.html",
        {
            "ug_programs": Programs.objects.filter(level="UG"),
            "pg_programs": Programs.objects.filter(level="PG"),
            "phd_programs": Programs.objects.filter(level="PHD"),
        },
    )


def admissions(req):
    admissions = Admission.objects.all()
    return render(req, "core/admissions.html", {"admissions": admissions})


def campuslife(req):
    return render(req, "core/campuslife.html")


def news(req):
    return render(req, "core/news.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect("core/dashboard.html")
    else:
        form = UserCreationForm()
        return render(request, "core/signup.html", {"form": form})


def student_login_view(req):
    if req.method == "POST":
        form = StudentLoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect("student_dashboard")  # Replace with your dashboard URL
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = StudentLoginForm()

    return render(req, "core/signin.html", {"form": form})


@login_required
def dashboard(req):
    return render(req, "core/dashboard.html")


def reset(req):
    return render(req, "core/reset.html")


def register(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ApplicationForm()

    return render(request, "core/register.html", {"form": form})


def applied(request):
    return render(request, "core/applied.html")


class CustomPasswordResetView(PasswordResetView):
    template_name = "core/password_reset.html"
    email_template_name = "core/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "core/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "core/password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "core/password_reset_complete.html"
