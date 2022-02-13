from django.db import models


class Occupation(models.Model):
    name = models.CharField('Name', max_length=200)
    company_name = models.CharField('Company name', max_length=100)
    position_name = models.CharField('Position name', max_length=100)
    hire_date = models.DateField('Hire date')
    fire_date = models.DateField('Fire date', null=True, blank=True)
    salary = models.IntegerField('Salary')
    fraction = models.IntegerField('Fraction')
    base = models.IntegerField('Base')
    advance = models.IntegerField('Advance')
    by_hours = models.BooleanField('By hours')

    def __str__(self):
        return self.name