from django.conf.urls.defaults import *
from rpgdashapp.models import *
from rpgdashapp import views

urlpatterns = patterns('django.views.generic.simple',
	#(r'(.+\.html)$', 'direct_to_template'),
	#(r'(.+\.css)$', 'direct_to_template'),
	#(r'', 'direct_to_template', {'template':'index.html'}),
	url(r'^$', views.index, name='index')
)





