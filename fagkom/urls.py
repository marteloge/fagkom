from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fagkom.views.home', name='home'),
    # url(r'^fagkom/', include('fagkom.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
