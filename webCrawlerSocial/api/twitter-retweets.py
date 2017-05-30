from utils.utils import get_oauth_token, output_json, get_file_basename
from utils.api import Twitter
import sys
import config

OAUTH_URL = 'https://api.twitter.com/oauth2/token'

def get_retweeters(tweet_id):
	token = get_oauth_token(config.TWITTER_API_KEY, config.TWITTER_API_SECRET, OAUTH_URL)
	if token == None:
		return

	resjson, timestamp = Twitter.get_retweeters(token, tweet_id)
	data = {
		'tweet_id': tweet_id,
		'timestamp': timestamp,
		'ids': resjson['ids']
	}
	output_json(data, '{}-{}'.format(get_file_basename(__file__), tweet_id))

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage: python3 {} <tweet_id>'.format(__file__))
	else:
		get_retweeters(sys.argv[1])