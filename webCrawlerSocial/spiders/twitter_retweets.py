# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import time
import config

class TwitterRetweetsSpider(scrapy.Spider):
    name = "twitter-retweets"
    allowed_domains = ["twitter.com"]
    start_urls = ['https://twitter.com/login']

    def __init__(self, username='realDonaldTrump', num_of_tweets=1, *args,**kwargs):
        super(TwitterRetweetsSpider, self).__init__(*args, **kwargs)
        self.username = username
        self.num_of_tweets = num_of_tweets

        firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
        firefox_capabilities['marionette'] = True
        firefox_options = Options()
        firefox_options.add_argument('--connect-existing')
        self.driver = webdriver.Firefox(capabilities=firefox_capabilities, firefox_options=firefox_options)

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formcss='.signin',
            formdata={'session[username_or_email]': config.TWITTER_USERNAME, 'session[password]': config.TWITTER_PASSWORD},
            callback=self.after_login
        )

    def after_login(self, response):
        if 'authentication failed' in response.body:
            self.logger.error('Login failed')
            return

        return scrapy.Request(
            url='https://twitter.com/{}'.format(self.username),
            callback=self.parse_timeline
        )

    def parse_timeline(self, response):
        links_to_tweets = response.css('ol.stream-items li div.tweet::attr(data-permalink-path)').extract()[:self.num_of_tweets]

        for link_to_tweet in links_to_tweets:
            yield scrapy.Request(url='https://twitter.com{}'.format(link_to_tweet), callback=self.parse_tweet)

    def parse_tweet(self, response):
        num_of_retweets = response.css('li.js-stat-retweets.stat-count a::attr(data-tweet-stat-count)').extract_first()
        print('num_of_retweets: {}'.format(num_of_retweets))

        # press retweet button to open popup
        self.driver.get(response.url)
        #print self.driver.page_source.encode('utf-8')
        self.driver.find_element_by_css_selector('li.js-stat-retweets.stat-count a.request-retweeted-popup').click()
        time.sleep(1)

        users = response.css('ol.activity-popup-users li::attr(data-item-id)').extract()
        print('users {}'.format(response.css('ol.activity-popup-users').extract()))

    def closed(self, spider):
        self.driver.close()

