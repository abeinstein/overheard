from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from posts.views import PostListView
from haystack.views import SearchView, search_view_factory
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'overheard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PostListView.as_view(), name='home')
    (r'^search/', include('haystack.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )