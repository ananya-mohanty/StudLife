from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserFormView.as_view(), name="doctor_login"),
    path('view/', views.logged_in, name="doctor_logged_in"),
    path('view/<int:profile_id>', views.individual_request, name="individual_request"),
]
