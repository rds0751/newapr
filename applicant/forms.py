from django import forms
from django.contrib.auth.models import User

from applicant.models import Document
from core.models import UserProfile



class DocumentForm(forms.ModelForm):
    description = forms.CharField(max_length=30)
    document = forms.FileField(widget=forms.FileInput())
    class Meta:
        model = Document
        fields = ('description', 'document', )

class VerificationForm(forms.Form):
    ID = forms.CharField(max_length=30)
    class Meta:
        fields = ('ID', )
