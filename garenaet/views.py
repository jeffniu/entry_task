import json
from django.http import HttpResponse
from models import TbUser
from models import TbToken
import hashlib
import uuid
from datetime import datetime, timedelta
# Create your views here.

def index(request):
    return HttpResponse("Hello, ET!")

def login(request):
	response_data = {}
	if request.method == 'POST':
		request_data = json.loads(request.body)
		username = request_data['username']
		password = request_data['password']
		if username and password:
			user_object = TbUser.objects.filter(username=username, pwd=password)
			print user_object
			users = user_object.values()
			if users:
				user = users[0]
				print user
				print 'id %s, username %s, password %s' % (str(user['id']), user['username'], user['pwd'])
				token = hashlib.sha256(str(uuid.uuid4())).hexdigest()
				t_data = TbToken(user=user_object[0], token=token)
				t_data.save()
				response_data['error_code'] = 0
				response_data['error_message'] = 'Ok'
				response_data['access_token'] = token
			else:
				response_data['error_code'] = 4
				response_data['error_message'] = 'Invalid Username or password'
		else:
			response_data['error_code'] = 2
			response_data['error_message'] = 'Username or password is empty'
	else:
		response_data['error_code'] = 3
		response_data['error_message'] = 'Only POST is allowed!'
	return HttpResponse(json.dumps(response_data), content_type="application/json")


def profile(request):
	response_data = {}
	if request.method == 'POST':
		request_data = json.loads(request.body)
		tokenStr = request_data['access_token']
		if isTokenValid(tokenStr):
			response_data['error_code'] = 0
			response_data['error_message'] = 'Ok'
			user = getUserFromToken(tokenStr)
			response_data['username'] = user.username
			response_data['nickname'] = user.nickname			
			response_data['icon_url'] = 'http://a.dryicons.com/images/icon_sets/travel_and_tourism_part_2/png/128x128/coffee.png'
		else:
			response_data['error_code'] = 2
			response_data['error_message'] = 'access token is invalid'
	else:
		response_data['error_code'] = 3
		response_data['error_message'] = 'Only POST is allowed!'

	return HttpResponse(json.dumps(response_data), content_type="application/json")

def upload_profile_icon(request):
	return HttpResponse("upload profile icon")

def update_nickname(request):
	response_data = {}
	if request.method == 'POST':
		request_data = json.loads(request.body)
		tokenStr = request_data['access_token']
		nickname = request_data['nickname']
		if isTokenValid(tokenStr):
			if nickname:
				user = getUserFromToken(tokenStr)
				user.nickname = nickname
				user.save()
				response_data['error_code'] = 0
				response_data['error_message'] = 'Ok'
			else:
				response_data['error_code'] = 4
				response_data['error_message'] = 'nickname can not be null'
		else:
			response_data['error_code'] = 2
			response_data['error_message'] = 'access token is invalid'
	else:
		response_data['error_code'] = 3
		response_data['error_message'] = 'Only POST is allowed!'

	return HttpResponse(json.dumps(response_data), content_type="application/json")


def isTokenValid(token):
	if not token:
		return False 
	tokenList = TbToken.objects.filter(token=token, creation_time__gte=datetime.now()-timedelta(minutes=30))
	return tokenList.count() > 0

def getUserFromToken(token):
	tokenList = TbToken.objects.filter(token=token, creation_time__gte=datetime.now()-timedelta(minutes=30))
	if tokenList.count() > 0:
		return tokenList[0].user
	else:
		return None

