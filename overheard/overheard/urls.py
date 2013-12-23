from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory
from posts.views import PostListView
from posts.models import Post
admin.autodiscover()

# TODO: Get ordering by likes working
#sqs = SearchQuerySet().order_by('-num_likes')#.exclude(body__isnull=True).exclude(body__exact='')
urlpatterns = patterns('haystack.views',
    # Examples:
    # url(r'^$', 'overheard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^search/$', search_view_factory(), name='haystack_search'),
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