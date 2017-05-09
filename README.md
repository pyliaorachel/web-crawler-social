## Libraries

* [Scrapy](https://scrapy.org/)

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
		3. Modified `level` global variable in `webCrawlerSocial/spiders/twitter_followers.py` for deeper level follower crawling


