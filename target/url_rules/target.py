def match(url):
    return url.hostname.endswith('target.com')

rules = [

    {'name'    : 'product',
     'pattern' : '^/p/(?P<pn1>.*?)/-/A-(?P<pid>.*?)([&#?]|$)',
     'action'  : 'product',
     'norm'    : 'http://www.target.com/p/{pn1}/-/A-{pid}'}, 

    {'name'    : 'c_list',
     'pattern' : '^/c/(?P<c1>.*?)/-/N-(?P<c1id>.*?)([&#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.target.com/c/{c1}/-/N-{c1id}',
     },

    {'name'    : 'sb_list',
     'pattern' : '^/sb/(?P<c1>.*?)/-/N-(?P<c1id>.*?)([&#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.target.com/sb/{c1}/-/N-{c1id}',
     },

     {'name'    : 'search',
     'pattern' : '^/s([&#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.target.com/s?searchTerm={search}&category={c1id}%7CAll%7Cmatchallpartial%7C{c1}',
     'qpattern': 'searchTerm=(?P<search>.*?)&category=(?P<c1id>.*?)%7CAll%7Cmatchallpartial%7C(?P<c1>.*?)([&]|$)'
     },

    {'name'    : 'irrelevant_domain',
     'hpattern': '(hrportal|corporate|targetcareers|mail|seclogin|redcard|samples|targetcareers|secureconnect|babycatalog|prefs|catalogs|patio\.catalogs|baby\.catalogs|m|fstl|wedding|virtualoffice|guestlogin|webmail|redirect|imgsvc-secure|m\.weeklyad)',
     'action'  : 'irrelevant'},  

    {'name'    : 'view_cart',
     'pattern' : 'checkout_cartview',
     'action'  : 'view cart',
     'norm'    : 'http://www.target.com/checkout_cartview'
    },

    {'name'    : 'store_locator',
     'pattern' : '^/store-locator',
     'action'  : 'store_locator'
    },  


    # {'name'    : 'irrelevant_domain',
    #  'hpattern': '(jobs|parts|intra|services|entertainment|webservices|marketplace|personalization|books|s7)',
    #  'action'  : 'irrelevant'},                    

    # {'name'    : 'shc_product',
    #  'pattern' : '^/shc/s/p_(?P<pid>.*?)([&#?]|$)',
    #  'action'  : 'product',
    #  'norm'    : 'http://www.sears.com/shc/s/p_{pid}'},                    

    # {'name'    : 'shc_product2',
    #  'pattern' : '^/shc/s/(?P<pn>.*?)/p-(?P<pid>.*?)([&#?]|$)',
    #  'action'  : 'product',
    #  'norm'    : 'http://www.sears.com/shc/s/{pn}/p-{pid}'},                    

    # # Must appear after 'shc_product2' so it won't override it
    # {'name'    : 'product',
    #  'pattern' : '^/(?P<pn>.*?)/p-(?P<pid>.*?)([&#?]|$)',
    #  'action'  : 'product',
    #  'norm'    : 'http://www.sears.com/{pn}/p-{pid}'},                    

    # {'name'    : 'shc_search',
    #  'pattern' : '^/shc/s/(?P<c2>.*?)/(?P<letter>[svc]?)-(?P<c2id>.*?)([&#?]|$)',
    #  'action'  : 'list',
    #  'norm'    : 'http://www.sears.com/shc/s/{c2}/{letter}-{c2id}?keyword={search}',
    #  'qpattern': 'keyword=(?P<search>.*?)([&]|$)'
    #  },

    # # Must appear after 'shc_search' so it won't override it
    # {'name'    : 'search',
    #  'pattern' : '^/(?P<c2>.*?)/(?P<letter>[svc]?)-(?P<c2id>.*?)([&#?]|$)',
    #  'action'  : 'list',
    #  'norm'    : 'http://www.sears.com/{c2}/{letter}-{c2id}?keyword={search}',
    #  'qpattern': 'keyword=(?P<search>.*?)([&]|$)'
    #  },

    # {'name'    : 'shc_list',
    #  'pattern' : '^/shc/s/(?P<letter>[svc]?)_(?P<c2id>.*?)([&#?]|$)',
    #  'action'  : 'list',
    #  'norm'    : 'http://www.sears.com/shc/s/{letter}_{c2id}'},                    

    # {'name'    : 'shc_list2',
    #  'pattern' : '^/shc/s/(?P<c2>.*?)/(?P<letter>[svc]?)-(?P<c2id>.*?)([&#?]|$)',
    #  'action'  : 'list',
    #  'norm'    : 'http://www.sears.com/shc/s/{c2}/{letter}-{c2id}'},                    

    # # Must appear after 'shc_list2' so it won't override it
    # {'name'    : 'list',
    #  'pattern' : '^/(?P<c2>.*?)/(?P<letter>([svc]|dap|dcp)?)-(?P<c2id>.*?)([&#?]|$)',
    #  'action'  : 'list',
    #  'norm'    : 'http://www.sears.com/{c2}/{letter}-{c2id}'},                    

    # {'name'    : 'search_only',
    #  'pattern' : '^/(?P<pre>.*?)search=(?P<search>.*?)([?]|$)',
    #  'action'  : 'list',
    #  'norm'    : 'http://www.sears.com/{pre}search={search}'},                    

    # {'name'    : 'shc_search_only',
    #  'pattern' : '^/shc/s/search_(?P<numbers>.*?)([?]|$)',
    #  'action'  : 'list',
    #  'norm'    : 'http://www.sears.com/shc/s/search_{numbers}?keyword={search}',
    #  'qpattern': 'keyword=(?P<search>.*?)([&]|$)'
    #  },

    # {'name'    : 'add_cart',
    #  'pattern' : 'shc/s/ProductOptionDisplayView',
    #  'action'  : 'add cart',
    #  'norm'    : 'http://www.sears.com/shc/s/ProductOptionDisplayView'},

    # {'name'    : 'view_cart',
    #  'pattern' : 'shc/s/ShoppingCartDisplayCmd',
    #  'action'  : 'view cart',
    #  'norm'    : 'http://www.sears.com/shc/s/ShoppingCartDisplayCmd'},

    # {'name'    : 'checkout',
    #  'spattern': 'https',
    #  'pattern' : 'shc/s/.*checkout',
    #  'action'  : 'checkout',
    #  'norm'    : 'https://www.sears.com/shc/s/checkout'},

    # {'name'    : 'StoreLocator',
    #  'pattern' : 'shc/s/StoreLocatorView',
    #  'action'  : 'offline_buy',
    #  'norm'    : 'http://www.sears.com/shc/s/StoreLocatorView'},
]

