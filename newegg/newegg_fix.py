def match(url):
    return url.hostname.endswith('newegg.com')

rules = [


    {'name'    : 'product',
     'pattern' : '^/Product/Product.aspx([?]|$)',
     'action'  : 'product',
     'qpattern': 'Item=(?P<pid>.*?)([&]|$)',
     'norm'    : 'http://www.newegg.com/Product/Product.aspx?Item={pid}'}, 

    {'name'    : 'shocker_product',
     'pattern' : '^/Special/ShellShocker.aspx',
     'action'  : 'product',    
     'norm'    : 'http://www.newegg.com/Special/ShellShocker.aspx',
     },
    
    {'name'    : 'store_list',
     'pattern' : '^/(?P<c1>.*?)/Store([&#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.newegg.com/{c1}/Store',
     },

    {'name'    : 'list',
     'pattern' : '^/(?P<c1>.*?)/(?P<word>.*?)/ID-(?P<c1id>.*?)([,/&#?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.newegg.com/{c1}/{word}/ID-{c1id}',
     },

     {'name'    : 'product_list',
     'pattern' : '^/Product/ProductList.aspx([#?]|$)',
     'action'  : 'list',
     # 'qpattern': '(?P<query>.*?)=(?P<search>.*?)([&]|$)',
     'norm'    : 'http://www.newegg.com/Product/ProductList.aspx?{query}={search}',
     },

     {'name'    : 'promotions_list',
     'hpattern': 'promotions',
     'pattern' : '^/(?P<c1>.*?)/(?P<c1id>.*?)/index.html',
     'action'  : 'list',
     'norm'    : 'http://promotions.newegg.com/{c1}/{c1id}/index.html',
     },

     {'name'    : 'daily_list',
     'pattern' : '^/DailyDeal.aspx([?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.newegg.com/DailyDeal.aspx',
     },

     {'name'    : 'index_list',
     'pattern' : '^/Index.aspx([?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.newegg.com/Index.aspx',
     },
     
    {'name'    : 'combodeals_list',
     'pattern' : '^/Store/ComboDeals.aspx([?]|$)',
     'action'  : 'list',
     'norm'    : 'http://www.newegg.com/Store/ComboDeals.aspx',
     },    

    {'name'    : 'add_cart',
     'pattern' : '^/Shopping/AddToCart.aspx([?]|$)',
     'hpattern': 'secure',
     'action'  : 'cart',
     'norm'    : 'http://secure.newegg.com/Shopping/AddToCart.aspx'
    },

    {'name'    : 'view_shop_item',
     'pattern' : '^/Shopping/ShoppingItem.aspx([?]|$)',
     'action'  : 'cart',
     'norm'    : 'http://www.newegg.com/Shopping/ShoppingItem.aspx'
    },

    {'name'    : 'view_shop_cart',
     'pattern' : '^/Shopping/ShoppingCart.aspx([?]|$)',
     'hpattern': 'secure',
     'action'  : 'cart',
     'norm'    : 'http://secure.newegg.com/Shopping/ShoppingCart.aspx'
    },

    {'name'    : 'purchase_guest',
     'spattern' : 'https',
     'hpattern': 'secure',
     'pattern' : '^/Guest/CheckoutStep4.aspx',
     'action'  : 'purchase',
     'norm'    : 'https://secure.newegg.com/Guest/CheckoutStep4.aspx'
    },

    {'name'    : 'purchase_registered',
     'spattern' : 'https',
     'hpattern': 'secure',
     'pattern' : '^/Shopping/CheckoutStep3.aspx',
     'action'  : 'purchase',
     'norm'    : 'https://secure.newegg.com/Shopping/CheckoutStep3.aspx'
    },

    {'name'    : 'checkout',
     'spattern' : 'https',
     'hpattern': 'secure',
     'pattern' : '^/(?P<word>.*?)/CheckoutStep(?P<num>[0-9]*?).aspx',
     'action'  : 'checkout',
     'norm'    : 'https://secure.newegg.com/{word}/CheckoutStep{num}.aspx'
    },

    
   {'name'    : 'irrelevant_domain',
     'hpattern': '(images|sellerportal|ssl-images|blog|secure.m|www.www.biz|download|wireless|help|promotions)',
     'action'  : 'irrelevant'},    

    {'name'    : 'irrelevant',
     'pattern' : '^/(Info|Special|marketplace|landingpage|win)',
     'action'  : 'irrelevant'}, 


]

