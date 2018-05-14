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
    #
    # def save(self, commit=True):
    #     fn = self.cleaned_data['executive']
    #     user = self.objects.get(first_name=fn)
    #     des = self.cleaned_data['description']
    #     doc = self.cleaned_data['document']
    #     dc = Document(executive=user, description=des, document=doc)
    #     dc.save()