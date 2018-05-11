from django.shortcuts import render, redirect
# Create your views here.
from applicant.models import Document
from applicant.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'applicant/home.html', { 'documents': documents })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'applicant/model_form_upload.html', {
        'form': form
    })