def match(url):
    return url.hostname.endswith('tigerdirect.com')

rules = [


    {'name'    : 'product',
     'pattern' : '^/applications/Searchtools/item-details.asp',
     'action'  : 'product',
     'qpattern': 'EdpNo=(?P<pid>.*?)([&]|$)',
     'norm'    : 'http://www.tigerdirect.com/applications/Searchtools/item-details.asp'}, 

    {'name'    : 'upsell_product',
     'pattern' : '^/applications/searchtools/item_upsell.asp',
     'action'  : 'product',
     'qpattern': 'EdpNo=(?P<pid>.*?)([&]|$)',
     'norm'    : 'http://www.tigerdirect.com/applications/searchtools/item_upsell.asp'}, 

    {'name'    : 'category_list',
    'pattern' : '^/applications/Category/guidedSearch.asp',
    'qpattern': 'CatId=(?P<c1id>.*?)([&]|$)',
    'action'  : 'list',
    'norm'    : 'http://www.tigerdirect.com/applications/Category/guidedSearch.asp',
    },

    {'name'    : 'category_slc_list',
    'pattern' : '^/applications/category/category_slc.asp',
    # 'qpattern': 'CatId=(?P<c1id>.*?)([&]|$)',
    'action'  : 'list',
    'norm'    : 'http://www.tigerdirect.com/applications/category/category_slc.asp',
    },

    {'name'    : 'category_tlc_list',
    'pattern' : '^/applications/category/category_tlc.asp',
    'qpattern': 'CatId=(?P<c1id>.*?)([&]|$)',
    'action'  : 'list',
    'norm'    : 'http://www.tigerdirect.com/applications/category/category_tlc.asp',
    },

    {'name'    : 'search_list',
    'pattern' : '^/applications/SearchTools/search.asp',
    'qpattern': 'keywords=(?P<search>.*?)([&]|$)',
    'action'  : 'list',
    'norm'    : 'http://www.tigerdirect.com/applications/SearchTools/search.asp',
    },

    {'name'    : 'index_list',
    'pattern' : '^/main/indexus.asp',
    'action'  : 'list',
    'norm'    : 'http://www.tigerdirect.com/main/indexus.asp',
    },

    {'name'    : 'index1_list',
    'pattern' : '^/indexus.asp',
    'action'  : 'list',
    'norm'    : 'http://www.tigerdirect.com/indexus.asp',
    },

    
    # {'name'    : 'overstock_list',
    # 'pattern' : '^/applications/Overstock/overstock_slc.asp',
    # 'qpattern': 'CatId=(?P<c1id>.*?)([&]|$)',
    # 'action'  : 'list',
    # 'norm'    : 'http://www.tigerdirect.com/applications/Overstock/overstock_slc.asp',
    # },

    {'name'    : 'normal_list',
    'pattern' : '^/applications/(?P<word>.*?)/(?P<word2>.*?)lc.asp',
    'action'  : 'list',
    'norm'    : 'http://www.tigerdirect.com/applications/{word}/{word2}lc.asp',
    },

    # {'name'    : 'normal2_list',
    # 'pattern' : '^/applications/(?P<word>.*?)/(?P<word2>.*?)_tlc.asp',
    # 'action'  : 'list',
    # 'norm'    : 'http://www.tigerdirect.com/applications/{word}/{word2}_tlc.asp',
    # },


    

    {'name'    : 'view_cart',
     'pattern' : '^/cgi-bin/ShoppingCart.asp',
     'action'  : 'cart',
     'norm'    : 'http://www.tigerdirect.com/cgi-bin/ShoppingCart.asp'
    },

    {'name'    : 'checkout',
     'spattern' : 'https',
     'hpattern': 'orders',
     'pattern' : '^/Checkout/(?P<method>.*?)',
     'action'  : 'checkout',
     'norm'    : 'https://orders.tigerdirect.com/Checkout/{method}'
    },

    {'name'    : 'store_locator',
     'pattern' : '^/retailstores/compusaStores/(?P<location>.*?).asp',
     'action'  : 'store_locator'},  


    {'name'    : 'irrelevant_domain',
     'hpattern': '(alpha|e|biz|static|news|tablets)',
     'action'  : 'irrelevant'},    

   

    {'name'    : 'irrelevant',
     'pattern' : '^/(help|giftcard|cgisec|sectors|email|coupons|include|applications/email|applications/SearchTools/giftideas|applications/campaigns|applications/b2b|applications/category/category_desktop.asp|applications/searchtools/failedsearch.asp|applications/category/topsoldskus.asp|applications/category/compare.asp|applications/openbox/openbox_slc.asp|applications/partners|applications/qa|cgi-bin/returns.asp|errors|go)',
     'action'  : 'irrelevant'}, 

]

