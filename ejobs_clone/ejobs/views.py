from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Company, Employee, Job
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'index.html')


def add_job(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        position = request.POST['position']
        city = request.POST['city']
        description = request.POST['description']
        categories = request.POST['categories']
        company = Company.objects.get(name=company_name)
        jb = Job(company=company, position=position, city=city, description=description, categories=categories)
        jb.save()
        return HttpResponseRedirect('success/')
    companies = Company.objects.all()
    return render(request, 'form.html', {'companies': companies})


def added_success(request):
    job = Job.objects.latest('id')
    return render(request, 'success.html', {'job': job})


def list_jobs(request):
    job = Job.objects.all()
    return render(request, 'display_job.html', {'job': job})


def apply(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        university = request.POST['university']
        company = request.POST['company_name']
        position = request.POST['position']

        com = Company.objects.get(name=company)
        jb = com.job_set.get(position=position)
        employee = Employee(first_name=first_name, last_name=last_name, university=university, job=jb)
        employee.save()
        return HttpResponseRedirect('application-successful/')

    companies = Company.objects.all()
    return render(request, 'apply-form.html', {'companies': companies})


def application_successful(request):
    Person = Employee.objects.latest('id')
    jobs = []
    people = Employee.objects.all()
    for person in people:
        if person.first_name == Person.first_name and person.last_name == Person.last_name:
            jobs.append(person.job)
    context = {'Person': Person, 'jobs': jobs}
    return render(request, 'application-successful.html', context=context)


def show_jobs(request):
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']

        jobs = []
        for empl in Employee.objects.all():
            if empl.first_name == first_name and empl.last_name == last_name:
                jobs.append(empl.job)

        return render(request, 'show-jobs.html', {'jobs': jobs, 'var': 1})

    return render(request, 'show-jobs.html', {"var": 0})

