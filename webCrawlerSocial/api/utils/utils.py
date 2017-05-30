import base64
import json
import time
import os
from urllib import request, parse

def get_oauth_token(apikey, apisecret, url):
	bearer_token_credentials = '{}:{}'.format(apikey, apisecret)
	bearer_token_credentials_encoded = base64.b64encode(bearer_token_credentials.encode('utf8')).decode()

	headers = {
		'Authorization': 'Basic {}'.format(bearer_token_credentials_encoded),
		'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
	}
	data = parse.urlencode({
		'grant_type': 'client_credentials'
	}).encode()

	req = request.Request(url, headers=headers, data=data)

	try:
		res = request.urlopen(req)
	except Exception as e:
		print(e)
		return None

	resjson = json.loads(res.read().decode('utf8'))
	return resjson['access_token']

def output_json(data, file_basename):
	file_path = '../../output/api/{}_results_{}.json'.format(file_basename, time.strftime('%Y%m%d-%H%M%S'))
	with open(file_path, 'w') as outfile:
		json.dump(data, outfile)

def get_file_basename(file_path):
	return os.path.basename(file_path).split('.')[0]