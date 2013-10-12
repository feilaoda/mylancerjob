'''
Created on Sep 11, 2013

@author: ariek
'''
import unittest
from scrapy.http import TextResponse
from scrapy.selector.lxmlsel import HtmlXPathSelector
from scraper import UrlItem

class Test(unittest.TestCase):

    def do_test(self, parser, html, pn):
        try:
            x = HtmlXPathSelector(TextResponse('url', body=html))
            item = parser(x, UrlItem())
            self.assertEquals(pn, item['scrap_pn'])
        except:
            print 'error in parser: ' + str(parser)
            print html
            raise

    def do_tests(self, examples):
        [self.do_test(e[0], e[1]['html'], e[1]['pn']) for e in examples]
        
    def test_domain(self):
        domain = 'target'
        mod = __import__(domain, globals(), locals(), ['*'], -1)
    
        examples = mod.__dict__.get('examples')
        if not examples: return True
        
        self.do_tests(examples)
               
if __name__ == "__main__":
    unittest.main()
    
