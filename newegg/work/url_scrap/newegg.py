# -*- coding: utf-8 -*-

def parse_product(x, item):
    names = x.select('//h1/span[@itemprop="name"]/text()').extract()   
    if names:
        item['scrap_pn'] = names[-1].strip()
    
    return item

def parse_shocker_product(x, item):
    names = x.select('//h1/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    
    return item
    

def parse_product_list(x, item):
    names = x.select('//div[@class="wrap_description"]/a/span[@class="descText"]/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()
    else:
        names = x.select('//div[@class="itemText"]/div[@class="wrapper"]/a/span[@class="itemDescription"]/text()').extract()   
        if names:
            item['scrap_pn'] = names[0].strip()
        else:
            names = x.select('//span[@class="descText"]/text()').extract()   
            if names:
                item['scrap_pn'] = names[0].strip()
            else:
                names = x.select('//div[@class="wrap_description"]/a[@class="descText"]/span/text()').extract()   
                if names:
                    item['scrap_pn'] = names[0].strip()
                else:
                    names = x.select('//a[@class="ProductTitle"]/text()').extract()   
                    if names:
                        item['scrap_pn'] = names[0].strip()

                

    return item

def parse_brand_list(x, item):
    names = x.select('//span[@class="itemDesc"]/span[@class="itemTitle"]/text()').extract()   
    if names:
        item['scrap_pn'] = names[0].strip()


    return item


parsers = {
    'product': parse_product,
    'shocker_product': parse_shocker_product,
    'promotion_store_list': parse_product_list,
    'promotions_list': parse_product_list,
    'product_list': parse_product_list,
    'store_list': parse_product_list,
    'promotion_store_list': parse_product_list,
    'sub_list': parse_product_list,
    'daily_list': parse_product_list,
    'combodeals_list': parse_product_list,
    'brand_list': parse_brand_list
}


examples = [

    [parse_product,
    {
    'url' : 'http://www.newegg.com/Product/Product.aspx?Item=9SIA2KF0TT6338',
    'html' : '''
        <h1>
            <span id="grpDescrip_0"  itemprop="name" style="display:none;">Samsung Galaxy S3 16GB White 3G Unlocked Android GSM Smart Phone with S Voice &#47; Smart Stay &#47; Direct Call &#40;i9300&#41;</span>
                        <span id="grpDescrip_75-176-413" itemprop="name" style="display:none">Samsung Galaxy S3 i9300 Brown 3G Quad-Core 1.4GHz 16GB Unlocked Android GSM Smart Phone with S Voice &#47; Smart Stay &#47; Direct Call</span>
                        <span id="grpDescrip_75-176-348" itemprop="name" style="display:none">Samsung Galaxy S3 16GB Blue 3G Unlocked Android GSM Smart Phone with S Voice &#47; Smart Stay &#47; Direct Call &#40;i9300&#41;</span>
                        <span id="grpDescrip_75-176-349" itemprop="name" style="display:none">Samsung Galaxy S III 16GB Red 3G Unlocked Android GSM Smart Phone with S Voice &#47; Smart Stay &#47; Direct Call &#40;i9300&#41;</span>
                        <span id="grpDescrip_75-176-412" itemprop="name" style="display:none">Samsung Galaxy S3 i9300 16GB Black 3G Unlocked Android GSM Smart Phone with S Voice &#47; Smart Stay &#47; Direct Call</span>
                        <span id="grpDescrip_75-176-350" itemprop="name" >Samsung Galaxy S3 16GB White 3G Unlocked Android GSM Smart Phone with S Voice &#47; Smart Stay &#47; Direct Call &#40;i9300&#41;</span>
        </h1>
        ''',
    'pn' : "Samsung Galaxy S3 16GB White 3G Unlocked Android GSM Smart Phone with S Voice / Smart Stay / Direct Call (i9300)"
    }],

    [   parse_product,
        {
        'url' : 'http://www.newegg.com/Product/Product.aspx?Item=N82E16883220316',
        'html' : '''
            <h1>
                <span itemprop="name">
                    ASUS Eee Box Celeron 4GB DDR3 500GB HDD Capacity Desktop PC Windows 8 64-Bit EB1505-B011M
                </span>
            </h1>
            ''',
        'pn' : "ASUS Eee Box Celeron 4GB DDR3 500GB HDD Capacity Desktop PC Windows 8 64-Bit EB1505-B011M"
        }
    ],

    [   parse_shocker_product,
        {
            'url': 'http://www.newegg.com/Special/ShellShocker.aspx?cm_sp=ShellShocker-_-1195757-_-01292013_1,1',
            'html': '''
                <h1>Kingston HyperX 3K SH103S3&#47;120G 2.5&#34; 120GB SATA III MLC Internal Solid State Drive &#40;SSD&#41; &#40;Stand-Alone Drive&#41;</h1>
                ''',
            'pn': 'Kingston HyperX 3K SH103S3/120G 2.5" 120GB SATA III MLC Internal Solid State Drive (SSD) (Stand-Alone Drive)'
        }
    ],

    [parse_product_list,
        {
            'url': 'http://www.newegg.com/Accessories863/promotionStore/ID-2022863/,3',
            'html': '''
                <div class="wrap_description">
                    <a href="http://www.newegg.com/Product/Product.aspx?Item=N82E16835103059" title="View Details" onclick="s_objectID=&quot;http://www.newegg.com/Product/Product.aspx?Item=N82E16835103059_2&quot;;return this.s_oc?this.s_oc(e):true">
                        <span class="descText" id="titleDescriptionID1" style="display:inline-block">COOLER MASTER RG-TF4-TGU1-GP ThermalFusion 400 Thermal Compound</span>
                        <span class="descText" id="lineDescriptionID1" style="display:none">Cooler Master ThermalFusion 400 - High Performance Thermal Compound</span>
                    </a>
                </div>
                ''',
            'pn': 'COOLER MASTER RG-TF4-TGU1-GP ThermalFusion 400 Thermal Compound'
        }
    ],

    [parse_product_list,
    {
        'url': 'http://www.newegg.com/Product/ProductList.aspx?bop=And&Submit=DailyDeals&N=40000636,2',
        'html': '''
            <div class="itemText">
                <div class="wrapper">
                    <a href="http://www.newegg.com/Product/Product.aspx?Item=N82E16817107132" title="View Details" onclick="s_objectID=&quot;http://www.newegg.com/Product/Product.aspx?Item=N82E16817107132_2&quot;;return this.s_oc?this.s_oc(e):true">
                        <span class="itemDescription" id="titleDescriptionID3" style="display:none">BYTECC KVM-MPC-2100 Auto USB 2 Port KVM Switch with Cable and Audio Function</span>
                        <span class="itemDescription" id="lineDescriptionID3" style="display:inline">BYTECC KVM-MPC-2100 Auto USB 2 Port KVM Switch with Cable and Audio Function</span>
                    </a>
                </div>
                <ul class="itemFeatures"><li>&nbsp;2 Ports Computer Connect...</li><li>&nbsp;Video Resolution 1920 x ...</li>
                </ul>   
                <ul class="featureList">
                    <li><b>Type:</b> D-Sub</li><li><b>Computer Connections:</b> 2 Ports</li><li><b>Video Resolution:</b> 1920 x 1440</li><li><b>Bandwidth:</b> 250MHz</li>
                    <li><b>Model #: </b>KVM-MPC-2100</li>
                    <li><b>Item #: </b>N82E16817107132</li>
                    <li><b>Return Policy: </b><a href="http://www.newegg.com/HelpInfo/ReturnPolicy.aspx#44" target="_blank" title="Standard Return Policy(New Window)" onclick="s_objectID=&quot;http://www.newegg.com/HelpInfo/ReturnPolicy.aspx#44_1&quot;;return this.s_oc?this.s_oc(e):true">Standard Return Policy</a></li>
                </ul>
            </div>
            ''',
        'pn': 'BYTECC KVM-MPC-2100 Auto USB 2 Port KVM Switch with Cable and Audio Function'
    }],


    [parse_product_list,
        {
            'url': 'http://www.newegg.com/PCs-Laptops/Store?nm_mc=EMC-IGNEFL022813&amp;amp;cm_mmc=EMC-IGNEFL022813-_-EMC-022813-Latest-_-Header-tab-_-PCLaptop,1',
            'html': '''
                <div class="wrap_description">
                    <a href="http://www.newegg.com/Product/Product.aspx?Item=N82E16834314216" title="View Details" onclick="s_objectID=&quot;http://www.newegg.com/Product/Product.aspx?Item=N82E16834314216_2&quot;;return this.s_oc?this.s_oc(e):true">
                        <span class="descText" id="titleDescriptionID1" style="display:inline-block">Acer Aspire V5 V5-552-X814 AMD A10-5757M 2.5GHz 15.6" Windows 8 Notebook</span>
                        <span class="descText" id="lineDescriptionID1" style="display:none">Acer Aspire V5 V5-552-X814 AMD A-Series A10-5757M(2.50GHz) 6GB Memory 750GB HDD 15.6" Notebook Windows 8</span>
                    </a>
                </div>
                ''',
            'pn': 'Acer Aspire V5 V5-552-X814 AMD A10-5757M 2.5GHz 15.6" Windows 8 Notebook'
        }
    ],

    [parse_product_list,
        {
            'url': 'http://www.newegg.com/PCs-Laptops/Store?nm_mc=EMC-IGNEFL022813&amp;amp;cm_mmc=EMC-IGNEFL022813-_-EMC-022813-Latest-_-Header-tab-_-PCLaptop,1',
            'html': '''
                <div class="wrap_description">
                    <a class="descText" href="http://www.newegg.com/Product/Product.aspx?Item=N82E16882676341" onclick="cmCreateManualLinkClickTag('http://www.newegg.com/Product/Product.aspx?Item=N82E16882676341&amp;cm_sp=Specials-_-82-676-341-_-10152013_1')" title="View Details">
                        <span>Samsung Galaxy Gear Smartwatch - Mocha Gray</span>
                    </a>
                </div>
                ''',
            'pn': 'Samsung Galaxy Gear Smartwatch - Mocha Gray'
        }
    ],

    [parse_brand_list,
    {
        'url':'http://www.newegg.com/Rosewill/BrandStore/ID-2177',
        'html': '''
           <span class="itemDesc">
                <span class="itemTitle">Rosewill RHTB-13003 TV Bracket mounts 37"-75", Max. Load : 132lbs , Max.VESA 800 x ...</span> 
            </span>
            ''',
        'pn': 'Rosewill RHTB-13003 TV Bracket mounts 37"-75", Max. Load : 132lbs , Max.VESA 800 x ...'
    }],

    

]