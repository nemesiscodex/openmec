from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openmec.views.home', name='home'),
    url(r'^upload/$', 'openmec.views.upload_file', name='upload'),
    url(r'^files/$', 'openmec.views.files', name='files'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^funcionarios/$', 'openmec.views.funcionario_list', name='funcionario_list'),
    # rest


    url(r'^admin/', include(admin.site.urls)),
)
