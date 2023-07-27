```python
import scrapy

class RedditItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    timestamp = scrapy.Field()
```