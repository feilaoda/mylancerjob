def parse_ip2(x, item):
    names = x.select('//meta[@name="title"]/@content').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//h1[@class="productTitle"]/text()').extract()
        if names:
            item['scrap_pn'] = names[0].strip()
        else:
            names = x.select('//span[@id="SAC_prodName"]/text()').extract()
            if names:
                item['scrap_pn'] = names[0].strip()      
        
    return item

def parse_seo_h1(x, item):
    names = x.select('//li[@class="last"]/h1[@class="seo_h1"]/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
        
    return item

def parse_seo_h1_or_SRNode_selected(x, item):
    names = x.select('//li[@class="last"]/h1[@class="seo_h1"]/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//div[@class="SRNode_selected"]/text()').extract()
        if names:
            item['scrap_pn'] = names[0].strip()
        
    return item

def parse_prodInfoBox(x, item):
    names = x.select('//div[@class="prodInfoBox"]/a[contains(@class,"prodLink")]/@title').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
        
    return item


parsers = {
    'ip2': parse_ip2,
    'cp1': parse_seo_h1,
    'cp2': parse_seo_h1,
    'browse1': parse_seo_h1_or_SRNode_selected,
    'browse2': parse_seo_h1_or_SRNode_selected,
    'browse3': parse_seo_h1_or_SRNode_selected,
    'search_browse': parse_prodInfoBox,
    'search': parse_prodInfoBox,    
          }

examples = [


[parse_ip2,
{
'url' : 'http://www.walmart.com/ip/9863255',
'html' : '''
    <meta name="title" content="The Mask / Son Of The Mask Double Feature (Widescreen)"/>         
    ''',
'pn' : 'The Mask / Son Of The Mask Double Feature (Widescreen)'
}],

[parse_ip2,
{
'url' : 'http://www.walmart.com/ip/10416694',
'html' : '''
    <h1 class="productTitle" itemprop="name">Dr. Scholl's Ingrown Toenail Relief</h1>         
    ''',
'pn' : 'Dr. Scholl\'s Ingrown Toenail Relief'
}],

[parse_ip2,
{
'url' : 'http://www.walmart.com/ip/10416694',
'html' : '''
    <span id="SAC_prodName">
    Dr. Scholl's Ingrown Toenail Relief
    </span>         
    ''',
'pn' : 'Dr. Scholl\'s Ingrown Toenail Relief'
}],

[parse_seo_h1,
{
'url' : 'http://www.walmart.com/cp/cameras/133277?fromPageCatId=1058864',
'html' : '''
    <li class="last"><h1 class="seo_h1">Cameras & Camcorders</h1></li>         
    ''',
'pn' : 'Cameras & Camcorders'
}],

[parse_seo_h1_or_SRNode_selected,
{
'url' : 'http://www.walmart.com/browse/auto-electronics/auto-accessories/3944_3947_544376',
'html' : '''
    <li class="last"><h1 class="seo_h1">Auto Accessories</h1></li>         
    ''',
'pn' : 'Auto Accessories'
}],

[parse_seo_h1_or_SRNode_selected,
{
'url' : 'http://www.walmart.com/browse/computers/laptop-computers/toshiba/3944_3951_132960/YnJhbmQ6VG9zaGliiYQieie',
'html' : '''
    <div class="SRNode_selected">Laptop Computers</div>         
    ''',
'pn' : 'Laptop Computers'
}],

[parse_prodInfoBox,
{
'url' : 'http://www.walmart.com/search/browse-ng.do?facet=category%3ACharcoal+Grills',
'html' : '''
    <div class="prodInfoBox">
<a class="prodLink GridItemLink" href="/ip/Backyard-Grill-22-Kettle-Charcoal-Grill/22018222"
onclick="javascript: trackProductClickOmniture('false','yes','',
'22018222','0','true',
'1','32','1','',
'32');" title="Backyard Grill 22" Kettle Charcoal Grill">Backyard Grill 22" Kettle Charcoal Grill</a>         
    ''',
'pn' : 'Backyard Grill 22'
}],

[parse_prodInfoBox,
{
'url' : 'http://www.walmart.com/search/search-ng.do?search_query=floor+lamp&facet=price%3a%2420+-+%2450',
'html' : '''
    <div class="prodInfoBox">
<a class="prodLink GridItemLink" href="/ip/Mainstays-Etagere-Floor-Lamp/11089113"
onclick="javascript: trackProductClickOmniture('false','yes','',
'11089113','0','true',
'1','16','1','',
'16');" title="Mainstays Etagere Floor Lamp">Mainstays Etagere <span class=highlight>Floor</span> <span class=highlight>Lamp</span></a>         
    ''',
'pn' : 'Mainstays Etagere Floor Lamp'
}],

]




