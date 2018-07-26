from django.contrib import admin

# Register your models here.
from applicant.models import Document
from .models import Post

admin.site.register(Post)

admin.site.register(Document)
