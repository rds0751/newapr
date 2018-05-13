from django.contrib.auth.models import User
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
            # fn = form.cleaned_data['executive']
            # user = User.objects.get(first_name=fn)
            # des = form.cleaned_data['description']
            # doc = form.cleaned_data['document']
            # dc = Document(executive=user, description=des, document=doc)
            # dc.save()
            form.save()
            return redirect('home')
        else:
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'applicant/model_form_upload.html', {
        'form': form
    })