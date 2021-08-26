from django.contrib import admin
from .models import Hello
# Register your models here.


@admin.register(Hello)
class HelloAdmin(admin.ModelAdmin):
    list_display = ['content',]
    readonly_fields = ['regist_date','update_date',]