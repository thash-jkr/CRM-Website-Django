from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path, include
from leads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPageView.as_view(), name="landing"),
    path('leads/', include("leads.urls", namespace='leads')),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('agents/', include("agents.urls", namespace="agents")),
    path('password-reset/', PasswordResetView.as_view(), name="password-reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confrim"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
