from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pregunta_id>[0-9]+)/$', views.detalles, name='detalles'),
    url(r'^(?P<pregunta_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
    url(r'^(?P<pregunta_id>[0-9]+)/votar/$', views.votar, name='votar'),

]