import base64
import json
import time
from urllib import request, parse

class Twitter():
	def get_retweeters(token, tweet_id, cursor=-1, count=100, stringify_ids=True):
		url = 'https://api.twitter.com/1.1/statuses/retweeters/ids.json'

		headers = {
			'Authorization': 'Bearer {}'.format(token),
		}
		params = parse.urlencode({
			'id': tweet_id,
			'cursor': cursor,
			'count': count,
			'stringify_ids': 'true' if stringify_ids else 'false'
		})

		req = request.Request('{}?{}'.format(url, params), headers=headers)

		try:
			res = request.urlopen(req)
		except Exception as e:
			print(e)
			return None

		resjson = json.loads(res.read().decode('utf8'))
		return resjson, time.time()
