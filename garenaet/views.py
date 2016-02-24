import json
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, ET!")

def login(request):
	response_data = {}
	if request.method == 'POST':
		request_data = json.loads(request.body)
		print 'username %s, password %s' % (request_data['username'], request_data['password'])
		response_data['error_code'] = 0
		response_data['error_message'] = 'Ok'
	else:
		response_data['error_code'] = 3
		response_data['error_message'] = 'Only POST is allowed!'
	return HttpResponse(json.dumps(response_data), content_type="application/json")


def profile(request):
	return HttpResponse("user profile")

def upload_profile_icon(request):
	return HttpResponse("upload profile icon")