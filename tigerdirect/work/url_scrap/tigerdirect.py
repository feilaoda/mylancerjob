# -*- coding: utf-8 -*-

def parse_product(x, item):
    names = x.select('//div[@class="prodName"]/h1/text()').extract()   
    if names:
        item['scrap_pn'] = names[-1].strip()
    else:
        names = x.select('//a/strong[@class="iuc-item-name"]/text()').extract()
        if names:
            item['scrap_pn'] = names[-1].strip()

    return item



def parse_product_list(x, item):
    names = x.select('//div[@class="productInfo"]/h3/a/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//table[@class="font_size2"]/tr/td/a/b/text()').extract()   
        if names:
            item['scrap_pn'] = names[0].strip()
        
                

    return item

 


parsers = {
    'product': parse_product,
    'upsell_product': parse_product,
    'category_list': parse_product_list,
    'category_slc_list': parse_product_list,
    'search_list': parse_product_list,
    'index_list': parse_product_list,
    'index1_list': parse_product_list
}


examples = [

    [parse_product,
    {
        'url' : 'http://www.tigerdirect.com/applications/Searchtools/item-details.asp?EdpNo=2416662&amp;amp;Sku=K24-2107&amp;amp;SRCCODE=MDOTTD&amp;amp;MobileOptOut=1',
        'html' : '''
            <div class="prodName">
                <h1>Kingston SH103S3/120G HyperX 120GB Solid State Drive - 120GB, SATA III, 2.5</h1>
                <span class="sku"><strong>Item#:</strong>&nbsp;K24-2107
                     &nbsp;|&nbsp;
                        <strong>Model#:</strong>&nbsp;SH103S3/120G</span>
            </div>
            ''',
        'pn' : "Kingston SH103S3/120G HyperX 120GB Solid State Drive - 120GB, SATA III, 2.5"
    }],


    [parse_product,
    {
        'url' : 'http://www.tigerdirect.com/applications/searchtools/item_upsell.asp?EdpNo=2951127&amp;amp;msg=',
        'html' : '''
            <div class="iuc-item-hdr">
            <a href="/applications/searchtools/item-details.asp?EdpNo=2688070&amp;csid=_32">
            <img name="imgLarger" class="iuc-item-thumb" src="http://images.highspeedbackbone.net/SkuImages/large/N100-3050-main02-tmc.jpg" border="0" alt="">
            <strong class="iuc-item-name">Netgear 1750 Mbps R6300 Wirelss 802.11AC Router </strong></a></div>

            ''',
        'pn' : "Netgear 1750 Mbps R6300 Wirelss 802.11AC Router"
    }],

    [parse_product_list,
    {
        'url' : 'http://www.tigerdirect.com/applications/Category/guidedSearch.asp?CatId=10',
        'html' : '''
            <div class="productInfo"><h3 class="itemName"><a href="../SearchTools/item-details.asp?EdpNo=3683258&amp;Sku=K24-2220" title="Kingston HyperX Blu 16GB Desktop Memory Kit">Kingston HyperX Blu 16GB Desktop Memory Kit</a></h3></div>

            ''',
        'pn' : "Kingston HyperX Blu 16GB Desktop Memory Kit"
    }],

    [parse_product_list,
    {
        'url' : 'http://www.tigerdirect.com/applications/Overstock/overstock_slc.asp?CatId=1736&amp;amp;category=Mobile%20Accessories',
        'html' : '''
            <table width="100%" border="0" cellspacing="0" cellpadding="0" class="font_size2">
                <tr>
                  <td><a href="/applications/SearchTools/item-details.asp?EdpNo=5501901&amp;CatId=5793" class="info"><b>RIM 8300 Blue Rubberized Skin</b></a></td>
                  <td>&nbsp;</td>
                </tr>
                <tr>
                  <td>Count on durable protection for your cell phone with RIM, the leading manufacturer of wireless solutions and maker of Blackberry.</td>
                  <td width="20">&nbsp;</td>
                </tr>
                <tr>
                  <td colspan="2" height="10"><img src="http://images.highspeedbackbone.net/misc/pixel-clr.gif" width="1" height="10"></td>
                </tr>
           </table>
            ''',
        'pn' : "RIM 8300 Blue Rubberized Skin"
    }],


   
    

]