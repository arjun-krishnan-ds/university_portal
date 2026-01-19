# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentLoginForm, AdmissionApplicationForm
from .models import Programs, Departments, Faculty, Admission
import pycountry
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


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
            login(request, user)  # auto-login after signup
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    # ✅ ALWAYS return a response
    return render(request, "core/signup.html", {"form": form})


def user_login_view(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = StudentLoginForm()

    return render(request, "core/signin.html", {"form": form})


@login_required(login_url="login")
def dashboard(request):
    return render(request, "core/dashboard.html")


def user_logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form = AdmissionApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("applied")
    else:
        form = AdmissionApplicationForm()

    exclude_fields = [
        "phone_country_code",
        "local_phone_number",
    ]

    return render(request, "core/register.html", {
        "form": form,
        "exclude_fields": exclude_fields
    })

def applied(request):
    return render(request, "core/applied.html")


def reset(req):
    return render(req, "core/reset.html")


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
