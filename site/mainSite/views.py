# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate as django_auth
from django.http import HttpResponse

def do_basic_auth(request):
	try:
		auth_string = request.META['HTTP_AUTHORIZATION']
		shit, moreshit, thestring = auth_string.partition(' ')
		username, sep, password =  thestring.decode('base64').partition(':')
		user = django_auth(username = username, password = password)
		if user is None:
			resp = HttpResponse()
			resp.status_code = 403
		else:
			resp = HttpResponse()
			resp.status_code = 200
	except KeyError, e:
		resp = HttpResponse()
		resp.status_code = 401
		resp['WWW-Authenticate'] = 'Basic Realm = "18SG JACAS"'
	return resp