params = [
    {'qpattern': 'Description=(?P<search>.*?)([&]|$)'},
]

examples = [
    ['http://www.tigerdirect.com/applications/Searchtools/item-details.asp?EdpNo=2416662&amp;amp;Sku=K24-2107&amp;amp;SRCCODE=MDOTTD&amp;amp;MobileOptOut=1',
    {
        'norm':'http://www.tigerdirect.com/applications/Searchtools/item-details.asp',
        'action':'product',
        'pid': '2416662',
        'rule': 'product'
    }],

    ['http://www.tigerdirect.com/applications/searchtools/item_upsell.asp?EdpNo=2951127&amp;amp;msg=',
    {
        'norm':'http://www.tigerdirect.com/applications/searchtools/item_upsell.asp',
        'action':'product',
        'pid': '2951127',
        'rule': 'upsell_product'
    }],

    
    ['http://www.tigerdirect.com/main/indexus.asp?SRCCODE=LINKSHARE&amp;amp;cm_mmc_o=-ddCjC1bELltzywCjC-d2CjCdwwp&amp;amp;AffiliateID=0j9vAklIxm0-p_DsvmnrKKmtfhbURYcj_A',
    {
        'norm': 'http://www.tigerdirect.com/main/indexus.asp',
        'action': 'list',
        'rule': 'index_list'
    }],

    ['http://www.tigerdirect.com/indexus.asp?SRCCODE=WEBGOOTD&amp;amp;cm_mmc_o=mH4CjC7BBTkwCjCECjCE&amp;amp;gclid=CIaC3PS0vrUCFQPnnAodTm0Aow',
    {
        'norm': 'http://www.tigerdirect.com/indexus.asp',
        'action': 'list',
        'rule': 'index1_list'
    }],



    ['http://www.tigerdirect.com/applications/Category/guidedSearch.asp?CatId=10',
    {
        'norm': 'http://www.tigerdirect.com/applications/Category/guidedSearch.asp',
        'action': 'list',
        'c1id': '10',
        'rule': 'category_list'
    }],

    ['http://www.tigerdirect.com/applications/category/category_slc.asp?CatId=1001&amp;amp;name=Video-Software&amp;amp;Nav=|c:997|&amp;amp;Sort=4&amp;amp;Recs=30',
    {
        'norm': 'http://www.tigerdirect.com/applications/category/category_slc.asp',
        'action': 'list',
        # 'c1id': '1001',
        'rule': 'category_slc_list'
    }],

    ['http://www.tigerdirect.com/applications/Category/category_tlc.asp?CatId=1&amp',
    {
        'norm': 'http://www.tigerdirect.com/applications/category/category_tlc.asp',
        'action': 'list',
        'c1id': '1',
        'rule': 'category_tlc_list'
    }],

    ['http://www.tigerdirect.com/applications/SearchTools/search.asp?cat=109&amp;amp;keywords=express cards&amp;amp;mnf=&amp;amp;lowprice=0&amp;amp;highprice=0#',
    {
        'norm': 'http://www.tigerdirect.com/applications/SearchTools/search.asp',
        'action': 'list',
        'search': 'express cards',
        'rule': 'search_list'
    }],

    ['http://www.tigerdirect.com/applications/Overstock/overstock_slc.asp?CatId=1736&amp;amp;category=Mobile%20Accessories',
    {
        'norm': 'http://www.tigerdirect.com/applications/Overstock/overstock_slc.asp',
        'action': 'list',
        'word': 'Overstock',
        'word2': 'overstock_s',
        'c1id': '1736',
        'rule': 'normal_list'
    }],

    ['http://www.tigerdirect.com/applications/refurb/refurb_slc.asp?CatId=22&amp;amp;category=CPUs%20/%20Processors',
    {
        'norm': 'http://www.tigerdirect.com/applications/refurb/refurb_slc.asp',
        'action': 'list',
        'word': 'refurb',
        'word2': 'refurb_s',
        'c1id': '22',
        'rule': 'normal_list'
    }],



    ['http://www.tigerdirect.com/cgi-bin/ShoppingCart.asp?message=&amp;amp;cm_mmc=Internal-_-Checkout-_-ContinueShopping-_-Review',
    {
        'norm': 'http://www.tigerdirect.com/cgi-bin/ShoppingCart.asp',
        'action': 'cart',
        'rule': 'view_cart'
    }],


]

