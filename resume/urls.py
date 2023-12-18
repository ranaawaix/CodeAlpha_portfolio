from django.urls import path
from resume.views import ResumeView


urlpatterns = [
    path('my_resume', ResumeView.as_view(), name='resume'),
]
