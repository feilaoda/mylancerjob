def parse_product(x, item):

    names = x.select('//meta[@property="og:title"]/@content').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//div[@class="contentLeft"]/div/h2[@class="product-name item"]/span/text()').extract()
        if names:
            item['scrap_pn'] = names[0].strip()
        else:
            names = x.select('//h2[@class="collection-name"]/span[@itemprop="name"]/text()').extract()
            if names:
                item['scrap_pn'] = names[0].strip()
    return item


parsers = {
    'product': parse_product,
    'cp1': parse_seo_h1,
    'cp2': parse_seo_h1,
    'browse1': parse_seo_h1_or_SRNode_selected,
    'browse2': parse_seo_h1_or_SRNode_selected,
    'browse3': parse_seo_h1_or_SRNode_selected,
    'search_browse': parse_prodInfoBox,
    'search': parse_prodInfoBox,    
    }