params = [
    #{'qpattern': 'keyword=(?P<search>.*?)([&]|$)'},     
]

examples = [
    ['http://www.target.com/p/the-second-dawn-paperback/-/A-13762396#prodSlot=medium_1_1&term=tirth',
    {
        'norm':'http://www.target.com/p/the-second-dawn-paperback/-/A-13762396',
        'action':'product',
        'pn': 'the-second-dawn-paperback',
        'pid': '13762396',
        'rule': 'product'
    }],

    ['http://www.target.com/c/patio/-/N-5xtq9#?lnk=gnav_patio_6_0',
    {
        'norm': 'http://www.target.com/c/patio/-/N-5xtq9',
        'action':'list',
        'c1': 'patio',
        'c1id': '5xtq9',
        'rule': 'c_list'
    }],

    ['http://www.target.com/sb/patio/-/N-5xtq9#?lnk=bnav_t_spc_2_0',
    {
        'norm': 'http://www.target.com/sb/patio/-/N-5xtq9',
        'action':'list',
        'c1': 'patio',
        'c1id': '5xtq9',
        'rule': 'sb_list'
    }],




    ['http://www.target.com/s?searchTerm=tirth&category=9611722%7CAll%7Cmatchallpartial%7Cclearance&lnk=snav_sbox_tirth#',
    {
        'norm': 'http://www.target.com/s?searchTerm=tirth&category=9611722%7CAll%7Cmatchallpartial%7Cclearance',
        'action': 'list',
        'search': 'tirth',
        'c1': 'clearance',
        'c1id': '9611722',
        'rule': 'search'
    }]


            
 # ['http://www.sears.com/appliances-accessories-washer-dryers/s-1023537?keyword=ge+washing+machines+on+sale&amp;amp;autoRedirect=true&amp;amp;viewItems=25&amp;amp;redirectType=CAT_REC_PRED',
 #  {'norm': 'http://www.sears.com/appliances-accessories-washer-dryers/s-1023537?keyword=ge+washing+machines+on+sale', 'action': 'list', 'c2': 'appliances-accessories-washer-dryers', 'letter': 's', 'c2id': '1023537', 'search': 'ge+washing+machines+on+sale', 'rule': 'search'}],
 
 # ['http://www.sears.com/computers-tablets-ereaders-tablets&amp;amp;Clearance/s-1231482572?filter=offer&amp;amp;keyword=augen+gentouch+nba7800atp+7inch+color+touchscreen+tablet+pc+w+android+2+1+os&amp;amp;keywordSearch=false&amp;amp;previousSort=ORIGINAL_SORT_ORDER&amp;amp;viewItems=50',
 #  {'norm': 'http://www.sears.com/computers-tablets-ereaders-tablets&amp;amp;Clearance/s-1231482572?keyword=augen+gentouch+nba7800atp+7inch+color+touchscreen+tablet+pc+w+android+2+1+os', 'action': 'list', 'c2': 'computers-tablets-ereaders-tablets&amp;amp;Clearance', 'letter': 's', 'c2id': '1231482572', 'search': 'augen+gentouch+nba7800atp+7inch+color+touchscreen+tablet+pc+w+android+2+1+os', 'rule': 'search'}],

 # ['http://www.sears.com/shc/s/appliances-small-kitchen-appliances-dessert-ice-cream-makers/s-1023488?keyword=ice+cream+maker&amp;amp;viewItems=25&amp;amp;autoRedirect=true&amp;amp;redirectType=CAT_REC_PRED&amp;amp;sid=ISx20070515x00001a&amp;amp;psid=31x2195606',
 #  {'norm': 'http://www.sears.com/shc/s/appliances-small-kitchen-appliances-dessert-ice-cream-makers/s-1023488?keyword=ice+cream+maker', 'action': 'list', 'c2': 'appliances-small-kitchen-appliances-dessert-ice-cream-makers', 'letter': 's', 'c2id': '1023488', 'search': 'ice+cream+maker', 'rule': 'shc_search'}],

 # ['http://www.sears.com/appliances-accessories/c-1020089?sName=View All&amp;amp;keywordSearch=false&amp;amp;previousSort=ORIGINAL_SORT_ORDER&amp;amp;pageNum=2&amp;amp;subCatView=true&amp;amp;viewItems=25',
 #  {'norm': 'http://www.sears.com/appliances-accessories/c-1020089', 'action': 'list', 'c2': 'appliances-accessories', 'letter': 'c', 'c2id': '1020089', 'rule': 'list'}],

 # ['http://www.sears.com/real-deals-electronics/dap-120000000221806?adCell=W21#null=sony',
 #  {'norm': 'http://www.sears.com/real-deals-electronics/dap-120000000221806', 'action': 'list', 'c2': 'real-deals-electronics', 'letter': 'dap', 'c2id': '120000000221806', 'rule': 'list'}],

 # ['http://www.sears.com/shc/s/clothing-women-s-dresses&amp;amp;Sears_Next/s-1023574?filter=storeOrigin_storeOrigin&amp;amp;viewItems=50&amp;amp;i_cntr=1366336840304',
 #  {'norm': 'http://www.sears.com/shc/s/clothing-women-s-dresses&amp;amp;Sears_Next/s-1023574', 'action': 'list', 'c2': 'clothing-women-s-dresses&amp;amp;Sears_Next', 'letter': 's', 'c2id': '1023574', 'rule': 'shc_list2'}],

 # ['http://www.sears.com/shc/s/c_10153_12605_Appliances_Washers?filter=Appliance+Brand%7CKenmore+Elite&amp;amp;sName=View+All&amp;amp;subCatView=true&amp;amp;sid=ISx20070515x00001a&amp;amp;psid=15x799994&amp;amp;knshCrid=30947979705&amp;amp;k_clickID=0fe2638c-af07-1869-83e0-000012cfd103',
 #  {'norm': 'http://www.sears.com/shc/s/c_10153_12605_Appliances_Washers', 'action': 'list', 'letter': 'c', 'c2id': '10153_12605_Appliances_Washers', 'rule': 'shc_list'}],

 # ['http://www.sears.com/acer-aspire-as5749z-4809-notebook-pc/p-020W004451989000P?prdNo=13&amp;amp;blockNo=13&amp;amp;blockType=G13',
 #  {'norm': 'http://www.sears.com/acer-aspire-as5749z-4809-notebook-pc/p-020W004451989000P', 'action': 'product', 'pn': 'acer-aspire-as5749z-4809-notebook-pc', 'pid': '020W004451989000P', 'rule': 'product'}],

 # ['http://www.sears.com/search=+newborn+boy%92s+bodysuit+pluto+short+sleeve?vName=Baby&amp;amp;cName=Baby+EB_AMP+Toddler+Clothing&amp;amp;autoRedirect=true&amp;amp;viewItems=50&amp;amp;redirectType=CAT_REC_PRED',
 #  {'norm': 'http://www.sears.com/search=+newborn+boy%92s+bodysuit+pluto+short+sleeve', 'action': 'list', 'pre': '', 'search': '+newborn+boy%92s+bodysuit+pluto+short+sleeve', 'rule': 'search_only'}],

 # ['http://www.sears.com/search=00648235000',
 #  {'norm': 'http://www.sears.com/search=00648235000', 'action': 'list', 'pre': '', 'search': '00648235000', 'rule': 'search_only'}],

 # ['http://www.sears.com/shc/s/search=storage%20cabinet?catalogId=12605&amp;amp;storeId=10153&amp;amp;i_cntr=1359514147071',
 #  {'norm': 'http://www.sears.com/shc/s/search=storage%20cabinet', 'action': 'list', 'pre': 'shc/s/', 'search': 'storage%20cabinet', 'rule': 'search_only'}], 

 # ['http://www.sears.com/shc/s/p_10153_12605_002B1393000P?&amp;amp;sid=IMx20120601x002000-Clothing-WindowShopper',
 #  {'norm': 'http://www.sears.com/shc/s/p_10153_12605_002B1393000P', 'action': 'product', 'pid': '10153_12605_002B1393000P', 'rule': 'shc_product'}],

 # ['http://www.sears.com/shc/s/search_10153_12605?vName=Appliances&amp;amp;cName=Microwaves&amp;amp;keyword=whirlpool+microwave&amp;amp;sid=ISx20070515x00001d&amp;amp;psid=15x1222646&amp;amp;knshCrid=1728848975&amp;amp;k_clickID=06860883-73e1-c2c9-d27c-00002c7e8150',
 #  {'norm': 'http://www.sears.com/shc/s/search_10153_12605?keyword=whirlpool+microwave', 'action': 'list', 'numbers': '10153_12605', 'search': 'whirlpool+microwave', 'rule': 'shc_search_only'}], 

 # ['http://www.sears.com/es/us/shc/s/ShoppingCartDisplayCmd?catalogId=12605&amp;amp;isCartValidated=true&amp;amp;orderId=.&amp;amp;displayEmptyCart=true&amp;amp;storeId=10153&amp;amp;ddkey=http:OrderItemDisplay',
 #  {'norm': 'http://www.sears.com/shc/s/ShoppingCartDisplayCmd', 'action': 'view cart', 'rule': 'view_cart'}], 

 # ['http://www.sears.com/shc/s/ProductOptionDisplayView?addToCartBtn=false&amp;amp;variant=0&amp;amp;atcFBT=PDP%3AFrequently+Bought+Together&amp;amp;PRODUCT_OPTIONS_RECOMMENDATIONS=true&amp;amp;orderId=481054203&amp;amp;UnitNumber=&amp;amp;cName=PatioFurniture&amp;amp;itemAdd=true&amp;amp;atc=PDP%3AHL3&amp;amp;vNameString=Outdoor+Living&amp;amp;catalogId=12605&amp;amp;OneClickExpressCheckout=&amp;amp;partNumber=&amp;amp;catIdsAdded=%5B43033952%2C+43591455%5D&amp;amp;sName=Garden%2520Oasis%2520Collectionsmv%3Drr&amp;amp;returnURL=&amp;amp;ffm_1=&amp;amp;vName=Outdoor%2520Living&amp;amp;nextPage=ProductOption&amp;amp;atc2=PDP%3AFrequently+Bought+Together&amp;amp;instPrice=&amp;amp;oosCatentryIds=&amp;amp;langId=-1&amp;amp;productPageFlag=POView&amp;amp;PRODUCT_OPTIONS_PAGE_FLAG=true&amp;amp;zipCode=&amp;amp;shipping=&amp;amp;grUserType=&amp;amp;IndicatorA=delivery&amp;amp;arrivalMethod=DDC&amp;amp;cNameString=Patio+Furniture&amp;amp;ItemsAdded=2&amp;amp;pickupStoreId=&amp;amp;presellDate=&a',
 #  {'norm': 'http://www.sears.com/shc/s/ProductOptionDisplayView', 'action': 'add cart', 'rule': 'add_cart'}], 
 
 # ['https://www.sears.com/shc/s/CheckOutLoginView?storeId=10153&amp;amp;catalogId=12605&amp;amp;langId=-1&amp;amp;zipCode=&amp;amp;krypto=woyJuooEB_PLUSFemBLaZ3dQUzy9fkvLaCOndNcr23jz31oWucjdKYlYjBmyzjguHvVaoBAeu0aZmwtEry%0AD7ZlncUUvbiUEB_PLUS1LmiLqL6HLtLmEB_PLUSoCZMNtEB_PLUSS1HcdEB_PLUS4K7QRRH0j97j8otFrpigpf0ynbEB_PLUSrLSFqeuL8%0APom006gfdhKEB_PLUSjx16yTOANuH73w7CviFmSeDakOthVE%2FgV3YxSLC2m4G2fJckOvXDD3TNBCHIfKjT%0A3aWGDI%2FCLWFt0TFnXP0RV3upDugOBBdkLEq22b2YQ8enbszBfGfXqd02WEB_PLUSrNBU8uUYHukACSPaiW%0A4i8NREAham9SNISGONz4qSaizGhKk1shu1M9pzeDkyLXlqFSFDv9MUoQU7mn5ze9vBEB_PLUS4Qc2K9vJe%0A753fZUp48jLLhmD4KcDmHf2H9xlIxx1ocixV21TEB_PLUS7MbEbBGL0wpJP3Ery3xwH2EB1zQGOQBajWsK%0Ai9AJTaWPLtHs%2FxirDCFvj2C8UQb6bdqB1J2uUZH3CLcuDihmcjCwNuLOREfMgh2MqXOrMbbAOrQ6%0ASM5JN1vmI98h6CLTVb0pRPqudKHILUX3iGGVW8XmoApDNo8IzIO40aABy7xBOOcYXVvLQuFVrlMP%0AXtpEiwhPn27hayPIHqkjzOvJRoKO%2FDvC9z5gVngXm3K1YR6wb7qzVNX29KWnhphnnGe6yRM4Vnr4%0Aei%2FwIUsesVa8WQ6vtwmlOtGj4CZRIYugQeBpCCNLq2DaqD07h6bIAFHrZP297xFoBZGxa7Akb0V6%0AIDYXM',
 #  {'norm': 'https://www.sears.com/shc/s/checkout', 'action': 'checkout', 'rule': 'checkout'}], 

 # ['http://www.sears.com/shc/s/StoreLocatorView?storeId=10153&amp;amp;catalogId=12605&amp;amp;langId=-1&amp;amp;adCell=W4&amp;amp;sid=ISx20070515x00001a&amp;amp;psid=13x187388&amp;amp;knshCrid=14601150205&amp;amp;k_clickID=483e4285-ee8c-4ac8-f3a4-00001ea8a22e',
 #  {'norm': 'http://www.sears.com/shc/s/StoreLocatorView', 'action': 'offline_buy', 'rule': 'StoreLocator'}], 

]

