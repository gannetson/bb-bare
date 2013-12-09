from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from bluebottle.views import HomeView

urlpatterns = patterns('',
    url(r'^api/users/', include('bluebottle.accounts.urlsapi')),
    url(r'^api/utils/', include('bluebottle.bluebottle_utils.urlsapi')),
    url(r'^api/geo/', include('bluebottle.geo.urlsapi')),
    # Examples:
    # url(r'^$', 'bare_site.views.home', name='home'),
    # url(r'^bare_site/', include('bare_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls', namespace='accounts')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^documents/', include('bluebottle.bluebottle_utils.urls')),
    url(r'^admin/utils/taggit-autocomplete/', include('taggit_autocomplete_modified.urls')),
)