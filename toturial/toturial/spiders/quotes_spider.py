import scrapy


class QuotesSpider(scrapy.Spider):
    # Using spider arguments
    name = 'quotes'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse())

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            # A shortcut for creating requests
            yield response.follow(next_page, callback=self.parse)



    # name = "quotes"
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    # ]
    #
    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first(),
    #             'tags': quote.css('div.tags a.tag::text').extract(),
    #         }
    #
    #     next_page = response.css('li.next a::attr(href)').extract_first()
    #     if next_page is not None:
    #         # next_page = response.urljoin(next_page)
    #         # yield scrapy.Request(next_page, callback=self.parse)
    #         # A shortcut for creating requests
    #         yield response.follow(next_page, callback=self.parse)
