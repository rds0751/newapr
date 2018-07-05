from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile, Organization
from django.forms import ModelForm

rio_choices = [
    ('','Select your Role in Organization'),
    ('executive', 'Executive'),
    ('admin', 'Admin'),
    ('student', 'Student'),
]

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'tabindex': 1}), required=True)
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'tabindex': 1}), required=False)
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'tabindex': 1}), required=False)
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address','tabindex':1}))
    organisation_id = forms.ModelChoiceField(queryset=Organization.objects.filter(), label='room', widget=forms.Select)
    role_in_organisation = forms.CharField(widget=forms.Select(choices=rio_choices, attrs={'class':'form-control','tabindex':1}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','tabindex':2}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'tabindex': 2}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'organisation_id',
            'role_in_organisation',
            'password1',
            'password2',
        ]


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.oid = self.cleaned_data['organisation_id']
        user.rio = self.cleaned_data['role_in_organisation']
        #user.password1=(self.cleaned_data["password1"])

        if commit:
            user.save()
            # userprof = UserProfile.objects.create(user=user, user_id=user.id, oid=self.cleaned_data['organisation_id'],
            #                        rio=self.cleaned_data['role_in_organisation'])
            # userprof.save()
        return user
