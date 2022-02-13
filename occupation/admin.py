from django.contrib import admin

from occupation.models import Occupation


@admin.register(Occupation)
class AdmWorkers(admin.ModelAdmin):
    list_display = ('id', 'name')