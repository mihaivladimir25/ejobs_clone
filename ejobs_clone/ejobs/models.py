from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    headquarters = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'


class Job(models.Model):
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    categories = models.CharField(max_length=1000)
    city = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.position} at {self.company.name}'


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
