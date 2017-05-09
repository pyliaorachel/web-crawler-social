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
		1. Write your twitter account info into `webCrawlerSocial/spiders/config.py`:
			```
			TWITTER_USERNAME = 'your-username'
			TWITTER_PASSWORD = 'your-password'
			```

		2. Run `scrapy crawl twitter-retweets`
		3. See output in `output/twitter-retweets_results_<timestamp>.json`

