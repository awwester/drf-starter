from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from .routers import router
from .docs import schema_view


# Prefix to be used on all v1 API urls
v1_prefix = 'v1/'
def v1_url(url):
    # Prepend a url string with the v1 prefix.
    return v1_prefix + url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='admin/')),

    # API urls
    path(v1_url('docs/'), schema_view.with_ui('redoc', cache_timeout=0),
         name='api-docs'),
    path(v1_prefix, include(router.urls)),
    path(v1_url('auth/'), include('rest_auth.urls')),
    path(v1_url('auth/registration/'), include('rest_auth.registration.urls')),
]
