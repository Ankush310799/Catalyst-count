# core/models.py

from django.db import models


class Company(models.Model):
    """ Stored data into table from CSV file """

    company_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linkedin_url = models.URLField()
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()
    

    def __str__(self):
        return self.name