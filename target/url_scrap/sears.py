def parse_cardProdTitle_or_gr_name(x, item):
    names = x.select('//div[@class="cardProdTitle"]/h2/a/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//div[@property="gr:name"]/@content').extract()   
        if names:
            item['scrap_pn'] = names[0].strip()       
        
    return item

def parse_col_2(x, item):
    names = x.select('//div[@class="col_2"]/h1/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
        
    return item


parsers = {
    'shc_product': parse_cardProdTitle_or_gr_name,
    'shc_search': parse_cardProdTitle_or_gr_name,
    'search': parse_cardProdTitle_or_gr_name,
    'shc_list2': parse_cardProdTitle_or_gr_name,
    'list': parse_cardProdTitle_or_gr_name,
    'search_only': parse_cardProdTitle_or_gr_name,
    'shc_search_only': parse_cardProdTitle_or_gr_name,
    'shc_list': parse_col_2,    
          }

examples = [


[parse_cardProdTitle_or_gr_name,
{
'url' : 'http://www.sears.com/shc/s/p_10153_12605_00624975000P',
'html' : '''
    <div property="gr:name" content="NordicTrack T5.5 Treadmill" xml:lang="en"></div>
         
    ''',
'pn' : 'NordicTrack T5.5 Treadmill'
}],

[parse_cardProdTitle_or_gr_name,
{
'url' : 'http://www.sears.com/search=ge%20washing%20machines%20on%20sale?storeId=10153&levels=Appliances_Accessories_Washer+%26+Dryers',
'html' : '''
        <div class="cardProdTitle">			
				<h2 itemprop="name">				
							<a href="/by-ge-washing-machine-lid-switch-assembly/p-SPM1611976414?prdNo=1" title="By GE GE Washing Machine Lid Switch Assembly WH12X10334" onclick="javascript:appendOmParams(this, 'SPM1611976414');">By GE GE Washing Machine Lid Switch Assembly WH12X10334</a>						
				</h2>				
			</div>
         
         
    ''',
'pn' : 'By GE GE Washing Machine Lid Switch Assembly WH12X10334'
}],

[parse_col_2,
{
'url' : 'http://www.sears.com/appliances-washers/b-1101269',
'html' : '''
<div class="col_2">		
				<div id="redir"></div>
		  		<script type="text/javascript" language="JavaScript" src="http://c.shld.net/09232200/shared/js/categoryPageBannerMessage.js"></script>  		
		<h1>Washers</h1>
         
    ''',
'pn' : 'Washers'
}],

]


