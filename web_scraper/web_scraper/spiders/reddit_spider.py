```python
import scrapy
from web_scraper.web_scraper.items import Item

class RedditSpider(scrapy.Spider):
    name = "reddit_spider"
    start_urls = ['http://www.reddit.com']

    def parse(self, response):
        for post in response.css('div.thing'):
            item = Item()
            item['title'] = post.css('p.title a::text').get()
            item['url'] = post.css('p.title a::attr(href)').get()
            item['author'] = post.css('a.author::text').get()
            item['timestamp'] = post.css('time::attr(datetime)').get()
            yield item

        next_page = response.css('span.next-button a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```