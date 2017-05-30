from utils.utils import get_oauth_token, output_json, get_file_basename
from utils.api import Twitter
import sys
import os
import datetime
import time
import config

OAUTH_URL = 'https://api.twitter.com/oauth2/token'

class TwitterRetweeterFetcher():
	def __init__(self, tweet_id, fetch_interval=60, exec_time=600):
		"""
			tweet_id: the tweet to fetch
			fetch_interval (sec): time elapsed before calling API the next time
			exec_time (sec): total time to execute the fetcher
		"""
		self.tweet_id = tweet_id
		self.exec_time = exec_time
		self.fetch_interval = fetch_interval

	def get_retweeters_once(self, token=None):
		if token == None:
			token = get_oauth_token(config.TWITTER_API_KEY, config.TWITTER_API_SECRET, OAUTH_URL)
			if token == None:
				return None

		resjson, timestamp = Twitter.get_retweeters(token, self.tweet_id)
		data = {
			'timestamp': timestamp,
			'data': {
				'ids': resjson['ids']
			}
		}
		return data

	def get_retweeters(self):
		token = get_oauth_token(config.TWITTER_API_KEY, config.TWITTER_API_SECRET, OAUTH_URL)
		if token == None:
			return

		# create output directory
		dir_path = '../../output/api/{}'.format(time.strftime('%Y%m%d-%H%M%S'))
		os.makedirs(dir_path)

		# start fetching
		start_time = time.time()
		prev_time = start_time
		while prev_time - start_time <= self.exec_time: 
			# calculate elapsed time to decide whether to start fetch, or sleep
			now = time.time()
			elapsed = now - prev_time
			if prev_time != start_time and elapsed < self.fetch_interval:
				time.sleep(self.fetch_interval - elapsed)

			# retrieve data
			data = self.get_retweeters_once(token)
			prev_time = time.time()

			print(data)
			output_json(data, '{}-{}'.format(get_file_basename(__file__), self.tweet_id), dir_path)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage: python3 {} <tweet_id>'.format(__file__))
	else:
		fetcher = TwitterRetweeterFetcher(tweet_id=sys.argv[1])
		fetcher.get_retweeters()











