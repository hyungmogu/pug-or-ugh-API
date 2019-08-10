from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

import pugorugh.views as views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/dog/(?P<pk>[\-\d]+)/(?P<type>undecided|liked|disliked)/next/$', views.RetrieveNextDogView.as_view(), name='dog-next'),
    url(r'^api/dog/(?P<pk>\d+)/(?P<type>undecided|liked|disliked)/$', views.RetrieveDogView.as_view(), name='dog'),
    url(r'^api/user/preferences/$', views.UserPerfView.as_view(), name='perf-user'),
    url(r'^api/user/login/$', obtain_auth_token, name='login-user'),
    url(r'^api/user/$', views.UserRegisterView.as_view(), name='register-user'),
    url(r'^favicon\.ico$',
        RedirectView.as_view(
            url='/static/icons/favicon.ico',
            permanent=True
        )),
    url(r'^$', TemplateView.as_view(template_name='index.html'))
])