params = [
    {'qpattern': 'N=(?P<c1id>.*?)([&]|$)'},
    {'qpattern': 'Description=(?P<search>.*?)([&]|$)'},
]

examples = [
    ['http://www.newegg.com/Product/Product.aspx?Item=9SIA2KF0TT6338',
    {
        'norm':'http://www.newegg.com/Product/Product.aspx?Item=9SIA2KF0TT6338',
        'action':'product',
        'pid': '9SIA2KF0TT6338',
        'rule': 'product'
    }],

    ['http://www.newegg.com/Special/ShellShocker.aspx?cm_sp=ShellShocker-_-1241625-_-03132013_4,1',
    {
        'norm': 'http://www.newegg.com/Special/ShellShocker.aspx',
        'action': 'product',
        'rule': 'shocker_product'
    }],

    ['http://www.newegg.com/PCs-Laptops/Store?nm_mc=EMC-IGNEFL022813&amp;amp;cm_mmc=EMC-IGNEFL022813-_-EMC-022813-Latest-_-Header-tab-_-PCLaptop,1',
    {
        'norm': 'http://www.newegg.com/PCs-Laptops/Store',
        'action': 'list',
        'c1': 'PCs-Laptops',
        'rule': 'store_list'
    }],

    ['http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007603%20600003274%20600003290&IsNodeId=1&name=500GB,1',
    {
        'norm': 'http://www.newegg.com/Product/ProductList.aspx?N=100007603%20600003274%20600003290',
        'action': 'list',
        'query': 'N',
        'search': '100007603%20600003274%20600003290',
        'rule': 'product_list'
    }],

    ['http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=24%20inch%20monitor&bop=And&Order=PRICE&PageSize=20,1',
    {
        'norm': 'http://www.newegg.com/Product/ProductList.aspx',
        'action': 'list',
        'rule': 'product_list'
    }],


    ['http://www.newegg.com/72-Hour-Month-End-Overstock-Supersale/PromotionStore/ID-184,9',
    {
        'norm': 'http://www.newegg.com/72-Hour-Month-End-Overstock-Supersale/PromotionStore/ID-184',
        'action': 'list',
        'c1': '72-Hour-Month-End-Overstock-Supersale',
        'word': 'PromotionStore',
        'c1id': '184',
        'rule': 'list'
    }],

    ['http://www.newegg.com/All-Headphones-Accessories/SubCategory/ID-70/Page-2,2',
    {
        'norm':'http://www.newegg.com/All-Headphones-Accessories/SubCategory/ID-70',
        'action':'list',
        'c1': 'All-Headphones-Accessories',
        'word': 'SubCategory',
        'c1id': '70',
        'rule': 'list'
    }],

    ['http://www.newegg.com/All-Case-Covers/SubCategory/ID-612,3',
    {
        'norm':'http://www.newegg.com/All-Case-Covers/SubCategory/ID-612',
        'action':'list',
        'c1': 'All-Case-Covers',
        'word': 'SubCategory',
        'c1id': '612',
        'rule': 'list'
    }],


    ['http://www.newegg.com/Unlocked-Cell-phones/SubCategory/ID-2961?Tid=17487&cm_sp=CellPhonesTab-_-Pillars-_-UnlockedPhones',
    {
        'norm':'http://www.newegg.com/Unlocked-Cell-phones/SubCategory/ID-2961',
        'action':'list',
        'c1': 'Unlocked-Cell-phones',
        'word': 'SubCategory',
        'c1id': '2961',
        'rule': 'list'
    }],

    ['http://www.newegg.com/DailyDeal.aspx?name=DailyDeal&cm_sp=Dailydeal-_-adlink-_-05042013,3',
    {
        'norm': 'http://www.newegg.com/DailyDeal.aspx',
        'action': 'list',
        'rule': 'daily_list'
    }],

    ['http://www.newegg.com/DailyDeal.aspx?name=DailyDeal&cm_sp=Dailydeal-_-adlink-_-05042013,3',
    {
        'norm': 'http://www.newegg.com/DailyDeal.aspx',
        'action': 'list',
        'rule': 'daily_list'
    }],

    ['http://www.newegg.com/DailyDeal.aspx',
    {
        'norm': 'http://www.newegg.com/DailyDeal.aspx',
        'action': 'list',
        'rule': 'daily_list'
    }],

    ['http://www.newegg.com/Index.aspx?nm_mc=AFC-C8Junction&amp;amp;cm_mmc=AFC-C8Junction-_-Branding-_-na-_-na&amp;amp;AID=10485908&amp;amp;PID=1915435&amp;amp;SID=5803775&amp;amp;afsrc=1,1',
    {
        'norm': 'http://www.newegg.com/Index.aspx',
        'action': 'list',
        'rule': 'index_list'
    }],

    ['http://www.newegg.com/Store/ComboDeals.aspx?ComboStoreID=1&amp;amp;name=CPUs-Motherboards&amp;amp;Page=5&amp;amp;RandomID=61177242431804320130428145435,1',
    {
        'norm': 'http://www.newegg.com/Store/ComboDeals.aspx',
        'action': 'list',
        'rule': 'combodeals_list'
    }],

    ['http://www.newegg.com/Rosewill/BrandStore/ID-2177',
    {   
        'norm': 'http://www.newegg.com/Rosewill/BrandStore/ID-2177',
        'action': 'list',
        'c1': 'Rosewill',
        'word': 'BrandStore',
        'c1id': '2177',
        'rule': 'list'
    }],

    ['http://secure.newegg.com/Shopping/AddToCart.aspx?Submit=Add&amp;amp;ItemList=9SIA1140B48181%7C1&amp;amp;OptionItemList=&amp;amp;PreItemList=&amp;amp;EWTList=&amp;amp;ItemProhibited=&amp;amp;isAit=0,1',
    {
        'norm': 'http://secure.newegg.com/Shopping/AddToCart.aspx',
        'action': 'cart',
        'rule': 'add_cart',
    }],

    ['http://www.newegg.com/Shopping/ShoppingItem.aspx?ItemList=N82E16830120700',
    {
        'norm': 'http://www.newegg.com/Shopping/ShoppingItem.aspx',
        'action': 'cart',
        'rule': 'view_shop_item'
    }],

    ['http://secure.newegg.com/Shopping/ShoppingCart.aspx?RandomID=43130209402087820130307123306,3',
    {
        'norm': 'http://secure.newegg.com/Shopping/ShoppingCart.aspx',
        'action': 'cart',
        'rule': 'view_shop_cart'
    }],

    ['https://secure.newegg.com/Shopping/CheckoutStep1.aspx?CartID=888%2bZABYZH8VDLNH3WM',
    {
        'norm': 'https://secure.newegg.com/Shopping/CheckoutStep1.aspx',
        'action': 'checkout',
        'word': 'Shopping',                
        'num': '1',        
        'rule': 'checkout'
    }],

    ['https://secure.newegg.com/Guest/CheckoutStep3.aspx?CartID=328%2bQRAJR2XQH4GNTQ4&amp;amp;PaypalMark=1&amp;amp;flag=1',
    {
        'norm': 'https://secure.newegg.com/Guest/CheckoutStep3.aspx',
        'action': 'checkout',
        'word': 'Guest',                
        'num': '3',        
        'rule': 'checkout'
    }],

    ['https://secure.newegg.com/Guest/CheckoutStep4.aspx?CartID=949EB_PLUSNH7T3LKZQWF4MHO&SONumbers=215687198',
    {
        'norm': 'https://secure.newegg.com/Guest/CheckoutStep4.aspx',
        'action': 'purchase',    
        'rule': 'purchase_guest'
    }],

    ['https://secure.newegg.com/Shopping/CheckoutStep3.aspx?CartID=986%2bL0B1XDS7Q3PD0IO&amp;amp;SONumbers=154974416',
    {
        'norm': 'https://secure.newegg.com/Shopping/CheckoutStep3.aspx',
        'action': 'purchase',    
        'rule': 'purchase_registered'
    }],
]

