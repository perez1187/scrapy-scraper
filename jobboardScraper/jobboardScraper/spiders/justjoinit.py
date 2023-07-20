import scrapy
from scrapy_playwright.page import PageMethod
from urllib.parse import urlencode
from scraper_api import ScraperAPIClient
from scrapfly import ScrapflyClient, ScrapeConfig

scrapfly=ScrapflyClient(key="")

API_KEY = '5376c38e-a6a8-406f-a398-02cf1f56d8df'
client = ScraperAPIClient(API_KEY)   

# for url endpoint
# this func get url of the site that we want scrape
# and send to api endpioint
def get_proxy_url(url):
    payload = {'api_key':API_KEY, 'url':url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class JustjoinitSpider(scrapy.Spider):
    name = "justjoinit"
    # allowed_domains = ["https://shoppable-campaign-demo.netlify.app/#/", "proxy.scrapeops.io"]
    # start_urls = ["https://shoppable-campaign-demo.netlify.app/#/"]

    def start_requests(self):
        test_url = 'https://shoppable-campaign-demo.netlify.app/#/'
        # test_url = 'http://quotes.toscrape.com/js/'
        yield scrapy.Request(
            # test_url, 
            # url = get_proxy_url(test_url),
            client.scrapyGet(url=test_url),
            callback=self.parse,
            # meta={'playwright':True}
            meta = {
                "playwright" : True,
                "playwright_include_page" : True,
                "playwright_page_methods" : [
                    PageMethod("wait_for_selector",'.card-body')
                ],
                'errback' :self.errback,
            },
            )
    def parse(self, response):
        # for quote in response.css('div.quote'):
        yield{
            'text':response.text
        }

    def parse(self, response):
        yield {
            'text':response.text
        }
    # def parse(self, response):
        
    #     products = response.xpath('//*[@class="card-body"]')
    #     for product in products:
    #         yield {
    #         'title':product.xpath('.//*[@class="card-title"]/text()').get()
          
    #         }
    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
