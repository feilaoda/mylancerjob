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


parsers = {
    'product': parse_product,
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
'pn' : 'Men\'s Mossimo Supply Co. Russom Boot - Navy'
}],


[parse_product,
{
'url' : 'http://www.target.com/p/men-s-mossimo-supply-co-russom-boot-black/-/A-14601294#prodSlot=large_1_6',
'html' : '''
    <meta property="og:title" content="Men&#39;s Mossimo Supply Co. Russom Boot - Black"/>

    ''',
'pn' : "Men's Mossimo Supply Co. Russom Boot - Black"
}],

]