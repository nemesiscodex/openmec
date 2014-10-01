from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openmec.views.home', name='home'),
    url(r'^upload/$', 'openmec.views.upload_file', name='upload'),
    url(r'^files/$', 'openmec.views.files', name='files'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^funcionario/$', 'openmec.views.funcionario_list', name='funcionario_list'),
    url(r'^funcionario/(?P<documento>[0-9]+)/$', 'openmec.views.funcionario', name='funcionario'),

    url(r'^objeto_gasto/$', 'openmec.views.objeto_gasto_list', name='objeto_gasto_list'),
    url(r'^objeto_gasto/(?P<codigo>[0-9]+)/$', 'openmec.views.objeto_gasto', name='objeto_gasto'),

    url(r'^dependencia/$', 'openmec.views.dependencia_list', name='dependencia_list'),
    # url(r'^dependencia/(?P<codigo>[0-9]+$', 'openmec.views.dependencia', name='dependencia'),

    url(r'^cargo/$', 'openmec.views.cargo_list', name='cargo_list'),

    url(r'^rubro/$', 'openmec.views.rubro_list', name='rubro_list'),
    url(r'^rubro/(?P<documento>[0-9]+)/$', 'openmec.views.rubro', name='rubro'),

    url(r'^concepto/$', 'openmec.views.concepto_list', name='concepto_list'),

    # rest


    url(r'^admin/', include(admin.site.urls)),
)
