from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('academics/', views.academics,name="academics"),
    path('admissions/', views.admissions,name="admissions"),
    path('campuslife/', views.campuslife,name="campuslife"),
    path('news/', views.news,name="news"),
    path('login/', views.user_login_view,name="login"),
    path('signup/', views.signup,name="signup"),
    path("logout/", views.user_logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('reset/', views.reset,name="reset"),
    path("register/", views.register, name="register"),
    path("applied/", views.applied, name="applied"),

    # Password reset flow
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="core/password_reset.html"),
        name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="core/password_reset_done.html"),
        name="password_reset_done"
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset_confirm.html"),
        name="password_reset_confirm"
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="core/password_reset_complete.html"),
        name="password_reset_complete"
    ),

]