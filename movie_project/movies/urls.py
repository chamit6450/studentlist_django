from django.urls import path
from .views import home, student_detail

urlpatterns = [
    path('', home, name='home'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),
]
