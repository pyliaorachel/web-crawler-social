# -*- coding: utf-8 -*-
import scrapy
import config

level = 3

class TwitterFollowersSpider(scrapy.Spider):
    name = "twitter-followers"
    allowed_domains = ["twitter.com"]
    start_urls = ['https://twitter.com/login']

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
            url='https://twitter.com/followers',
            callback=self.parse_followers
        )

    def parse_followers(self, response):
        print('name = {}'.format(response.css('h1.ProfileHeaderCard-name a ::text').extract_first().encode('utf-8')))

        global level
        if level > 0:
            level -= 1
            follower_pages = response.css('.ProfileCard-userFields a.fullname ::attr(href)').extract()
            for follower_page in follower_pages:
                yield scrapy.Request(response.urljoin('{}/followers'.format(follower_page)), callback=self.parse_followers)