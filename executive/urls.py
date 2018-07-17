"""Approapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    # ***********************************************************************
    # ***********************************************************************
    # ************************* Form handlers *******************************
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # **************************** Listing **********************************
    # ***********************************************************************
    # Specific form entries listing
    url(r'^(?P<form_entry_id>\d+)/$',
        view=views.dashboard,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'view_saved_form_data_entries'),

    url(r'^$',
        view=views.dashboard,
        name='fobi.contrib.plugins.form_handlers.db_store.'
             'view_saved_form_data_entries'),
    
    url(r'^(?P<form_entry_id>[-\w]+)/detail/(?P<feid>[-\w]+)/$', view=views.saved_form_data_entries_detailview, name='savedformentry-detail'),

    url(r'^(?P<form_entry_id>[-\w]+)/detail/(?P<feid>[-\w]+)/approve$', view=views.approve_form_entry, name='approve'),

    url(r'^(?P<form_entry_id>[-\w]+)/detail/(?P<feid>[-\w]+)/disapprove$', view=views.disapprove_form_entry, name='approve'),
    
]