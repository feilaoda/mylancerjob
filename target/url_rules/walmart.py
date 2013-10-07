def match(url):
    return url.hostname.endswith('walmart.com')

rules = [

    {'name'    : 'irrelevant_domain',
     'hpattern': '(answers|avocado|brands|careers|challenge|classrings|corporate|delivery|download|familyjewelry|foundation|getegiftcard|giftcardreload|health|help|instoresnow|jobs|linksynergy|liquidations|localad|medicationfinder|mobile|mp3|news|personalizeditems|photo|pin|reviews|see|soundcheck|stock|survey|tracking|walmarttalent|wireless|wm|wwwndc)',
     'action'  : 'irrelevant'},	                   

    {'name'    : 'search_browse',
     'pattern' : 'browse-ng.do',
     'action'  : 'list',
     'norm'    : 'http://www.walmart.com/search/browse-ng.do?facet={facet}'},  
	 
    {'name'    : 'search',
     'pattern' : 'search-ng.do',
     'action'  : 'list',
     'norm'    : 'http://www.walmart.com/search/search-ng.do?search_query={search}&facet={facet}'},

	 # 'ip1' rule must apear before 'ip2' rule so it won't be overridden	
    {'name'    : 'ip1',
     'pattern' : 'ip/(?P<pn>.*?)/(?P<pid>.*?)([#?]|$)',
     'action'  : 'product',
     'norm'    : 'http://www.walmart.com/ip/{pn}/{pid}'},                    

    {'name'    : 'ip2',
     'pattern' : 'ip/(?P<pid>.*?)([#?]|$)',
     'action'  : 'product',
     'norm'    : 'http://www.walmart.com/ip/{pid}'},                    

	 # 'cp1' rule must apear before 'cp2' rule so it won't be overridden
    {'name'    : 'cp1',
     'pattern' : 'cp/(?P<c2>.*?)/(?P<c2id>.*?)([#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.walmart.com/cp/{c2}/{c2id}'},                    

    {'name'    : 'cp2',
     'pattern' : 'cp/(?P<c2id>.*?)([#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.walmart.com/cp/{c2id}'},      
	 
	 # browse rules must be in this order (3, 2, 1)
    {'name'    : 'browse3',
     'pattern' : 'browse/(?P<c1>.*?)/(?P<c2>.*?)/(?P<c3>.*?)/(?P<c2id>.*?)/(?P<words>.*?)([#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.walmart.com/browse/{c1}/{c2}/{c3}/{c2id}/{words}'},      	               

    {'name'    : 'browse2',
     'pattern' : 'browse/(?P<c1>.*?)/(?P<c2>.*?)/(?P<c2id>.*?)/([#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.walmart.com/browse/{c1}/{c2}/{c2id}/'},      	               

    {'name'    : 'browse1',
     'pattern' : 'browse/(?P<c1>.*?)/(?P<c1id>.*?)/([#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.walmart.com/browse/{c1}/{c1id}/?facet={facet}'},      	               

    {'name'    : 'storeLocator',
     'pattern' : '^/storeLocator',
     'action'  : 'store_locator'},	

    {'name'    : 'checkout2',
     'spattern' : 'https',
     'pattern' : '^/(wmflows|subflow)/checkout',
     'action'  : 'checkout',
     'norm'    : 'https://www.walmart.com/wmflows/checkout'},

	 # 'checkout1' rule must apear before 'cart' rule so it won't be overridden
    {'name'    : 'checkout1',
     'spattern' : 'https',
     'pattern' : '^/cart.*#gberr',
     'action'  : 'checkout',
     'norm'    : 'https://www.walmart.com/cart2/cart.do#gberr'},
	 
    {'name'    : 'cart',
     'spattern' : 'https',
     'pattern' : '^/cart',
     'action'  : 'view cart',
     'norm'    : 'https://www.walmart.com/cart2/cart.do'},

    {'name'    : 'thankyouPrintable',
    'spattern' : 'https',
     'pattern' : '^/.*/thankyouPrintable',
     'action'  : 'purchase'},

    {'name'    : 'printerFriendlyThankyou',
     'spattern' : 'https',
     'pattern' : '^/printerFriendlyThankyou',
     'action'  : 'purchase'},

	## Must appear last, since this rule can override others
    {'name'    : 'irrelevant',
     'pattern' : '^/(cservice|pharmacy|giftregistry|catalog)',
     'action'  : 'irrelevant'}, 
]

