# -*- coding: utf-8 -*-

def parse_list(x, item):
    names = x.select('//span[@class="productTitle"]/a/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//span[@class="compare-disabled screen-reader-only"]/text()').extract()
        if names:
            item['scrap_pn'] = names[0].strip()
        else:
            names = x.select('//span[@class="hl_prodtitle"]/a/@title').extract()
            if names:
                item['scrap_pn'] = names[0].strip()

    return item


parsers = {
    'c_list': parse_list,
    'sb_list': parse_list,
    'search': parse_list,
    's_search': parse_list
}


examples = [
    #parse //span[@class="productTitle"]/a/text()
    [parse_list,
    {
    'url' : 'http://www.target.com/c/disney-princess-favorite-characters/-/N-5tdvs',
    'html' : '''
        <span class="productTitle">
    <a href='http://www.target.com/p/disney-princess-gift-day-cinder/-/A-13422958#prodSlot=medium_1_1' title="Disney Princess Gift Day Cinder" id='prodTitle-medium-1-1' class='productClick'>Disney Princess Gift Day Cinder</a>
        ''',
    'pn' : "Disney Princess Gift Day Cinder"
    }],

    #parse //span[@class="compare-disabled screen-reader-only"]/text()
    [parse_list,
    {
    'url' : 'http://www.target.com/c/1-maxi-dresses-skirts-women-s-ways-to-shop/-/N-55tup',
    'html' : '''
        <span class="compare-disabled screen-reader-only">  Mossimo Supply Co. Juniors High Low Racerback Tank - Assorted Colors</span>
        ''',
    'pn' : "Mossimo Supply Co. Juniors High Low Racerback Tank - Assorted Colors"
    }],


    #parse //span[@class="hl_prodtitle"]/a/@title
    [parse_list,
    {
    'url': 'http://www.target.com/c/infant-car-seats-baby/-/N-5q0ev#?lnk=gnav_baby_3_20&intc=736562|null',
    'html': '''
    <span class="hl_prodtitle"><a href="http://www.hlserve.com/Delivery/Delivery.aspx?hm_CID=131&amp;hm_PN=TaxonomyProductAd_Click&amp;hm_guid=948e9e07-8e11-497e-8221-33e939f83285&amp;hm_evals=ZYvdBO7dTtjD6KbiKZbDiIPQ6ctIU9SMmiQNNjXEboEjDaOTV0eHhxjWZf1RYsIWgxU3C0vKLbMWmowi7MZiKZBlQ2tElOE3qR/G3IpjB/SGhfSli5DMx+wqUYhB9/YAKU0ImF/+fS8AxIqErFAFh3IeXHW6SCY7iK1Leedf559fZHySVjyQp/WCNk/zUZjQY+xHai3O1N2yhYpAalPY9TTy4H1nQEYzBk0YvRi/Cx+SyrtVip2fMyYaP67dWnfegOeK0ns67N8CtI/WrxXBoIPMNZ5HcZTjxv/p7aqS8GyY7t0bc0RW7M4CRmDEWO1A98Bu8jEle6gP/5w+CMxWGVwbWXwln5oZwuij31RGsqg3oU3MEXnJVcRdZYL1G+ceUAAwXdNbfCPtOpTyEEFirZt1+NZ/uSs2AsisUi9y0aJ+XAOzsHr+z1UPlufCyuWlrU+1Gtm9JX5UnEPbzekSwdeY9mEhe7mkez2sHpvYI2BBto90i4MRU6LREqoLY3a9Ifm2ohtzczkQIpuGkjQi8UPVgCg3bOBQITF7gEItpnd6tOX6K/JGl+u/hg+ITF3QwdeEj83X09TrwqMQ1TAkJdEJ9jR6dRadg/VDPFtrEccNsyGiyITZY+v1LmeSDqkA88vUoYoYiL4/UyTNBw+DjHkQHg0PtM8mwJZurf2HbgTYglew0FyuuQ==&amp;hmClckThru=www.target.com%2fp%2fgraco-smartseat-all-in-one-car-seat-rosin%2f-%2fA-13516953%3Fintc%3D8675309_hl13516953_null%26lnk%3Dother_plp_hl_tl_x1y3" title="Graco SmartSeat All in One Car Seat - Rosin">Graco SmartSeat All in One Car Seat...</a></span>
    ''',
    'pn': "Graco SmartSeat All in One Car Seat - Rosin"
    }]

]