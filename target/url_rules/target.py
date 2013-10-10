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

     {'name'    : 'search',
     'pattern' : '^/s([&#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.target.com/s?searchTerm={search}&category={c1id}%7CAll%7Cmatchallpartial%7C{c1}',
     },

 

    {'name'    : 'view_cart',
     'pattern' : '^/checkout_cartview',
     'action'  : 'view cart',
     'norm'    : 'http://www.target.com/checkout_cartview'
    },

    {'name'    : 'checkout',
     'spattern' : 'https',
     'pattern' : 'checkout_process',
     'action'  : 'checkout',
     'norm'    : 'https://www-secure.target.com/checkout_process'
    },

    

    {'name'    : 'store_locator',
     'pattern' : '^/store-locator',
     'action'  : 'store_locator'
    },

   {'name'    : 'irrelevant_domain',
     'hpattern': '(hrportal|corporate|targetcareers|mail|seclogin|redcard|samples|targetcareers|secureconnect|babycatalog|prefs|catalogs|patio\.catalogs|baby\.catalogs|m|fstl|wedding|virtualoffice|guestlogin|webmail|redirect|imgsvc-secure|m\.weeklyad)',
     'action'  : 'irrelevant'},  

    {'name'    : 'irrelevant',
     'pattern' : '^/(redcard|np)',
     'action'  : 'irrelevant'}, 



]

params = [
    {'qpattern': 'searchTerm=(?P<search>.*?)([&]|$)'},
    {'qpattern': 'category=(?P<c1id>.*?)%7CAll%7Cmatchallpartial%7C(?P<c1>.*?)([&]|$)'},
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
    }],

    ['http://www.target.com/checkout_cartview?updatePrices=1&calculationUsageId=-1&calculationUsageId=-2&calculationUsageId=-7&orderId=.&lnk=atc_overlay',
        {
            'norm':'http://www.target.com/checkout_cartview',
            'action': 'view cart',
            'rule': 'view_cart'
        }
    ]


]

