## Libraries

* [Scrapy](https://scrapy.org/)
* [Selenium](http://selenium-python.readthedocs.io/index.html)
* [geckodriver (driver engine for Firefox)](https://github.com/mozilla/geckodriver)

```
pip install scrapy
pip install selenium
brew install geckodriver
```

Make sure you have the latest Firefox browser.

## Usage

- General
	1. Write your configuration info e.g. account, into a new file `webCrawlerSocial/spiders/config.py`
		- See `webCrawlerSocial/spiders/config.py.template` for available configurations
	2. Run `scrapy crawl <spider name>`
		- Run `scrapy list` for available spiders

- Twitter
	- Followers
		1. Write your twitter account info into `webCrawlerSocial/spiders/config.py`:
			```
			TWITTER_USERNAME = 'your-username'
			TWITTER_PASSWORD = 'your-password'
			```

		2. Run `scrapy crawl twitter-followers`
		3. See output in `output/twitter-retweets_results_<timestamp>.json`
		4. Modified `level` global variable in `webCrawlerSocial/spiders/twitter_followers.py` for deeper level follower crawling
	
	- Retweet Users
		- Crawler
			1. Write your twitter account info into `webCrawlerSocial/spiders/config.py`:
				```
				TWITTER_USERNAME = 'your-username'
				TWITTER_PASSWORD = 'your-password'
				```

			2. Run `scrapy crawl twitter-retweets`
			3. See output in `output/twitter-retweets_results_<timestamp>.json`
		- API
			1. Goto [Twitter Developers - Application Management](https://apps.twitter.com/), create an app, get the API key & secret
			2. Write your twitter API info into `webCrawlerSocial/api/config.py`:
				```
				TWITTER_API_KEY = 'your-api-key'
				TWITTER_API_SECRET = 'your-api-secret'
				```
			3. `cd webCrawlerSocial/api`, run `python3 twitter-retweets.py <tweet-id>`
				- It requests data from the API every 1 minute and runs for a default of 10 minutes
			4. See output in `output/api/<timestamp>/twitter-retweets_results_<timestamp>.json`
			5. Aggregate results
				- 1 output file above represents the results of 1 request; to aggregate the results for the entire execution, `cd tools` and run `python3 aggregator.py`
				- See output in `output/api/<timestamp>/twitter-retweets_all.json`












