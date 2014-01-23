from django.conf.urls import patterns, include, url
# from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^beer-penalty/', include('fagkom.apps.beer_penalty.urls')),
    url(r'auth/', include('fagkom.apps.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('fagkom.apps.main.urls')),

    # Athentication (solved by auth app)
    # url(r'^accounts/login/', 'django.contrib.auth.views.login',
    #     {'template_name': 'login.html'}),
    # (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # (r'^accounts/$', RedirectView.as_view(url='/')),
    # (r'^accounts/profile/$', RedirectView.as_view(url='/')),
)
