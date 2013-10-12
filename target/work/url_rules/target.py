def match(url):
    return url.hostname.endswith('target.com')

rules = [

    {'name'    : 'product',
     'pattern' : '^/p/(?P<pn>.*?)/-/A-(?P<pid>.*?)([&#?]|$)',
     'action'  : 'product',
     'norm'    : 'http://www.target.com/p/{pn}/-/A-{pid}'}, 

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

     {'name'    : 's_search',
     'pattern' : '^/s/(?P<search>.*?)([&#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.target.com/s/{search}',
     },

     {'name'    : 'search',
     'pattern' : '^/s([&#?]|$)',
     'action'  : 'list',
     'qpattern': 'searchTerm=(?P<search>.*?)([&]|$)',
     'norm'    : 'http://www.target.com/s',
     },



    {'name'    : 'open_zoom_layer',
     'pattern' : '^/OpenZoomLayer',
     'action'  : 'product',
     'qpattern': 'itemTitle=(?P<pn>.*?)([&]|$)'
     },


    {'name'    : 'view_cart',
     'pattern' : '^/checkout_cartview',
     'action'  : 'view cart',
     'norm'    : 'http://www.target.com/checkout_cartview'
    },

    {'name'    : 'purchase',
     'spattern' : 'https',
     'hpattern' : 'www-secure',
     'pattern' : '^/checkout_printconfirmation',
     'action'  : 'purchase',
     'norm'    : 'https://www-secure.target.com/checkout_printconfirmation'
    },
    

    {'name'    : 'checkout',
     'spattern' : 'https',
     'pattern' : '^/checkout',
     'hpattern' : 'www-secure',
     'action'  : 'checkout',
     'norm'    : 'https://www-secure.target.com/checkout'
    },

    {'name'    : 'store_locator',
     'pattern' : '^/store-locator/store-details/storeNumber=(?P<location>.*?)([&#?]|$)',
     'action'  : 'store_locator',
    },

    {'name'    : 'store_locator2',
     'pattern' : '^/store-locator/store-details([&#?]|$)',
     'action'  : 'store_locator',
     'qpattern': 'storeNumber=(?P<location>.*?)([&]|$)',
    },

   {'name'    : 'irrelevant_domain',
    'hpattern': '(nro01|weeklyad|coupons|rcam|hrportal|corporate|targetcareers|mail|seclogin|redcard|samples|targetcareers|secureconnect|babycatalog|prefs|catalogs|patio\.catalogs|baby\.catalogs|m|fstl|wedding|virtualoffice|guestlogin|webmail|redirect|imgsvc-secure|m\.weeklyad)',
    'action'  : 'irrelevant'},

    {'name'    : 'irrelevant',
     'pattern' : '^/(redcard|np|spot|SearchNavigationView|FiatsCmd|HelpContent|pharmacy|RegistryListPrintCmd|#)',
     'action'  : 'irrelevant'}, 

]

params = [
   
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

    

    ['http://www.target.com/s/papaya',
    {
        'norm': 'http://www.target.com/s/papaya',
        'action': 'list',
        'search': 'papaya',
        'rule': 's_search'
    }],


    ['http://www.target.com/s?searchTerm=tirth&category=9611722%7CAll%7Cmatchallpartial%7Cclearance&lnk=snav_sbox_tirth#',
    {
        'norm': 'http://www.target.com/s',
        'action': 'list',
        'search': 'tirth',
        'rule': 'search'
    }],

    ['http://www.target.com/checkout_cartview?updatePrices=1&calculationUsageId=-1&calculationUsageId=-2&calculationUsageId=-7&orderId=.&lnk=atc_overlay',
        {
            'norm':'http://www.target.com/checkout_cartview',
            'action': 'view cart',
            'rule': 'view_cart'
        }
    ],

    ['https://www-secure.target.com/checkout_billing?storeId=10151&amp;amp;catalogId=10051&amp;amp;langId=-1&amp;amp;krypto=DYHUITxotig%2BSyiW%2BUdSAtdN3lkPDUUtkvZDrLm4DQL2GUrwtP0Fnw%3D%3D&amp;amp;ddkey=https:checkout_addgiftwrap',
    {
        'norm': 'https://www-secure.target.com/checkout',
        'action': 'checkout',
        'rule': 'checkout'
    }
    ],

    ['https://www-secure.target.com/checkout_printconfirmation?catalogId=10051&orderId=1143722545&langId=-1&storeId=10151&ormOrderId=101143722545',
    {
    'norm': 'https://www-secure.target.com/checkout_printconfirmation',
    'action': 'purchase',
    'rule': 'purchase'
    }
    ],


    ['http://weeklyad.target.com',
    {
        'action':'irrelevant',
        'rule': 'irrelevant_domain'
    }],

    ['http://www.target.com/OpenZoomLayer?template=scene7-image&image=Target/11125130_is&omniZoomPartNumber=11125130&swCellSpacing=10,10&swHighlightThickness=1&swBorderThickness=0&itemTitle=Magna+MenEB_AMP%23x27%3Bs+Excitor+26EB_AMPquot%3B+Terrain+Bike+-+RedEB_AMP%23x2f%3BBlack&omniImageCount=1#',
    {
        'action': 'product',
        'rule': 'open_zoom_layer',
        'pn': 'Magna+MenEB_AMP%23x27%3Bs+Excitor+26EB_AMPquot%3B+Terrain+Bike+-+RedEB_AMP%23x2f%3BBlack'
    }],
    ['http://www.target.com/OpenZoomLayer?template=scene7-image&amp;amp;image=Target/12307835_is&amp;amp;omniZoomPartNumber=12307835&amp;amp;swCellSpacing=10,10&amp;amp;swHighlightThickness=1&amp;amp;swBorderThickness=0&amp;amp;itemTitle=WomenEB_AMP%23x27%3Bs+X',
    {
        'action': 'product',
        'rule': 'open_zoom_layer',
        'pn': 'WomenEB_AMP%23x27%3Bs+X'
    }],

    ['http://www.target.com/store-locator/store-details/storeNumber=1193#?afid=storeloc&amp;amp;cpng=MD&amp;amp;lnm=Gaithersburg_1193',
    {
        'action': 'store_locator',
        'rule': 'store_locator',
        'location': '1193'
    }],
    ['http://www.target.com/store-locator/store-details?storeNumber=844&amp;amp;submit=StoreDetails&amp;amp;page=stateResults&amp;amp;userAgent=0&amp;amp;mapHeight=420&amp;amp;mapWidth=530&amp;amp;storeDetailsAction=store-details&amp;amp;stateResultsPrint=state',
    {
        'action': 'store_locator',
        'rule': 'store_locator2',
        'location': '844'
    }],

]

