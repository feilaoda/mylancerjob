# -*- coding: utf-8 -*-

def parse_product(x, item):
    names = x.select('//meta[@property="og:title"]/@content').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//h2[@class="product-name item"]/span/text()').extract()
        if names:
            item['scrap_pn'] = names[0].strip()
        else:
            names = x.select('//h2[@class="collection-name"]/span[@itemprop="name"]/text()').extract()
            if names:
                item['scrap_pn'] = names[0].strip()
    return item

def parse_list(x, item):
    names = x.select('//span[@class="productTitle"]/a/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//span[@class="compare-disabled screen-reader-only"]/text()').extract()
        if names:
            item['scrap_pn'] = names[0].strip()
        else:
            names = x.select('//h2[@class="H_Gray_Med_Bold_36px_333333"]/text()').extract()
            if names:
                item['scrap_pn'] = names[0].strip()

    return item


parsers = {
    'product': parse_product,
    'c_list': parse_list,
    'sb_list': parse_list,
    'search': parse_list
}


examples = [

    [parse_product,
    {
    'url' : 'http://www.target.com/p/men-s-mossimo-supply-co-russom-boot-navy/-/A-14601296#prodSlot=large_1_2',
    'html' : '''
        <h2 class="product-name item">
                <span class="fn" itemprop="name">Men's Mossimo Supply Co. Russom Boot - Navy</span>
            </h2>
            
        ''',
    'pn' : "Men's Mossimo Supply Co. Russom Boot - Navy"
    }],

    [parse_product,
    {
    'url' : 'http://www.target.com/p/girls-knit-beanie-and-arm-warmer-set/-/A-14549375_201307091131',
    'html' : '''
        <meta property="og:title" content="Girls&#39; Knit Beanie and Arm Warmer Set"/>
        ''',
    'pn' : "Girls' Knit Beanie and Arm Warmer Set"
    }],

    [parse_list,
    {
    'url' : 'http://www.target.com/c/disney-princess-favorite-characters/-/N-5tdvs',
    'html' : '''
        <span class="productTitle">
    <a href='http://www.target.com/p/disney-princess-gift-day-cinder/-/A-13422958#prodSlot=medium_1_1' title="Disney Princess Gift Day Cinder" id='prodTitle-medium-1-1' class='productClick'>Disney Princess Gift Day Cinder</a>
        ''',
    'pn' : "Disney Princess Gift Day Cinder"
    }],

    [parse_list,
    {
    'url' : 'http://www.target.com/c/1-maxi-dresses-skirts-women-s-ways-to-shop/-/N-55tup',
    'html' : '''
        <span class="compare-disabled screen-reader-only">  Mossimo Supply Co. Juniors High Low Racerback Tank - Assorted Colors</span>
        ''',
    'pn' : "Mossimo Supply Co. Juniors High Low Racerback Tank - Assorted Colors"
    }],


]