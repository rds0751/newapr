from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from core.forms import RegistrationForm
# Create your views here.
from .models import UserProfile
        

def home(request):
    return render(request, 'core/index.html')


def mainpage(request):
    if request.user.is_authenticated:
        ui = UserProfile.objects.get(user=request.user)
        if ui.rio == "applicant":
            return redirect('/fobi/orglist')
        elif ui.rio == "organisation":
            return redirect('/fobi/forms/create')
        else:
            return render(request, 'executive/home.html')
    else:
        args = {}
        return render(request,'/main_page.html', args)

#def login_redirect(request):
    #return redirect('loginReg/login')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                oid = form.cleaned_data['organisation_id']
                rio = form.cleaned_data['role_in_organisation']
                first_name = form.cleaned_data['first_name']
                user = User.objects.get(first_name=first_name)
                up = UserProfile.objects.get(user=user)
                up.rio = rio
                up.oid = oid
                up.save()
                return redirect('/')
            else:
                args = {'form': form}
                return render(request, 'core/reg_form.html', context=args)
        else:
            form = RegistrationForm()
            args = {'form': form}
            return render(request, 'core/reg_form.html', context=args)


def profile_view(request):
    usr = UserProfile.objects.get(user=request.user)
    args = {'user':usr}
    return render(request,'core/profile.html',args)

def profile_edit(request):
    if request.method=='POST':
        form=UserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form=UserChangeForm(instance=request.user)
        args={'form':form}
        return render(request,'core/edit.html',args)