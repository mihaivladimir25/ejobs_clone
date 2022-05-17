"""ejobs_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejobs.views import index, list_jobs, add_job, added_success, \
    apply, application_successful, show_jobs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('apply/', list_jobs),
    path('add/', add_job),
    path('add/success/', added_success),
    path('apply/form/', apply),
    path('apply/form/application-successful/', application_successful),
    path('show-jobs/', show_jobs),
]