# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rpgdashapp.models import *
import rpgdashapp.level


def index(request):
	achievements = []
	skills = Skill.objects.all() #["jason", "anderson"]
	skillsLevelsMetrics = []
	for s in skills:
		metricList = []
		skillTotal = 0
		for m in Metric.objects.filter(skill=s):
			skillTotal += m.metricValue()
			metricList.append(m)
		addTuple = (s, rpgdashapp.level.XPToLevel(skillTotal), metricList,)
		skillsLevelsMetrics.append(addTuple)
	
	context = {'name': "Jason Anderson", 'achievements': achievements, "skills":skills, "skillsLevelsMetrics":skillsLevelsMetrics}

	if mobileBrowser(request):
		return render(request, 'indexMobile.html', context)
	else:
		return render(request, 'index.html', context)

    #return HttpResponse("Hello, world. You're at the poll index.")


# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]
def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''
 
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser

