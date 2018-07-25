from django.contrib import admin

# Register your models here.
from applicant.models import Document
from .models import Ticket

admin.site.register(Ticket)

admin.site.register(Document)
