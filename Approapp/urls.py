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
from django.conf.urls.static import static
from django.contrib import admin

from Approapp import settings
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls'), name="home"),
    # View URLs
	url(r'^fobi/', include('fobi.urls.view')),
    url(r'^applicant/', include('applicant.urls')),
    url(r'^executive/', include('executive.urls')),

	# Edit URLs
	url(r'^fobi/', include('fobi.urls.edit')),
	url(r'^fobi/plugins/form-handlers/db-store/', include('fobi.contrib.plugins.form_handlers.db_store.urls')),
    url(r'^msg/', include('messenger.urls'), name="msg"),

    #conver to pdf
    url('^pdf/$', views.GeneratePdf.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
