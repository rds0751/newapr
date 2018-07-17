from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from applicant.models import Document
from applicant.forms import DocumentForm, VerificationForm

from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# from fobi.decorators import permissions_required, SATISFY_ALL, SATISFY_ANY
from django.views.generic import DetailView
from requests import post

from core.models import UserProfile
from fobi.contrib.plugins.form_handlers.db_store.forms import CommentForm
from fobi.contrib.plugins.form_handlers.db_store.base import (
    get_form_handler_plugin_widget,
    get_form_wizard_handler_plugin_widget,
)

from nine import versions

from fobi.contrib.plugins.form_handlers.db_store import UID
from fobi.contrib.plugins.form_handlers.db_store.models import SavedFormDataEntry, SavedFormWizardDataEntry, Comments
from fobi.contrib.plugins.form_handlers.db_store.helpers import DataExporter

if versions.DJANGO_GTE_1_10:
    from django.shortcuts import render, redirect
else:
    from django.shortcuts import render_to_response


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

def verify(request):
    return render(request, 'applicant/verify.html')

@login_required
def applicant_dashboard(
        request, form_entry_id=None, theme=None,
        template_name='applicant/applicant_dashboard.html'):
    """View saved form data entries.

    :param django.http.HttpRequest request:
    :param int form_entry_id: Form ID.
    :param fobi.base.BaseTheme theme: Subclass of ``fobi.base.BaseTheme``.
    :param string template_name:
    :return django.http.HttpResponse:
    """

    entries = SavedFormDataEntry._default_manager\
        .select_related('form_entry') \
        .filter(submitted_by__exact=request.user)
    print('applicant')
    print(request.user)

    if form_entry_id:
        entries = entries.filter()

    context = {'entries': entries, 'form_entry_id': form_entry_id}

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    widget = get_form_handler_plugin_widget(
        UID, request=request, as_instance=True, theme=theme
    )

    if widget and widget.view_saved_form_data_entries_template_name:
        template_name = widget.view_saved_form_data_entries_template_name

    if versions.DJANGO_GTE_1_10:
        return render(request, template_name, context)
    else:
        return render_to_response(
            template_name, context, context_instance=RequestContext(request)
        )

@login_required
def past_applications(
        request, form_entry_id=None, theme=None,
        template_name='db_store/view_saved_form_data_entries.html'):
    """View saved form data entries.

    :param django.http.HttpRequest request:
    :param int form_entry_id: Form ID.
    :param fobi.base.BaseTheme theme: Subclass of ``fobi.base.BaseTheme``.
    :param string template_name:
    :return django.http.HttpResponse:
    """

    entries = SavedFormDataEntry._default_manager\
        .select_related('form_entry') \
        .filter(submitted_by__exact=request.user)

    if form_entry_id:
        entries = entries.filter()

    context = {'entries': entries, 'form_entry_id': form_entry_id}

    # If given, pass to the template (and override the value set by
    # the context processor.
    if theme:
        context.update({'fobi_theme': theme})

    widget = get_form_handler_plugin_widget(
        UID, request=request, as_instance=True, theme=theme
    )

    if widget and widget.view_saved_form_data_entries_template_name:
        template_name = widget.view_saved_form_data_entries_template_name

    if versions.DJANGO_GTE_1_10:
        return render(request, template_name, context)
    else:
        return render_to_response(
            template_name, context, context_instance=RequestContext(request)
        )
