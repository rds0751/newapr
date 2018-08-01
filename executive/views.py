from django.contrib.auth.models import User
# Create your views here.

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

__title__ = 'fobi.contrib.plugins.form_handlers.db_store.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'view_saved_form_data_entries',
    'export_saved_form_data_entries',
    'view_saved_form_wizard_data_entries',
    'export_saved_form_wizard_data_entries',
)

# *****************************************************************************
# *************************** Form handler views ******************************
# *****************************************************************************

# entries_permissions = [
#    'db_store.add_savedformdataentry',
#    'db_store.change_savedformdataentry',
#    'db_store.delete_savedformdataentry',
# ] 

def approve_form_entry(request, form_entry_id=None, feid=None):
    entries = SavedFormDataEntry.objects.get(form_entry__id=form_entry_id, id=feid)
    entries.approved = True
    entries.approved_by = request.user.first_name
    entries.save()
    return redirect('savedformentry-detail', form_entry_id=form_entry_id, feid=feid)

def disapprove_form_entry(request, form_entry_id=None, feid=None):
    entries = SavedFormDataEntry.objects.get(form_entry__id=form_entry_id, id=feid)
    entries.disapproved = True
    entries.disapproved_by = request.user.first_name
    entries.save()
    return redirect('savedformentry-detail', form_entry_id=form_entry_id, feid=feid)

def saved_form_data_entries_detailview(
        request, form_entry_id=None, feid=None, theme=None,
        template_name="db_store/savedformdataentry_detail.html"):
    if request.method == "GET":
        entries = SavedFormDataEntry.objects.get(form_entry_id=form_entry_id, id=feid)
        print(entries.id)
        comments = Comments.objects.filter(ident=entries.id)
        form = CommentForm()
        context = {'entry': entries, "comments": comments, "form":form, "comment_id":feid}


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
    else:
        form = CommentForm(request.POST)
        entries = SavedFormDataEntry.objects.get(form_entry__id=form_entry_id, id=feid)
        print(entries.id)
        print(type(entries.id))
        comments = Comments.objects.filter(ident=entries.id)
        context = {'entry': entries, "comments": comments}
        if form.is_valid():
            comment = form.save(commit=False)
            comment.form_entry = entries.form_entry
            comment.created_by = UserProfile.objects.get(user=request.user)
            comment.ident = feid
            comment.save()
            if theme:
                context.update({'fobi_theme': theme})

            widget = get_form_handler_plugin_widget(
                UID, request=request, as_instance=True, theme=theme
            )
            forms = CommentForm
            context.update({"form":forms})
            if widget and widget.view_saved_form_data_entries_template_name:
                template_name = widget.view_saved_form_data_entries_template_name

            if versions.DJANGO_GTE_1_10:
                return render(request, template_name, context)
            else:
                return render_to_response(
                    template_name, context, context_instance=RequestContext(request)
                )


# @permissions_required(satisfy=SATISFY_ANY, perms=entries_permissions)
@login_required
def dashboard(
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
        .filter(form_entry__approvers__id__exact=request.user.pk)
    print (entries)

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