params = [
    {'qpattern': 'search_query=(?P<search>.*?)([&]|$)'},     
    {'qpattern': 'facet=(?P<facet>.*?)([&]|$)'},     
    {'qpattern': 'sfsearch_zip=(?P<location>.*?)([&]|$)'},     
]

examples = [
            
 ['http://www.walmart.com/search/browse-ng.do?_refineresult=true&amp;amp;povid=cat1070145-env172199-moduleA080112-lLinkGNAV_Electronics_Electronics_GPS_Navigation&amp;amp;facet=brand%3AGarmin&amp;amp;cat_id=3944&amp;amp;fromPageCatId=538883',
  {'norm': 'http://www.walmart.com/search/browse-ng.do?facet=brand%3AGarmin', 'action': 'list', 'facet': 'brand%3AGarmin', 'rule': 'search_browse'}],

 ['http://www.walmart.com/search/search-ng.do?Find=Find&amp;amp;_refineresult=true&amp;amp;cdnHost=search-cdn.walmart.com&amp;amp;ic=16_0&amp;amp;indexId=13d87925f5fc&amp;amp;search_constraint=0&amp;amp;search_query=windows+7+computers&amp;amp;searchdropdowndiv=com.wm.module.305715.constraint&amp;amp;facet=brand%3AHP',
  {'norm': 'http://www.walmart.com/search/search-ng.do?search_query=windows+7+computers&facet=brand%3AHP', 'action': 'list', 'search': 'windows+7+computers', 'facet': 'brand%3AHP', 'rule': 'search'}],
 
 ['http://www.walmart.com/search/search-ng.do?tab_value=all&search_query=floor+lamp&search_constraint=4044&Find=Find&cat_id=4044&facet=price%3a%2420+-+%2450&pref_store=5129&ss=false&ic=16_32&_be_related=2',
  {'norm': 'http://www.walmart.com/search/search-ng.do?search_query=floor+lamp&facet=price%3a%2420+-+%2450', 'action': 'list', 'search': 'floor+lamp', 'facet': 'price%3a%2420+-+%2450', 'rule': 'search'}],

 ['http://www.walmart.com/ip/Dyson-DC24-Animal-Ultra-Lightweight-Bagless-Upright-Vacuum-Cleaner/15173329?wmlspartner=HBLvzQS2RdU&amp;amp;sourceid=00051088942570117644&amp;amp;affillinktype=3&amp;amp;veh=aff',
  {'norm': 'http://www.walmart.com/ip/Dyson-DC24-Animal-Ultra-Lightweight-Bagless-Upright-Vacuum-Cleaner/15173329', 'action': 'product', 'pn': 'Dyson-DC24-Animal-Ultra-Lightweight-Bagless-Upright-Vacuum-Cleaner', 'pid': '15173329', 'rule': 'ip1'}],
 
 ['http://www.walmart.com/ip/10824234?wmlspartner=wlpa&amp;amp;adid=22222222227008990994&amp;amp;wl0=&amp;amp;wl1=g&amp;amp;wl2=&amp;amp;wl3=13222930270&amp;amp;wl4=&amp;amp;wl5=pla&amp;amp;veh=sem',
  {'norm': 'http://www.walmart.com/ip/10824234', 'action': 'product', 'pid': '10824234', 'rule': 'ip2'}],

 ['http://www.walmart.com/cp/iPad-eReaders-Tablets/1078524?povid=P1262-C1110.2784+1455.2776+1115.2956-L21',
  {'norm': 'http://www.walmart.com/cp/iPad-eReaders-Tablets/1078524', 'action': 'list', 'c2': 'iPad-eReaders-Tablets', 'c2id': '1078524', 'rule': 'cp1'}],
 
 ['http://www.walmart.com/cp/584291?adid=77777777924000003351&amp;amp;wmlspartner=PSComarketing_EveryLittleStep&amp;amp;veh=sem',
  {'norm': 'http://www.walmart.com/cp/584291', 'action': 'list', 'c2id': '584291', 'rule': 'cp2'}],

 ['http://www.walmart.com/browse/apparel/5438/?tab_value=all&amp;amp;search_sort=6&amp;amp;cat_id=5438&amp;amp;facet=category%3aCapri+Pants%7c%7ccategory%3aShorts%7c%7capparel_category%3aWomen%7c%7capparel_category%3aWomen%27s+Plus&amp;amp;pref_store=1307&amp;amp;ss=false&amp;amp;ic=32_32',
  {'norm': 'http://www.walmart.com/browse/apparel/5438/?facet=category%3aCapri+Pants%7c%7ccategory%3aShorts%7c%7capparel_category%3aWomen%7c%7capparel_category%3aWomen%27s+Plus', 'action': 'list', 'c1': 'apparel', 'c1id': '5438', 'facet': 'category%3aCapri+Pants%7c%7ccategory%3aShorts%7c%7capparel_category%3aWomen%7c%7capparel_category%3aWomen%27s+Plus', 'rule': 'browse1'}],
 
 ['http://www.walmart.com/browse/electronics/scanners/3944_3951_37807_4439/?tab_value=all&amp;amp;pref_store=1576&amp;amp;ss=false&amp;amp;ic=32_0',
  {'norm': 'http://www.walmart.com/browse/electronics/scanners/3944_3951_37807_4439/', 'action': 'list', 'c1': 'electronics', 'c2': 'scanners', 'c2id': '3944_3951_37807_4439', 'rule': 'browse2'}],

 ['http://www.walmart.com/browse/ipad-ereaders/tablet-pcs/apple/3944_1078524_1078084/YnJhbmQ6QXBwbGUie?_refineresult=true&amp;amp;povid=cat1078524-env441856-module506921-lLink18',
  {'norm': 'http://www.walmart.com/browse/ipad-ereaders/tablet-pcs/apple/3944_1078524_1078084/YnJhbmQ6QXBwbGUie', 'action': 'list', 'c1': 'ipad-ereaders', 'c2': 'tablet-pcs', 'c3': 'apple', 'c2id': '3944_1078524_1078084', 'words': 'YnJhbmQ6QXBwbGUie', 'rule': 'browse3'}],

 ['http://www.walmart.com/browse/ipad-ereaders/tablet-pcs/apple/3944_1078524_1078084/',
  {'norm': 'http://www.walmart.com/browse/ipad-ereaders/tablet-pcs/apple/3944_1078524_1078084/', 'action': 'list', 'c1': 'ipad-ereaders', 'c2': 'tablet-pcs', 'c3': 'apple', 'c2id': '3944_1078524_1078084', 'words': '', 'rule': 'browse3'}],

 ['http://www.walmart.com/storeLocator/ca_storefinder_details_short.do?sfsearch_zip=19310&amp;amp;rx_dest=%2Findex.gsp&amp;amp;rx_title=com.wm.www.apps.storelocator.page.serviceLink.title.default&amp;amp;sfsearch_city=&amp;amp;edit_object_id=2945&amp;amp;sfsearch_single_line_address=&amp;amp;sfsearch_state=',
  {'action': 'store_locator', 'location': '19310', 'rule': 'storeLocator'}],

 ['https://www.walmart.com/cart2/cart.do?webflowforward=true&amp;amp;webflowforward=true',
  {'norm': 'https://www.walmart.com/cart2/cart.do', 'action': 'view cart', 'rule': 'cart'}],

 ['https://www.walmart.com/cart2/cartCmd.do#gberr',
  {'norm': 'https://www.walmart.com/cart2/cart.do#gberr', 'action': 'checkout', 'rule': 'checkout1'}],

 ['https://www.walmart.com/subflow/CheckoutFlowContext/1000193623/webflow/co_regular',
  {'norm': 'https://www.walmart.com/wmflows/checkout', 'action': 'checkout', 'rule': 'checkout2'}],

 ['https://www.walmart.com/co_regular/thankyouPrintable.do',
  {'action': 'purchase', 'rule': 'thankyouPrintable'}],

 ['https://www.walmart.com/printerFriendlyThankyou.do',
  {'action': 'purchase', 'rule': 'printerFriendlyThankyou'}],
]

