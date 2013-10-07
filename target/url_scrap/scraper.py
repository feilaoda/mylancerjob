'''
Created on Sep 7, 2013

@author: ariek
'''

from scrapy.item import Item, Field
from scrapy.selector.lxmlsel import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http.request import Request
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from twisted.internet import reactor
import walmart, sears

settings = {
    'BOT_NAME' : 'pscrawler',
    'DOWNLOAD_TIMEOUT' : 10,
    'USER_AGENT' : 'crawler (+http://www.purchasesciences.com)'
}

class UrlItem(Item):
    attach = Field()
    url = Field()
    scrap_parser = Field()
    scrap_pn = Field()
    scrap_pid = Field()
    
class Spider(BaseSpider):
    name = "psspider"
    
    def parse(self, response):
        x = HtmlXPathSelector(response)
        item = UrlItem()
        item['url'] = response.url       
        item['attach'] = response.meta['attach']     
        item['scrap_parser'] = response.meta['parser_name']
        parser = response.meta['parser']
        parser(x, item)
        return item


def scrap(requests, item_scraped_callback=None, loglevel=log.WARNING):
    spider = Spider()
    crawler = Crawler(Settings(settings))
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    if item_scraped_callback: crawler.signals.connect(item_scraped_callback, signal=signals.item_scraped)
    crawler.configure()
    crawler.crawl(spider, requests)
    crawler.start()
    log.start(loglevel = loglevel, crawler = crawler, logstdout = False)
    reactor.run() 
    # the script will block here until the spider_closed signal was sent

def request(url, parser, attach):
    r = Request(url=url)
    r.meta['parser'] = parser
    r.meta['parser_name'] = parser.__name__
    r.meta['attach'] = attach
    return r

if __name__ == "__main__":
    pass
   
    requests = (request("http://www.walmart.com/browse/computers/laptop-computers/toshiba/3944_3951_132960/YnJhbmQ6VG9zaGliiYQieie", walmart.parse_seo_h1_or_SRNode_selected, None),
                request("http://www.walmart.com/search/browse-ng.do?facet=category%3ACharcoal+Grills", walmart.parse_prodInfoBox, None),
                request("http://www.walmart.com/ip/10416694", walmart.parse_prodInfoBox, None))
    scrap(requests, None, loglevel=log.DEBUG)
