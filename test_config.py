# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
import datetime
today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))
today = str(today)
#from test_loop3 import isWaite_loop3


#详细页面等待函数配置
#content_wait_func_dic = {'':None,'isWaite_loop3':isWaite_loop3}

#配置xpath
parameter = {
    #老版本
    #金彩网
    "jincai_1" : {"li" : "//div[@class='col-lg-9 cfcpn_padding_LR0 cfcpn_list_border-right']/div[@class='cfcpn_list_content text-left']" , #标题的上一级
                  "li_time" : "./p/text()" , #时间
                  "title" : "./p/a/text()", #标题
                  "href" : "./p/a/@href", #标题地址
                  "domainName_url" : "http://www.cfcpn.com", #拼接域名
                  "li_area": "",  #区域
                  "page_name" :  {"type":0,"style":r'pageNo=\d+',"startNum":1}, #页数
                  "number_xpath" : "//ul[@class='pagination']/li[11]/a/text()", #页数区域
                  "search" : {"pageNo" : "1", "kflag" :"0" },
                  },
    #中国招标与采购网
    "zhongguozhaobiaoyucaigouwang_3":{
        #登陆
        "login":{"button":"//*[@id='login_frm1']/span[3]/input",
                 "isHasVerify_code":False,
                 "params":[{"type":"id","name":"username","value":"京北方信息技术"},
                           {"type":"id","name":"userpwd","value":"123456"}
                           ],
                 
                 },        
        "li" : "//ul[@class='ul_list']/li", #标题的上一级
        "li_time" : "./b/text()" , #时间
        "title" : "./a/@title", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "./span[2]/text()",  #区域
        "isloopBytime": True, #是否控制时间循环
        "page_name" : {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath" : "//*[@id='center_box']//font/b[1]/text()", #获取总的条数
        "search" : "",
        "content_wait_class":"isWaite_loop3"
    },
    #中国政府采购网
    "zhongguozhengfucaigouwang_4": {
        "li" : "//ul[@class='vT-srch-result-list-bid']/li" , #标题的上一级
        "li_time" : "./span/text()" , #时间
        "title" : "./a/text()", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "./span/a/text()",  #区域
        "page_name" :  {"type":0,"style":r'page_index=\d+',"startNum":1}, #页数
        "number_xpath" : "//div[@class='vT_z']/div/div/p[@class='pager']/a[last()-1]/text()", #页数区域
        "search" : "",
        "page_wait_class":""
    },
    #中国移动采购与招标网_招标
    "zhongguoyidongcaigouyuzhaobiao_5_0":{
        "li" : "//table[@class='jtgs_table']//tr[contains(@class,'_data_tr_flag')]" , #标题的上一级
        "li_time" : "" , #时间
        "title" : "./td[2]/a/@title", #标题
        "href" : "./@onclick", #标题地址
        "domainName_url" : "https://b2b.10086.cn/b2b/main/viewNoticeContent.html?noticeBean.id=", #拼接域名
        "li_area": "",  #区域
        "isloopBytime":False,
        "page_name" : {
            "type":2,
            "style":"post",
            "startNum":1,
            "headers":{
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'JSESSIONID=mhoX9yE4tFvB6cMJtU8NDTnJKrA5bgE6Ny0M_SAPLAGiB9L3KWvZb_Hg9zydgUW3; saplb_*=(J2EE204289820)204289852',
                'Host': 'b2b.10086.cn',
                'Referer': 'https://b2b.10086.cn/b2b/main/showBiao!preShowBiao.html?noticeType=list1',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',               
                'User-Agent': UserAgent().chrome,
                'Upgrade-Insecure-Requests': '1',
                },
            "data":{"page.currentPage" : "1",
                    "page.perPageSize" : "20",
                    "noticeBean.companyName": "",
                    "noticeBean.title" : "",
                    "noticeBean.startDate": yesterday,
                    "noticeBean.endDate" : yesterday
            },                                  
            "post_url":"https://b2b.10086.cn/b2b/main/showBiao!showZhaobiaoResult.html",
            "pageNoKey":"page.currentPage"
        }, 
        "number_xpath" : "//td[@id='pageid2']/table/tbody/tr/td[last()-2]/span/text()", #页数区域
        "search" : "",        
    },
    #中国移动采购与招标网_中标
    
    #国电招投标网_招标
    "guodianzhaobiaowang_7_0":{
        "li" : "//div[@class='lb-link']/ul/li" , #标题的上一级
        "li_time" : "./a/span[2]/text()" , #时间
        "title" : "./a/@title", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域 
        "page_name" :  {"type":1,"style":"http://www.cgdcbidding.com/zbgg/index_count.jhtml","replaceKey":"count","startNum":1}, #页数
        "number_xpath" : "//div[@class='pagination']/div/text()[1]", #页数区域
        "search" : "",        
    },
    #北京市政府采购网
    "beijingshizhengfu_8":{
        "li" : "//ul[@class='xinxi_ul']/li" , #标题的上一级
        "li_time" : "./span/text()" , #时间
        "title" : "./a/text()", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : ["http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg","http://www.ccgp-beijing.gov.cn/xxgg/qjzfcggg"], #拼接域名
        "li_area": "",  #区域 
        "page_name" :  {"type":0,"style":r'index_*\d*',"startNum":0}, #页数
        "number_xpath" : "", #页数区域
        "search" : "",        
    },    
    
    #中化招标平台
    "zhonghuazhaobiao_9_0":{
        "li" : "//ul[@class='search-list']/li" , #标题的上一级
        "li_time" : "./p/text()" , #时间
        "title" : "./a/@title", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "http://e.sinochemitc.com", #拼接域名
        "li_area": "",  #区域 
        "page_name" :  {"type":0,"style":r'pageNo=\d+',"startNum":1}, #页数
        "number_xpath" : "//div[@class='pag-txt hide-sm']/em[2]/text()", #页数区域
        "search" : "",           
    },
    #人保
    "renbao_10":{ 
        "li" : "//div[@class='contentBox']/div" , #标题的上一级
        "li_time" : "./div[@class='date']/text()" , #时间
        "title" : "./div[@class='content']/a/text()", #标题
        "href" : "./div[@class='content']/a/@href", #标题地址
        "domainName_url" : "http://caigou.epicc.com.cn", #拼接域名
        "li_area": "",  #区域 
        "page_name" :  {"type":0,"style":r'page=\d+',"startNum":1}, #页数
        "number_xpath" : "//div[@class='page_bg']/span[3]/text()", #页数区域
        "search" : "",           
    },
    #国寿
    "guoshou_11":{
        "li" : "//ul[@class='news_list__set']/li" , #标题的上一级
        "li_time" : "./span/text()" , #时间
        "title" : "./a/@title", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域 
        "page_name" :  {"type":0,"style":r'curtPage=\d+',"startNum":1}, #页数
        "number_xpath" : "//div[@class='event_area']/div[1]/div/a[last()-1]/text()", #页数区域
        "search" : "",           
    },    
    #安邦
    "anbang_12":{
        "li" : "//ul[@class='news_list']/li" , #标题的上一级
        "li_time" : "./span/text()" , #时间
        "title" : "./a/text()", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "http://ab.anbanggroup.com/abjr/cgyb/", #拼接域名
        "li_area": "",  #区域 
        "page_name" :  {"type":1,"style":"http://ab.anbanggroup.com/abjr/cgyb/indexcount.htm","replaceKey":"count","startNum":0}, #页数
        "number_xpath" : "//div[@class='page']/ul/li[last()-1]/a/text()", #页数区域
        "search" : "",           
    }, 
    #泰康
    "taikang_13_0": {
        "li" : "//div[@class='c1-body']/div" , #标题的上一级
        "li_time" : "./div[2]/text()" , #时间
        "title" : "./div[1]/a/@title", #标题
        "href" : "./div[1]/a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域 
        "page_name" :  {"type":1,"style":"http://eps.taikang.com/ggxx/index_count.htm","replaceKey":"count","startNum":1}, #页数
        "number_xpath" : "//div[@class='pagination']/a[last()]/@href", #页数区域
        "search" : "",           
    }, 
    #长城资产
    "changchengzichan_14": {
        "li" : "//div[@id='contentHolder']/ul/li" , #标题的上一级
        "li_time" : "./span/text()" , #时间
        "title" : "./a/text()", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "http://www.gwamcc.com", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {
            "type":3,
            "style":"onclick",
            "startNum":1,
            "onclick":[{"replaceKey":"count","button":"//li[@id='liPages']/a[text()=count]","params":[]}]
        },  #页数
        "number_xpath" : "//div[@id='pagerHolder']/ul/li[last()-2]/span/text()", #页数区域
        "search" : "",           
    }, 
    #信达资产
    "xindazichan_15": {
        "li" : "//div[contains(@class,'sGray')]" , #标题的上一级
        "li_time" : "./span[2]/text()" , #时间 
        "title" : "./strong/a/text()", #标题
        "href" : "./strong/a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":1,"style":"http://www.cinda.com.cn/xdjt/xdjtpd/cgxxgs/list_count.shtml","replaceKey":"count","startNum":1},
        "number_xpath" : "/html/body/div[2]/div/div[22]/div[1]/text()[3]", #页数区域
        "search" : "",           
    }, 
    #阳光保险
    "yangguangbaoxian_16":{
        "li" : "//div[contains(@class,'List1')]/ul/li" , #标题的上一级
        "li_time" : "./span/text()" , #时间 
        "title" : "./a/text()", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "http://sunshine-eps.sinosig.com", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":1,"style":"http://sunshine-eps.sinosig.com/cggg/index_count.jhtml","replaceKey":"count","startNum":1},
        "number_xpath" : "//div[contains(@class,'Top8 TxtCenter')]/div/text()[1]", #页数区域
        "search" : "",           
    },
    #出口信用保险
    "chukouxinyongbaoxian_17":{
        "li" : "//div[@class='campus']/ul/li" , #标题的上一级
        "li_time" : "./span/text()" , #时间 
        "title" : "./a/text()", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "http://www.sinosure.com.cn", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":1,"style":"http://www.sinosure.com.cn/gywm/gsjj/xxpl/jzcg/index_count.shtml","replaceKey":"count","startNum":1},
        "number_xpath" : "/html/body/div[3]/div/div[4]/div[2]/div/div[3]/span/text()[2]", #页数区域
        "search" : "",           
    },
    #华海
    "huahai_18":{
        "li" : "//ul[@class='callbids-list']/li" , #标题的上一级
        "li_time" : "./a/span[1]/text()" , #时间 
        "title" : "./a/h6/text()", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":1,"style":"https://www.cnoic.com/zbgg/index_count.jhtml","replaceKey":"count","startNum":1},
        "number_xpath" : "", #页数区域
        "search" : "",           
    },    
    #中信招标
    "zhongxinzhaobiao_19": {
        "li" : "//div[@class='newstitle']/ul" , #标题的上一级
        "li_time" : "./li[2]/text()" , #时间 
        "title" : "./li[1]/h3/a/@title", #标题
        "href" : "./li[1]/h3/a/@href", #标题地址
        "domainName_url" : "http://www.bidding.citic", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":0,"style":r'pageNo=\d+',"startNum":1},
        "number_xpath" : "//div[@class='number']/a[last()-2]/text()", #页数区域
        "search" : "",           
    },
    #中证信息
    "zhongzhenxinxi_20":{
        "li" : "//div[@class='list_list']/ul/li/div" , #标题的上一级
        "li_time" : "./span/text()" , #时间 
        "title" : "./a/@title", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "http://www.csits.org.cn", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":1,"style":"http://www.csits.org.cn/csits/zbxm/hydt_count.shtml","replaceKey":"count","startNum":1},
        "number_xpath" : "//div[@class='pagination_index_last']/text()[3]", #页数区域
        "search" : "",           
    },
    #国家电网
    "guojiadianwang_21": {
        "li" : "//div[@class='contentRight']/table/tbody/tr" , #标题的上一级
        "li_time" : "./td[4]/text()" , #时间 
        "title" : "./td[3]/a/@title", #标题
        "href" : "./td[3]/a/@onclick", #标题地址
        "href_suf":".html",
        "domainName_url" : "http://ecp.sgcc.com.cn/html/project/", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":0,"style":r'pageNo=\d+',"startNum":1},
        "number_xpath" : "//div[@class='page']/a[last()-1]/text()", #页数区域
        "search" : "",           
    },
    #国航
    "guohang_22":{
        "li" : "//div[@class='serviceMsg']/ul/li" , #标题的上一级
        "li_time" : "./span/text()" , #时间 
        "title" : "./a/text()", #标题
        "href" : "./a/@href", #标题地址
        "href_suf":"",
        "domainName_url" : "http://www.airchina.com.cn", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":1,"style":"http://www.airchina.com.cn/cn/contact_us/cgpt/cgxmgg/index_count.shtml","replaceKey":"count","startNum":1},
        "number_xpath" : "", #页数区域
        "search" : "",           
    },
    #邮政系统 招标
    "youzheng_23_0": {
        "li" : "//div[@class='new_list']/ul/li" , #标题的上一级
        "li_time" : "./span[2]/text()" , #时间 
        "title" : "./span[1]/a/@title", #标题
        "href" : "./span[1]/a/@href", #标题地址
        "href_suf":"",
        "domainName_url" : "http://www.chinapost.com.cn", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":1,"style":"http://www.chinapost.com.cn/html1/category/181313/7345-count.htm","replaceKey":"count","startNum":1},
        "number_xpath" : "//li[@id='PageNum']/a[last()-2]/text()", #页数区域
        "search" : "",           
    },
    #铁塔公司
    "tieta_24":{
        "li_time" : r'"effect_time":"(.*?)",' , #时间 
        "title" : r'"notice_title":"(.*?)",', #标题
        "href" : r'"id":"(.*?)",', #标题地址
        "href_suf":"",
        "domainName_url" : "http://www.tower.com.cn/default/main/index/noticedetail.jsp?_operation=notice&_notice=6&_id=", #拼接域名
        "li_area": r'"c_orgname":"(.*?)",',  #区域 
        "li_endtime":r'"failure_time":"(.*?)",', #截止时间
        "page_name" : {"replace":"pageIndex","startNum":0},
        "number_xpath" : "",
        "search" : "",           
    },
    #中国电子进出口有限公司
    "zhongguodianzijinchukou_26":  {
        "li" : "//div[@class='main']/div/div/table[2]/tbody/tr" , #标题的上一级
        "li_time" : "./td[2]/text()" , #时间 
        "title" : "./td[1]/a/text()", #标题
        "href" : "./td[1]/a/@href", #标题地址
        "href_suf":"",
        "domainName_url" : "https://www.ceiec.com.cn", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath" : "", #页数区域
        "search" : "",           
    },
    #中国电网注册信息
    "zhongguodianwangzhucexinxi_27":{
        "li" : "//div[@class='article_list_lb']//ul/li" , #标题的上一级
        "li_time" : "./i/text()" , #时间 
        "title" : "./span/a/@title", #标题
        "href" : "./span/a/@onclick", #标题地址
        "href_suf":"",
        "domainName_url" : "http://www.cpeinet.com.cn/cpcec/bul/bul_show.jsp?id=", #拼接域名
        "li_area": "./font/text()",  #区域 
        "page_name" : {"type":0,"style":r'PageIndex=\d+',"startNum":1},
        "number_xpath" : "//div[@class='page']/font[2]/text()", #页数区域
        "search" : "",           
    }, 
    #诚E招标网
    "chengEzhaobiao_28":{
        "li" : "//ul[@id='list1']/li" , #标题的上一级
        "li_time" : "./a/em/text()" , #时间 
        "title" : "./a/@title", #标题
        "href" : "./a/@href", #标题地址
        "href_suf":"",
        "domainName_url" : "https://www.chengezhao.com", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":0,"style":r'pageNo=\d+',"startNum":1},
        "number_xpath" : "//div[@class='pag-txt']/em[2]/text()", #页数区域
        "search" : "",           
    }, 
    #内蒙古招标投标网 招标
    "neimengguzhaobiao_29_0": {
        "li" : "//div[@id='menutab_4_1']/table[2]/tbody/tr" , #标题的上一级
        "li_time" : "./td[3]/text()" , #时间 
        "title" : "./td[1]/a/text()", #标题
        "href" : "./td[1]/a/@href", #标题地址
        "href_suf":"",
        "domainName_url" : "http://www.nmgztb.com.cn", #拼接域名
        "li_area": "",  #区域 
        "page_name" : {"type":0,"style":r'pageNo=\d+',"startNum":1},
        "number_xpath" : "//div[@id='layui-laypage-1']/span[1]/text()", #页数区域
        "search" : "",           
    },    
    
    #老版本结束
    
    
    #中化商务电子招投标平台
    "zhonghuashangwupingtai_1_1_0" : {"li" : '//*[@id="tab1"]/ul/li' , #标题的上一级
                                    "li_time" : "./p/text()" , #时间
                                    "title" : "./a/text()", #标题
                                    "href" : "./a/@href", #标题地址
                                    "domainName_url" : "http://e.sinochemitc.com", #拼接域名
                                    "li_area": "",  #区域
                                    "page_name" :  {"type":0,"style":r'pageNo=\d+',"startNum":1}, #有问题，需要测试   #页数
                                    "number_xpath" : '//div[@class="pag-link"]/a[7]/text()', #页数区域
                                    "search" : "",


                     },
       
        
    #中国人民财产保险采购门户
    "zhongguorenminbaoxiancaigou_1_3_0" : {"li" : '//div[@class = "contentBox"]/div' , #标题的上一级
                                           "li_time" : "./div[3]/text()" , #时间
                                           "title" : "./div[2]/a/text()", #标题
                                           "href" : "./div[2]/a/@href", #标题地址
                                           "domainName_url" : "http://caigou.epicc.com.cn", #拼接域名
                                           "li_area": "",  #区域
                                           "page_name" :  {"type":0,"style":r'page=\d+',"startNum":1}, #页数
                                           "number_xpath" : '//div[@class="page"]/div/span[3]/text()', #页数区域
                                           "search" : { "sendTimeMin" : yesterday ,"sendTimeMax" : yesterday, "page" : "1"},

                             
                     },
    
    #山东省采购与招标网
    "shangdongcaigouyuzhaobiao_1_6_0" : {"li" : '//div[@class="listmian"]//tr' , #标题的上一级
                                   "li_time" : "./td[5]/text()" , #时间
                                    "title" : "./td[2]/a/@title", #标题
                                    "href" : "./td[2]/a/@href", #标题地址
                                    "domainName_url" : "https://www.sdbidding.org.cn", #拼接域名
                                    "li_area": "",  #区域
                                    "page_name" :  {"type":0,"style":r'pageNo=\d+',"startNum":1}, #页数
                                    "number_xpath" : '//*[@id="page"]//a[@title="尾页"]/text()', #页数区域
                                    "search" : {"pageNo":"1"},

                                    
                             },
    #山西省招标投标公共服务平台
    "shanxishenzhaobiaogonggongfuwupingtai_1_7_0" : {"li" : '//ul[@class="on"]//table[@class="download_table"]/tbody/tr' , #标题的上一级
                                                     "li_time" : "./td[4]/text()" , #时间
                                                     "title" : "./td[2]/@title", #标题
                                                      "href" : "./td[2]/a/@href", #标题地址
                                                      "domainName_url" : "http://www.sxbid.com.cn", #拼接域名
                                                      "li_area": "./td[2]/span[1]/text()",  #区域
                                                      "page_name" : {"type":0,"style":r'pageNo=\d+',"startNum":1}, #页数
                                                      "number_xpath" : '//ul[@class="on"]//div[@class="list_pages"]/form/span/text()', #页数区域
                                                      "search" : {"pageNo":"1","pageSize":"15","accordToLaw":""},                                   
                                    },
    #中原招采网 
    "zhongyuanzhaocai_1_8_0" : {"li" : '//div[@class="List3 Top18"]/ul/li' , #标题的上一级
                                "li_time" : "./span[@class='time']/text()" , #时间
                                "title" : "./a/text()", #标题
                                "href" : "./a/@href", #标题地址
                                "domainName_url" : "", #拼接域名
                                "li_area": "",  #区域
                                "page_name" : {"type":1,"style":"http://www.zybtp.com/fwzb/index_count.jhtml","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
                                "number_xpath" : '//div[@class="Top8 TxtCenter"]/div[2]/a[4]/@href', #页数区域
                                "search" : "",
                          
                          },
    
    #河北省招标投标公共服务平台 页面内跳转  post请求
    "heibeishenzhaobiaotoubiao_1_9_0" : {"li" : '//div[@class="publicont"]/div' , #标题的上一级
                                         "li_time" : "./h4/span/text()" , #时间
                                         "title" : "./h4/a/@title", #标题
                                         "href" : "./h4/a/@href", #标题地址
                                         "domainName_url" : "http://www.hebeieb.com", #拼接域名
                                         "li_area": "./p/span[2]/text()",  #区域
                                         "page_name" : {
                                             "type":2,
                                             "style":"post",
                                             "startNum":0,
                                             "headers":{
                                                 'User-Agent': UserAgent().chrome,                                        
                                                 },
                                             "data":{
                                                 "page": "0",
                                                 "TimeStr": yesterday+","+yesterday,
                                                 "AllPtName": "",
                                                 "KeyStr": "",
                                                 "KeyType": "ggname"
                                                 },                                       
                                             "post_url":"http://www.hebeieb.com/tender/xxgk/zbgg.do",
                                             "pageNoKey":"page"
                                             },  
                                         "number_xpath" : '//*[@id="zbggPagination"]/a[4]/text()', #页数区域
                                         "search" : "",                                               
                                                                                                        
                                   },
    #黑龙江政府采购网
    "heilongjiangcaigou_1_10_0" : {"li" : "//div[@class='xxei']", #标题的上一级
                                   "li_time" : "./span[@class='sjej']/text()" , #时间
                                   "title" : "./span[@class='lbej']/a/text()", #标题
                                   "href" : "./span[@class='lbej']/a/@onclick", #标题地址
                                   "domainName_url" : "http://www.hljcg.gov.cn", #拼接域名
                                   "li_area": "",  #区域
                                   "page_name" : {
                                                "type":3,
                                                "style":"onclick",
                                                "startNum":1,
                                                "onclick":[{"replaceKey":"count","button":"//*[@id='rightej']/div[3]/div[2]/a[text()=count]","params":[]}]
                                                }, 
                                   "number_xpath" : '//*[@id="pageCount"]/@value', #页数区域
                                   "search" : "",

                          },
    #广东省政府采购网
    "guangdongshenzhengfucaigou_1_17_0":{"li" : "//ul[@class='m_m_c_list']/li", #标题的上一级
                                         "li_time" : "./em/text()" , #时间
                                         "title" : "./a/@title", #标题
                                         "href" : "./a/@href", #标题地址
                                         "domainName_url" : "http://www.ccgp-guangdong.gov.cn", #拼接域名
                                         "li_area": "",  #区域
                                         "page_name" : {"type":3,
                                                       "style":"onclick",
                                                       "startNum":1,
                                                       "onclick":[{"replaceKey":"count","button":"//div[@class='m_m_c_page']/form/a[span/text()=count]","params":[]}]
                                                       }, 
                                         "number_xpath" : "//div[@class='m_m_c_page']/form/a[last()-3]/span/text()", #页数区域
                                         "search" : "",                          
    },
    #内蒙古自治区政府采购网
    "neimengguzizhiquzhengfucaigou":{"li" : "//*[@id='itemContainer']/tbody/tr", #标题的上一级
                          "li_time" : "./td[@class='feed-time']/span//text()" , #时间
                          "title" : "./td[@class='title']/a/@title", #标题
                          "href" : "./td[@class='title']/a/@href", #标题地址
                          "domainName_url" : "", #拼接域名
                          "li_area": "./td[2]/span/text()",  #区域
                          "isloopBytime": False, #是否控制时间循环
                          "page_name" : {"type":3,
                                        "style":"onclick",
                                        "startNum":1,
                                        "onclick":[{"replaceKey":"count",
                                                   "button":"//*[@id='c-main-2']/div/div[2]/div[4]/a[text()=count]",
                                                   "params":[]}
                                                   ]
            , 
                                        },
                          "number_xpath" : "//*[@id='c-main-2']/div/div[2]/div[4]/a/text()", #页数区域
                          "search" : "",                          
    },
    #福建省公共资源交易中心
    "fujianshengonggongziyuanjiaoyi_1_18_0":{"li" : "//div[@class='main-content-grid']/table/tbody/tr", #标题的上一级
                                             "li_time" : "./td[2]/a/span/text()" , #截止时间
                                             "title" : "./td[2]/a/@title", #标题
                                             "href" : "./td[2]/a/@href", #标题地址
                                             "domainName_url" : "http://www.fjggzyjy.cn", #拼接域名
                                             "li_area": "",  #区域
                                             "isloopBytime": True, #是否控制时间循环
                                             "page_name" : {"type":1,"style":"http://www.fjggzyjy.cn/news/category/9/?page=count","replaceKey":"count","startNum":1},
                                             "number_xpath" : "//ul[@class='pagination']/li[last()-1]/a/text()", #页数区域
                                             "search" : "",                          
                             
                             },#区域        
    
    #千里马
    "qinglima_1_4_0":{
        #登陆
        "login":{"button":"//*[@id='deng']",
                 "isHasVerify_code":False,
                 "params":[{"type":"id","name":"abc","value":"18602298203"},
                           {"type":"xpath","name":"//*[@id='kuang']/fieldset/input[2]","value":"123456789"}
                           ],
                 "login_status":{"class":"isLogin_byXpath","params":"//*[@id='light']"}
                 },
        #start页  进入到显示 标题列表的页
        "startPage":{"type":"onclick",
                     "onclick":[{"button":"",
                                 "params":[],
                                 "url":"http://www.qianlima.com/zb/area_2262_0_1/"
                                 },                                
                                ],
        },
        
        "li" : "/html/body/table[8]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td/table/tbody/tr", #标题的上一级
        "li_time" : "./td[3]/text()" , #时间
        "title" : "./td[2]/a/@title", #标题
        "href" : "./td[2]/a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域
        "isloopBytime": True, #是否控制时间循环
        "page_name" : {"type":1,"style":"http://www.qianlima.com/zb/area_2262_0_count/","replaceKey":"count","startNum":1},
        "number_xpath" : "/html/body/table[8]/tbody/tr/td[1]/table[5]/tbody/tr/td/font/text()", #页数区域
        "search" : "",              
    },
    #深圳市国际招标有限公司 
    "shenzhenshiguojizhaobiao_1_21_0" : {"li" : '//div[@class="lb-link"]/ul/li' , #标题的上一级
                                         "li_time" : "./a/span[2]/text()" , #时间
                                         "title" : "./a/span[1]/text()", #标题
                                         "href" : "./a/@href", #标题地址
                                         "domainName_url" : "", #拼接域名
                                         "li_area": "",  #区域
                                         "page_name" : {"type":1,"style":"http://www.sztc.com/bidBulletin/index_count.htm?timeFrame=4","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
                                         "number_xpath" : '//div[@class="pag-txt"]/em[last()]/text()', #页数区域
                                         "search" : "",

                          },
    #广西招标网 
    "guangxizhaobiao_1_19_0" : {"li" : '//*[@id="main"]/div/div[2]/ul/li' , #标题的上一级
                                "li_time" : "./div[2]/text()" , #时间
                                "title" : "./div[1]/a/@title", #标题
                                "href" : "./div[1]/a/@href", #标题地址
                                "domainName_url" : "http://www.guangxibid.com.cn", #拼接域名
                                "li_area": "",  #区域
                                "page_name" : {"type":1,"style":"http://www.guangxibid.com.cn/zbcg/002001/count.html","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
                                "number_xpath" : '//*[@id="page"]/ul/li[last()]/a/text()', #页数区域
                                "search" : "",

                          }, 
    #湖南湘咨工程咨询有限公司 
    "hunanxiangzigongchengzixu_1_22_0" : {"li" : '//div[@class="lynewsli"]/ul/li' , #标题的上一级
                                          "li_time" : "./span[2]/text()" , #时间
                                           "title" : "./span[1]/a/text()", #标题
                                           "href" : "./span[1]/a/@href", #标题地址
                                           "domainName_url" : "http://www.hnxzzx.cn/", #拼接域名
                                           "li_area": "",  #区域
                                           "page_name" : {"type":1,"style":"http://www.hnxzzx.cn/NewsClass?id=7&page=count","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
                                           "number_xpath" : '//div[@class="pleft ptop20 page mbot"]/span[last()]/a/@href', #页数区域
                                           "search" : "",
                          },
    #江西省机电设备招标有限公司
    "jiangxijidianshebeizhaobiao_1_24_0": {"li" : '//*[@id="rightcontent"]/div[1]/div/div[2]/table/tbody/tr' , #标题的上一级
                                           "li_time" : "./td[4]/text()" , #时间
                                           "title" : "./td[2]/a/text()", #标题
                                           "href" : "./td[2]/a/@href", #标题地址
                                           "domainName_url" : "http://www.jxbidding.com/", #拼接域名
                                           "li_area": "",  #区域
                                           "page_name" : {"type":1,"style":"http://www.jxbidding.com/list.php?catid=146&page=count","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
                                           "number_xpath" : '//*[@id="pages"]/b[2]/text()', #页数区域
                                           "search" : "",
                          },
    #贵州省公共资源交易中心 
    "guizhoushenggongongziyuanjiaoyi_1_25_0": {"li" : '//div[@class="list_all_style_1 height_auto"]/div' , #标题的上一级
                                               "li_time" : "./p/span[last()]/text()" , #时间
                                               "title" : "./p/span[2]/text()", #标题
                                               "href" : "./@onclick", #标题地址
                                               "domainName_url" : "http://ggzy.guizhou.gov.cn", #拼接域名
                                               "li_area": "",  #区域
                                               "page_name" : {"type":1,"style":"http://ggzy.guizhou.gov.cn/jygkzfcg/index_count.jhtml","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
                                               "number_xpath" : '//ul[@class="pages-list"]/li[1]/a/text()', #页数区域
                                               "search" : "",
                                    },
    #陕西采购与招标网 
    "shanxicaigouyuzhaobiao_1_30_0": {"li" : '//ul[@class="news_list3 news_list_box"]/li' , #标题的上一级
                               "li_time" : "./span/text()" , #时间
                               "title" : "./a/text()", #标题
                               "href" : "./a/@href", #标题地址
                               "domainName_url" : "http://www.sntba.com/website/", #拼接域名
                               "li_area": "",  #区域
                               "page_name" : {"type":1,"style":"http://www.sntba.com/website/gg_list.aspx?category_id=53&page=count","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
                               "number_xpath" : '//div[@class="digg"]/a[last()-1]/text()', #页数区域
                               "search" : "",
                               },
    #安徽招标咨询网-省级
    "anhuizhaobiao_sheng_1_23_0":{"li" : "", #标题的上一级
                                  "li_time" : "//div[@class='content_list']/div[4]/ul/li/text()" , #时间
                                  "title" : "//div[@class='content_list']/div[2]/ul/li/a/@title", #标题
                                  "href" : "//div[@class='content_list']/div[2]/ul/li/a/@href", #标题地址
                                  "domainName_url" : "http://www.ahbc.com.cn/", #拼接域名
                                  "li_area": "",  #区域
                                  "isloopBytime": True, #是否控制时间循环
                                  "page_name" : {"type":3,
                                                 "style":"onclick",
                                                "startNum":1,
                                                "onclick":[{"replaceKey":"",
                                                            "button":"//div[@class='page']/div[2]/a",
                                                           "params":[]}],
                                                },
                                  "number_xpath" : "", #页数区域
                                   "search" : "",                          
                           },
    #安徽招标咨询网-市县
    "anhuizhaobiao_shixian_1_23_0":{"li" : "", #标题的上一级
                                    "li_time" : "//div[@class='content_list']/div[4]/ul/li/text()" , #时间
                                    "title" : "//div[@class='content_list']/div[2]/ul/li/a/@title", #标题
                                    "href" : "//div[@class='content_list']/div[2]/ul/li/a/@href", #标题地址
                                    "domainName_url" : "http://www.ahbc.com.cn/", #拼接域名
                                    "li_area": "",  #区域
                                    "isloopBytime": True, #是否控制时间循环
                                    "page_name" : {"type":3,
                                                   "style":"onclick",
                                                   "startNum":1,
                                                  "onclick":[{"replaceKey":"",
                                                              "button":"//div[@class='page']/div[2]/a",
                                                              "params":[]}],
                                                  },
                                    "number_xpath" : "", #页数区域
                                     "search" : "",                          
                            },
    #云南省公共资源交易中心-政府
    "yunnanshenggonggongziyuan_zhengfu_1_26_0":{"li" : "//table[@id='data_tab']/tbody/tr", #标题的上一级
                                                "li_time" : "./td[4]/text()" , #时间
                                                "title" : "./td[3]/a/@title", #标题
                                                "href" : "./td[3]/a/@href", #标题地址
                                                "domainName_url" : "https://www.ynggzy.com", #拼接域名
                                                "li_area": "",  #区域
                                                "isloopBytime": True, #是否控制时间循环
                                                "page_name" : {"type":3,
                                                               "style":"onclick",
                                                               "startNum":1,
                                                               "onclick":[{"replaceKey":"count",
                                                                          "button":"//div[@class='mmggxlh']/a[text()=count]",
                                                                          "params":[]}],
                                                              },
                                                "number_xpath" : "//div[@class='mmggxlh']/a[last()-1]/text()", #页数区域
                                                 "search" : "",                          
                            },
    #重庆市政府采购网
    "chongqingshizhengfucaigou_1_27_0":{"li" : "//div[@class='row']", #标题的上一级
                                        "li_time" : "./div[last()]/div/text()" , #时间
                                        "title" : "./div[1]/a/text()", #标题
                                        "href" : "./div[1]/a/@href", #标题地址
                                        "domainName_url" : "https://www.ccgp-chongqing.gov.cn", #拼接域名
                                        "li_area": "",  #区域
                                        "isloopBytime": True, #是否控制时间循环
                                        "page_name" : {"type":3,
                                                       "style":"onclick",
                                                       "startNum":1,
                                                       "onclick":[{"replaceKey":"count",
                                                                   "button":"//*[@id='notice']/div/div[3]/div[3]/ul/li/a[text()=count]",
                                                                  "params":[]}],
                                                       },
                                        "number_xpath" : "//*[@id='notice']/div/div[3]/div[2]/text()[1]", #页数区域
                                        "search" : "",                          
                            },
    #西藏自治区政府采购网
    "zizangzizhiquzhengfucaigou_1_28_0":{"li" : "//*[@id='news_div']/ul/li", #标题的上一级
                                         "li_time" : "./span/text()" , #时间
                                         "title" : "./div/a/text()", #标题
                                         "href" : "./div/a/@href", #标题地址
                                         "domainName_url" : "http://www.ccgp-xizang.gov.cn", #拼接域名
                                         "li_area": "",  #区域
                                         "isloopBytime": True, #是否控制时间循环
                                         "page_name" : {"type":3,
                                                        "style":"onclick",
                                                        "startNum":1,
                                                        "onclick":[{"replaceKey":"count",
                                                                    "button":"//div[@class='flipEffect']/div/a[text()=count]",
                                                                    "params":[]}],
                                                        },
                                         "number_xpath" : "", #页数区域
                                         "search" : "",                          
                                 },
    #新疆政府采购网
    "xinjiangzhengfucaigou_1_32_0":{"li" : "//div[@class='list-container']/ul/li", #标题的上一级
                                    "li_time" : "./span/text()" , #时间
                                    "title" : "./a/@title", #标题
                                    "href" : "./a/@href", #标题地址
                                    "domainName_url" : "http://www.ccgp-xinjiang.gov.cn", #拼接域名
                                    "li_area": "./a/span/text()",  #区域
                                    "isloopBytime": True, #是否控制时间循环
                                    "page_name" : {"type":3,
                                                   "style":"onclick",
                                                   "startNum":1,
                                                   "onclick":[{"replaceKey":"count",
                                                               "button":"//div[@class='paginationjs-pages']/ul/li[a[text()=count]]",
                                                               "params":[]}],
                                                   },
                                    "number_xpath" : "//div[@class='paginationjs-pages']/ul/li[last()-1]/a/text()", #页数区域
                                    "search" : "",                          
                             },
    #吉林招标网   非会员只能看免费信息type=0（只有招标）time=7  一周(30 月...)  (会员：招标信息（type=1），中标信息（type=4)) https://search.bidcenter.com.cn/search?diqu=7&time=7&type=0&page=1
    #登陆异常验证： 滑动条形框
    "jilinzhaobiao_1_11_0":{
        #登陆
        "login":{"button":"//*[@id='login_login_btn']",
                 "isHasVerify_code":False,
                 "params":[{"type":"id","name":"txtusername","value":"13889891148"},
                           {"type":"id","name":"txtpassword","value":"jbf123"}
                           ],
                 "login_status":{"class":"isLogin_byXpath","params":"//*[@id='f_meblg']/ul/li[1]"}
                 },
        #start页  进入到显示 标题列表的页
        "startPage":{"type":"onclick",
                     "onclick":[{"button":"",
                                 "params":[],
                                 "url":"https://search.bidcenter.com.cn/search?diqu=7&time=7&type=1&page=1"
                                 },                                
                                ],
                     },
        
        "li" : "//table/tbody/tr", #标题的上一级
        "li_time" : "./td[7]/text()" , #时间
        "title" : "./td[2]/a/text()", #标题
        "href" : "./td[2]/a/@href", #标题地址
        "domainName_url" : "https:", #拼接域名
        "li_area": "./td[5]/a/text()",  #区域
        "isloopBytime": True, #是否控制时间循环
        "page_name" : {"type":1,"style":"https://search.bidcenter.com.cn/search?diqu=7&time=7&type=1&page=count","replaceKey":"count","startNum":1},#{"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath" : "//div[@class='list_page']/div/ul/li[@class='page_num']/text()", #页数区域
        "search" : "",              
    },
    
    #四川招标采购信息网  已推荐 rec=1 和未推荐 rec=0
    "sichuanzhaobiaocaigou_1_29_0":  {#登陆
        "login":{"button":"//form[@class='layui-form userLogin']//button[text()='登录']",
                 "isHasVerify_code":False,
                 "params":[{"type":"xpath","name":"//input[@name='loginName']","value":"18161261795"},
                           {"type":"xpath","name":"//input[@name='password']","value":"jbf123456"}
                           ],
                 "login_status":{"class":"isLogin_byXpath","params":"//*[@id='f_meblg']/ul/li[1]"}
                 },
        "startPage_pre":{"type":"get","url":"http://www.sczbcg.com/template?fbid=7"},
        #start页  进入到显示 标题列表的页
        "startPage":[{"type":"get",
                      "url":"http://www.sczbcg.com/zbnews/list?rec=0&cp=1&ls=20",
                     },
                     {"type":"get",
                      "url":"http://www.sczbcg.com/zbnews/list?rec=1&cp=1&ls=20",
                      }],
        "li" : "//div[@class='layui-tab-content']/div/ul/li", #标题的上一级
        "li_time" : "./a/span[3]/text()" , #时间
        "title" : "./a/span[1]/text()", #标题
        "href" : "./a/@href", #标题地址
        "domainName_url" : "http://www.sczbcg.com", #拼接域名
        "li_area": "./a/span[2]/text()",  #区域
        "isloopBytime": True, #是否控制时间循环
        "page_name" : {"type":0,"style":r'cp=\d+',"startNum":1},#{"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath" : "//*[@id='layui-laypage-1']/a[last()-1]/text()", #页数区域
        "search" : "",            
    },

#zl excel colomn3


    # 中招国际招标有限公司
    "zhongzhaoguojizhaobiaoyouxiangongsi_3_1_0": {"li": '/html/body/div[3]/div[1]/ul/li',
                                       "li_time": ".//li[2]/text()",  # 时间
                                       "title": ".//a/@title",  # 标题
                                       "href": ".//a/@onclick",  # 标题地址
                                       "domainName_url": "http://www.cntcitc.com.cn/more/article.html?gContentId=",  # 拼接域名
                                       "li_area": "",  # 区域
                                       "page_name" : {"type":1,"style":"http://www.cntcitc.com.cn/column.html?currentPage=count&chanId=12","replaceKey":"count","startNum":1}, #页数
                                       "number_xpath": '', # 页数区域
                                       "search": "",
                                     },

# 中招国际招标有限公司
    "zhongzhaoguojizhaobiaoyouxiangongsi_3_1_1": {"li": '/html/body/div[3]/div[1]/ul/li',
                                       "li_time": ".//li[2]/text()",  # 时间
                                       "title": ".//a/@title",  # 标题
                                       "href": ".//a/@onclick",  # 标题地址
                                       "domainName_url": "http://www.cntcitc.com.cn/more/article.html?gContentId=",  # 拼接域名
                                       "li_area": "",  # 区域
                                       "page_name" : {"type":1,"style":"http://www.cntcitc.com.cn/column.html?currentPage=count&chanId=13","replaceKey":"count","startNum":1}, #页数
                                       "number_xpath": '', # 页数区域
                                       "search": "",
                                     },


    #中钢国际招标公司
    "zhonggangzhaobiaoyouxianzerengongsi_3_2_0" : {"li" : '//*[@id="list"]/tr', #标题的上一级
                          "li_time" : "./td[4]/text()" , #时间
                          "title" : "./td[2]/a/@title", #标题
                          "href" : "./td[2]/a/@href", #标题地址
                          "domainName_url" : "http://tendering.sinosteel.com", #拼接域名
                          "li_area": "",  #区域
                          "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'/html/body/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/ul/li/a[text()=count]',"params":[]}]
                                       },
                          "number_xpath" : '/html/body/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/div[2]/text()', #页数区域
                          "search" : "",

                          },

    #中钢国际招标公司
    "zhonggangzhaobiaoyouxianzerengongsi_3_2_1" : {"li" : '//*[@id="list"]/tr', #标题的上一级
                          "li_time" : "./td[3]/text()" , #时间
                          "title" : "./td[2]/a/@title", #标题
                          "href" : "./td[2]/a/@href", #标题地址
                          "domainName_url" : "http://tendering.sinosteel.com", #拼接域名
                          "li_area": "",  #区域
                          "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'/html/body/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/ul/li/a[text()=count]',"params":[]}]
                                       },
                          "number_xpath" : '/html/body/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/div[2]/text()', #页数区域
                          "search" : "",

                          },

    #太平洋保险
    "taipingyangbaoxian_3_3_0" : {"li" : '/html/body/div[2]/div[1]/div[2]/div[2]/ul/li', #标题的上一级
                          "li_time" : "./a/em/text()" , #时间
                          "title" : "./a/@title", #标题
                          "href" : "./a/@href", #标题地址
                          "domainName_url" : "http://purchase.cpic.com.cn", #拼接域名
                          "li_area": "",  #区域
                          "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'/html/body/div[2]/div[1]/div[2]/ul/div/div/div[2]/a[text()=count]',"params":[]}]
                                       },
                          "number_xpath" : '/html/body/div[2]/div[1]/div[2]/ul/div/div/div[1]/em[2]/text()', #页数区域
                          "search" : "",

                          },







    #天津市政府采购平台
    "tianjinshizhengfucaigoupingtai_3_4" : {"li" : '//*[@id="reflshPage"]/ul/li',
                                     "li_time" : "./span/text()" ,  #时间
                                     "title" : "./a/@title",  #标题
                                     "href" : "./a/@href",  #标题地址
                                     "domainName_url" : "http://tjgp.cz.tj.gov.cn",  #拼接域名
                                     "li_area": "",  #区域
                                     "page_name": {
                                         "type": 2,
                                         "style": "post",
                                         "startNum": 1,
                                         "headers": {
                                            'Accept': '*/*',
                                            'Accept-Encoding': 'gzip, deflate',
                                            'Accept-Language': 'zh-CN,zh;q=0.9',
                                            'Connection': 'keep-alive',
                                            'Content-Length': '65',
                                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                            'Cookie': 'uid=112; JSESSIONID=dZbtjG3SxsOV0T-53JO31Fl4aW7UsGZc2OTvgTyjBd6dyx9C-B6R!1932321690; insert_cookie=19021653',
                                            'Host': '60.30.25.51',
                                            'Origin': 'http://60.30.25.51',
                                            'Referer': 'http://60.30.25.51/portal/topicView.do?method=find',
                                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
                                            'X-Requested-With': 'XMLHttpRequest'
                                         },
                                         "data": {
                                            'method': 'find',
                                            'id': '',
                                            'page': '2',
                                            'name': '',
                                            'view': '',
                                            'ldateQGE': '',
                                            'ldateQLE': '',
                                            'siteLists': ''
                                         },
                                         "post_url": "http://60.30.25.51/portal/topicView.do",
                                         "pageNoKey":"page"
                                     },  # 页数  index_pageNo.jhtml
                                     "number_xpath": '//*[@id="pagesColumn"]/div/span[2]/b/text()',  # 总区域
                                     "search": "",
                                     "type"  : "招标"

                                     },

    # 内蒙古自治区公共资源交易平台
    "neimengguzizhiqugonggongziyuanjiaoyiwang_3_5_0": {"li": '/html/body/div[2]/div[2]/div/div[4]/table/tbody//tr',
                                       "li_time": "./td[4]/text()",  # 时间
                                       "title": "./td[3]/a/@title",  # 标题
                                       "href": "./td[3]/a/@href",  # 标题地址
                                       "domainName_url": "http://ggzyjy.nmg.gov.cn",  # 拼接域名
                                       "li_area": "",  # 区域
                                       "page_name" : {"type":1,"style":"http://ggzyjy.nmg.gov.cn/jyxx/jsgcZbgg?currentPage=count","replaceKey":"count","startNum":1}, #页数
                                       "number_xpath": '/html/body/div[2]/div[2]/div/div[5]/div/a[7]/text()', # 页数区域
                                       "search": "",
                                     },

    # 内蒙古自治区公共资源交易平台
    "neimengguzizhiqugonggongziyuanjiaoyiwang_3_5_1": {"li": '/html/body/div[2]/div[2]/div/div[4]/table/tbody//tr',
                                       "li_time": "./td[3]/text()",  # 时间
                                       "title": "./td[2]/a/@title",  # 标题
                                       "href": "./td[2]/a/@href",  # 标题地址
                                       "domainName_url": "http://ggzyjy.nmg.gov.cn",  # 拼接域名
                                       "li_area": "",  # 区域
                                       "page_name" : {"type":1,"style":"http://ggzyjy.nmg.gov.cn/jyxx/jsgcZbhxrgs?currentPage=count","replaceKey":"count","startNum":1}, #页数
                                       "number_xpath": '/html/body/div[2]/div[2]/div/div[5]/div/a[7]/text()', # 页数区域
                                       "search": "",
                                     },

    #山东省政府采购信息公开平台
    "shandongshengzhengfucaigouxinxigongkaipingtai_3_6_0": {"li": '//*[@class="Font9"]',
                                                      "li_time": "./text()[2]",  # 时间
                                                      "title": "./a/@title",  # 标题
                                                      "href": "./a/@href",  # 标题地址
                                                      "domainName_url": "http://www.ccgp-shandong.gov.cn",  # 拼接域名
                                                      "li_area": "",  # 区域
                                                      "page_name": {"type": 1,
                                                                  "style": "http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?subject=&pdate=&areacode=&unitname=&kindof=&projectname=&projectcode=&colcode=0301&curpage=count",
                                                                  "replaceKey": "count", "startNum": 1},
                                                       # "page_name" : {
                                                       #      "type":2,
                                                       #      "style":"post",
                                                       #      "startNum":1,
                                                       #      "headers":{
                                                       #          'User-Agent': UserAgent().chrome,
                                                       #      },
                                                       #      "data":{
                                                       #          "subject":"",
                                                       #          "pdate":"" ,
                                                       #          "areacode":"" ,
                                                       #          "unitname":"",
                                                       #          "kindof": "",
                                                       #          "projectname":"" ,
                                                       #          "projectcode": "",
                                                       #          "colcode": "0301",
                                                       #          "curpage": "",
                                                       #      },
                                                       #      "post_url":"http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp",
                                                       #      "pageNoKey":"curpage"
                                                       #  },
                                                       "number_xpath": '//*[@class = "Font9"]/strong/text()', # 页数区域
                                                       "search": "",
                                                       },

    # 山东省政府采购信息公开平台
    "shandongshengzhengfucaigouxinxigongkaipingtai_3_6_1": {"li": '//*[@class="Font9"]',
                                                      "li_time": "./text()[2]",  # 时间
                                                      "title": "./a/@title",  # 标题
                                                      "href": "./a/@href",  # 标题地址
                                                      "domainName_url": "http://www.ccgp-shandong.gov.cn",  # 拼接域名
                                                      "li_area": "",  # 区域
                                                      "page_name": {"type": 1,"style": "http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?subject=&pdate=&areacode=&unitname=&kindof=&projectname=&projectcode=&colcode=0302&curpage=count",
                                                                  "replaceKey": "count", "startNum": 1},
                                                      # "page_name": {
                                                      #     "type": 2,
                                                      #     "style": "post",
                                                      #     "startNum": 1,
                                                      #     "headers": {
                                                      #         'User-Agent': UserAgent().chrome,
                                                      #     },
                                                      #     "data": {
                                                      #           "subject":"",
                                                      #           "pdate":"" ,
                                                      #           "areacode":"" ,
                                                      #           "unitname":"",
                                                      #           "kindof": "",
                                                      #           "projectname":"" ,
                                                      #           "projectcode": "",
                                                      #           "colcode": "0301",
                                                      #           "curpage": "",
                                                      #     },
                                                      #     "post_url": "http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp",
                                                      #     "pageNoKey": "curpage"
                                                      # },
                                                      "number_xpath": '//*[@class = "Font9"]/strong/text()',  # 页数区域
                                                      "search": "",
                                                      },


    #山东省政府采购信息公开平台_市县
    "shandongshengzhengfucaigouxinxigongkaipingtai_shixian_3_6_0": {"li": '//*[@class="Font9"]',
                                                      "li_time": "./text()",  # 时间
                                                      "title": "./a/@title",  # 标题
                                                      "href": "./a/@href",  # 标题地址
                                                      "domainName_url": "http://www.ccgp-shandong.gov.cn",  # 拼接域名
                                                      "li_area": "",  # 区域
                                                      "page_name": {"type": 1,
                                                                  "style": "http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?subject=&pdate=&areacode=&unitname=&kindof=&projectname=&projectcode=&colcode=0303&curpage=count",
                                                                  "replaceKey": "count", "startNum": 1},
                                                       # "page_name" : {
                                                       #      "type":2,
                                                       #      "style":"post",
                                                       #      "startNum":1,
                                                       #      "headers":{
                                                       #          'User-Agent': UserAgent().chrome,
                                                       #      },
                                                       #      "data":{
                                                       #          "subject":"",
                                                       #          "pdate":"" ,
                                                       #          "areacode":"" ,
                                                       #          "unitname":"",
                                                       #          "kindof": "",
                                                       #          "projectname":"" ,
                                                       #          "projectcode": "",
                                                       #          "colcode": "0302",
                                                       #          "curpage": "",
                                                       #      },
                                                       #      "post_url":"http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp",
                                                       #      "pageNoKey":"curpage"
                                                       #  },
                                                       "number_xpath": '//*[@class = "Font9"]/strong/text()', # 页数区域
                                                       "search": "",
                                                       },


#山东省政府采购信息公开平台_市县
    "shandongshengzhengfucaigouxinxigongkaipingtai_shixian_3_6_1": {"li": '//*[@class="Font9"]',
                                                      "li_time": "./text()",  # 时间
                                                      "title": "./a/@title",  # 标题
                                                      "href": "./a/@href",  # 标题地址
                                                      "domainName_url": "http://www.ccgp-shandong.gov.cn",  # 拼接域名
                                                      "li_area": "",  # 区域
                                                      "page_name": {"type": 1,
                                                                  "style": "http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?subject=&pdate=&areacode=&unitname=&kindof=&projectname=&projectcode=&colcode=0304&curpage=count",
                                                                  "replaceKey": "count", "startNum": 1},
                                                       # "page_name" : {
                                                       #      "type":2,
                                                       #      "style":"post",
                                                       #      "startNum":1,
                                                       #      "headers":{
                                                       #          'User-Agent': UserAgent().chrome,
                                                       #      },
                                                       #      "data":{
                                                       #          "subject":"",
                                                       #          "pdate":"" ,
                                                       #          "areacode":"" ,
                                                       #          "unitname":"",
                                                       #          "kindof": "",
                                                       #          "projectname":"" ,
                                                       #          "projectcode": "",
                                                       #          "colcode": "0302",
                                                       #          "curpage": "",
                                                       #      },
                                                       #      "post_url":"http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp",
                                                       #      "pageNoKey":"curpage"
                                                       #  },
                                                       "number_xpath": '//*[@class = "Font9"]/strong/text()', # 页数区域
                                                       "search": "",
                                                       },

    #上海公共资源交易网
    "shanghaigonggongziyuanjiaoyiwang_3_14" :{"li": '/html/body/div[5]/div[1]/div[4]/div[2]/table/tbody/tr',
                                         "li_time": "./td[5]/text()",  # 时间
                                          "title": "./td[1]/a/@title",  # 标题
                                          "href": "./td[1]/a/@href",  # 标题地址
                                          "domainName_url": "http://www.zgazxxw.com",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://www.zgazxxw.com/sh-000012-count.html","replaceKey":"count","startNum":0},
                                          "number_xpath": '/html/body/div[5]/div[1]/div[5]/div[1]/a[last()]/@href', # 页数区域
                                          "search": "",
                                        },
     #浙江省公共资源交易网
    "zhejiangshenggonggongziyuanjiaoyiwang_3_15_0" :{"li" : '/html/body/div/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/div/table/tbody/tr'    ,
                                         "li_time": "./td[3]/text()",  # 时间
                                          "title": "./td[2]/a/@title",  # 标题
                                          "href": "./td[2]/a/@href",  # 标题地址
                                          "domainName_url": "http://new.zmctc.com",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://new.zmctc.com/zjgcjy/jyxx/004001/004001003/?Paging=count","replaceKey":"count","startNum":1},
                                          "number_xpath": '/html/body/div/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/div/div/div/table/tbody/tr/td[23]/@title', # 页数区域
                                          "search": "",
            },


    # 浙江省公共资源交易网
    "zhejiangshenggonggongziyuanjiaoyiwang_3_15_1" :{"li" : '/html/body/div/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/div/table/tbody/tr'    ,
                                         "li_time": "./td[3]/text()",  # 时间
                                          "title": "./td[2]/a/@title",  # 标题
                                          "href": "./td[2]/a/@href",  # 标题地址
                                          "domainName_url": "http://new.zmctc.com",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://new.zmctc.com/zjgcjy/jyxx/004010/004010003/?Paging=count","replaceKey":"count","startNum":1},
                                          "number_xpath": '/html/body/div/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/div/div/div/table/tbody/tr/td[23]/@title', # 页数区域
                                          "search": "",
            },

    #江苏政府采购网
    "jiangsuzhengfucaigouwang_3_16_0" :{"li" : '//*[@id="newsList"]/ul/li',
                                         "li_time": "./text()[2]",  # 时间
                                          "title": "./a/text()",  # 标题
                                          "href": "./a/@href",  # 标题地址
                                          "domainName_url": "http://www.ccgp-jiangsu.gov.cn/ggxx/gkzbgg/",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://www.ccgp-jiangsu.gov.cn/ggxx/gkzbgg/index_count.html","replaceKey":"count","startNum":1},
                                          "number_xpath": '//*[@id="newsPage"]/div/a[2]/@href', # 页数区域
                                          "search": "",
                                 },
    #江苏政府采购网
    "jiangsuzhengfucaigouwang_3_16_1" :{"li" : '//*[@id="newsList"]/ul/li',
                                         "li_time": "./text()[2]",  # 时间
                                          "title": "./a/text()",  # 标题
                                          "href": "./a/@href",  # 标题地址
                                          "domainName_url": "http://www.ccgp-jiangsu.gov.cn/ggxx/zbgg/",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://www.ccgp-jiangsu.gov.cn/ggxx/gkzbgg/index_count.html","replaceKey":"count","startNum":1},
                                          "number_xpath": '//*[@id="newsPage"]/div/a[2]/@href', # 页数区域
                                          "search": "",
                                 },

    #厦门市政府采购网
    "xiamenshigongongziyuanjiaoyiwang_3_18_0" : {"li" : '//*[@id="pubdays"]/li[position()>1]', #标题的上一级
                          "li_time" : "./span[2]/text()" , #时间
                          "title" : "./a/@title", #标题
                          "href" : "./a/@href", #标题地址
                          "domainName_url" : "http://www.xmzyjy.cn", #拼接域名
                          "li_area": "",  #区域
                          "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="pageList"]/li/a[text()=count]',"params":[]}]
                                       },
                          "number_xpath" : '//*[@id="pageList"]/li[14]/@jp-data', #页数区域
                          "search" : "",

                          },

    #厦门市政府采购网
    "xiamenshigongongziyuanjiaoyiwang_3_18_1" : {"li" : '//*[@id="pubdays"]/li[position()>1]', #标题的上一级
                          "li_time" : "./span[1]/text()" , #时间
                          "title" : "./a/@title", #标题
                          "href" : "./a/@href", #标题地址
                          "domainName_url" : "http://www.xmzyjy.cn", #拼接域名
                          "li_area": "",  #区域
                          "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="pageList"]/li/a[text()=count]',"params":[]}]
                                       },
                          "number_xpath" : '//*[@id="pageList"]/li[14]/@jp-data', #页数区域
                          "search" : "",

                          },




    #广西招标投标公共服务平台
    "guangxizhaobiaotoubiaogonggongfuwupingtai_3_19_0" :{"li": '/html/body/table/tbody/tr[position()>1]',
                                         "li_time": "./td[5]/text()",  # 时间
                                          "title": "./td[1]/a/@title",  # 标题
                                          "href": "./td[1]/a/@href",  # 标题地址
                                          "domainName_url": "",  # 拼接域名
                                          "li_area": "./td[3]/span/@title",  # 区域
                                          "page_name" : {"type":1,"style":"http://zbtb.gxi.gov.cn:9000/xxfbcms/category/bulletinList.html?searchDate=1994-10-23&dates=300&word=&categoryId=88&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=1&page=count","replaceKey":"count","startNum":1},
                                          "number_xpath": '/html/body/div[2]/a[2]/@onclick', # 页数区域
                                          "search": "",
                                          "type" : "招标"
                                        },

    # 广西招标投标公共服务平台
    "guangxizhaobiaotoubiaogonggongfuwupingtai_3_19_1" :{"li": '/html/body/table/tbody/tr[position()>1]',
                                         "li_time": "./td[5]/text()",  # 时间
                                          "title": "./td[1]/a/@title",  # 标题
                                          "href": "./td[1]/a/@href",  # 标题地址
                                          "domainName_url": "",  # 拼接域名
                                          "li_area": "./td[3]/span/@title",  # 区域
                                          "page_name" : {"type":1,"style":"http://zbtb.gxi.gov.cn:9000/xxfbcms/category/resultBulletinList.html?searchDate=1994-10-30&dates=300&word=&categoryId=90&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&page=count","replaceKey":"count","startNum":1},
                                          "number_xpath": '/html/body/div[2]/a[2]/@onclick', # 页数区域
                                          "search": "",
                                          "type" : "招标"
                                        },


    #海南省公共资源交易网
    "hainanshenggonggongziyuanjiaoyiwang_3_20" :{"li": '/html/body/div[4]/div[2]/div[2]/div',
                                         "li_time": "./p/span[2]/text()",  # 时间
                                          "title": "./p/a/@title",  # 标题
                                          "href": "./a/@href",  # 标题地址
                                          "domainName_url": "http://www.zgazxxw.com",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://www.zgazxxw.com/hi-001012l772-count.html","replaceKey":"count","startNum":0},
                                          "number_xpath": '/html/body/div[4]/div[2]/div[2]/div[30]/a[last()]/@href', # 页数区域
                                          "search": "",
                                        },

    #湖南国联招标有限公司
    "hunanguolianzhaobiaoyouxiangongsi_3_22_0": {"li": '',  # 标题的上一级
                                  "li_time": "",  # 时间
                                  "title": "/html/body/div[4]/div/div[2]/ul/li/a/text()",  # 标题
                                  "href": "/html/body/div[4]/div/div[2]/ul/li/a/@href",  # 标题地址
                                  "domainName_url": "",  # 拼接域名
                                  "li_area": "",  # 区域
                                  #"isloopBytime": False,
                                   "page_name" : {"type":1,"style":"https://hnglzb.dlzb.com/fuwu/page-count.shtml","replaceKey":"count","startNum":0},
                                  "number_xpath": '',  # 页数区域
                                  "search": "",

                                  },#todo 循环无法停止



    #安招采网
    "anzhaocai_3_23": {"li": '//*[@id="gridcontainer1"]/div/div[1]/div[position()>1]',  # 标题的上一级
                                  "li_time": "./span[3]/text()",  # 时间
                                  "title": "./a/text()",  # 标题
                                  "href": "./a/@href",  # 标题地址
                                  "domainName_url": "http://www.anzhaocai.com",  # 拼接域名
                                  "li_area": "./span[2]/text()",  # 区域
                                   "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="gridcontainer1"]/div/div[2]/div/a[text()=count]',"params":[]}]
                                       },
                                  "number_xpath": '//*[@id="gridcontainer1"]/div/div[2]/div/a[10]/text()',  # 页数区域
                                  "search": "",

                                  },
    #江西国政招标有限公司
        "jiangxiguozhengzhaobiaoyouxiangongsi_3_24_0" :{"li": '/html/body/div[3]/div/div/div[2]/ul/li',
                                             "li_time": "./span/text()",  # 时间
                                              "title": "./a/@title",  # 标题
                                              "href": "./a/@href",  # 标题地址
                                              "domainName_url": "http://www.jxgzzb.com.cn",  # 拼接域名
                                              "li_area": "",  # 区域
                                               "page_name" : {"type":1,"style":"http://www.jxgzzb.com.cn/Index/notice/inftype/1/page/count.html","replaceKey":"count","startNum":1},
                                              "number_xpath": '/html/body/div[3]/div/div/div[2]/div[2]/ul/li[8]/a/text()', # 页数区域
                                              "search": "",
                                            },


    #江西国政招标有限公司
        "jiangxiguozhengzhaobiaoyouxiangongsi_3_24_1" :{"li": '/html/body/div[3]/div/div/div[2]/ul/li',
                                             "li_time": "./span/text()",  # 时间
                                              "title": "./a/@title",  # 标题
                                              "href": "./a/@href",  # 标题地址
                                              "domainName_url": "http://www.jxgzzb.com.cn",  # 拼接域名
                                              "li_area": "",  # 区域
                                               "page_name" : {"type":1,"style":"http://www.jxgzzb.com.cn/Index/notice/inftype/2/page/count.html","replaceKey":"count","startNum":1},
                                              "number_xpath": '/html/body/div[3]/div/div/div[2]/div[2]/ul/li[8]/a/text()', # 页数区域
                                              "search": "",
                                            },


    #云南省政府采购网
    "yunnanshengzhengfucaigouwang_3_26_0": {"li": '//*[@id="bulletinlistid"]/tbody/tr',  # 标题的上一级
                                  "li_time": "./td[4]/text()",  # 时间
                                  "title": "./td[1]/@title",  # 标题
                                  # "href": {"href_url": "http://www.yngp.com/newbulletin_zz.do?method=preinsertgomodify&operator_state=1&flag=view&bulletin_id=substitution",
                                  #          "href_xpath_position":"./td[1]/a/@data-bulletin_id",
                                  #          "replacekey":"substitution"},  # 标题地址
                                  # "domainName_url": "",  # 拼接域名
                                  "href":"./td[1]/a/@data-bulletin_id",
                                  "domainName_url":"http://www.yngp.com/newbulletin_zz.do?method=preinsertgomodify&operator_state=1&flag=view&bulletin_id=",
                                  "li_area": "./td[3]/@title",  # 区域
                                   "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="bulletinlistid-footer"]/div/div[1]/ul/li/a[text()=count]',"params":[]}]
                                       },
                                  "number_xpath": '',  # 页数区域//*[@id="bulletinlistid-footer"]/div/div[1]/ul/li/text()
                                  "search": "",

                                  },

    #云南省政府采购网
    "yunnanshengzhengfucaigouwang_3_26_1": {"li": '//*[@id="bulletinlistid"]/tbody/tr',  # 标题的上一级
                                  "li_time": "./td[4]/text()",  # 时间
                                  "title": "./td[1]/@title",  # 标题
                                  # "href": {"href_url": "http://www.yngp.com/newbulletin_zz.do?method=preinsertgomodify&operator_state=1&flag=view&bulletin_id=substitution",
                                  #          "href_xpath_position":"./td[1]/a/@data-bulletin_id",
                                  #          "replacekey":"substitution"},  # 标题地址
                                  # "domainName_url": "",  # 拼接域名
                                  "href":"./td[1]/a/@data-bulletin_id",
                                  "domainName_url":"http://www.yngp.com/newbulletin_zz.do?method=preinsertgomodify&operator_state=1&flag=view&bulletin_id=",
                                  "li_area": "./td[3]/@title",  # 区域
                                   "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="bulletinlistid-footer"]/div/div[1]/ul/li/a[text()=count]',"params":[]}]
                                       },
                                  "number_xpath": '',  # 页数区域//*[@id="bulletinlistid-footer"]/div/div[1]/ul/li/text()
                                  "search": "",

                                  },

    #  重庆国际投资咨询集团有限公司
    "chongqingguojitouzizixunjituanyouxiangongsi_3_27": {"li": '//*[@id="right"]/div[2]/ul/li',
                         "li_time": "./span/text()",  # 时间
                         "title": "./div/a/@title",  # 标题
                         "href": "./div/a/@href",  # 标题地址
                         "domainName_url": "http://cqiic.com",  # 拼接域名
                         "li_area": "",  # 区域
                         "page_name": {"type": 1,
                                       "style": "http://cqiic.com/CZJTweb/zbgg/?Paging=count",
                                       "replaceKey": "count", "startNum": 1},
                         "number_xpath": '',  # 页数区域//*[@id="Paging"]/div/div/table/tbody/tr/td[19]
                         "search": "",
                         },





    # 拉萨公共资源交易网
    "lasagonggongziyuanjiaoyiwang_3_28_0": {"li": '//*[@id="listCon"]/ul/li',  # 标题的上一级
                                  "li_time": "./span/text()",  # 时间
                                  "title": "./a/@title",  # 标题
                                  "href": "./a/@href",  # 标题地址
                                  "domainName_url": "http://ggzy.lasa.gov.cn",  # 拼接域名
                                  "li_area": "",  # 区域
                                   "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="listCon"]/div/div/a[text()=count]',"params":[]}]
                                       },
                                  "number_xpath": '//*[@id="listCon"]/div/div/a[7]/@onclick',  # 页数区域
                                  "search": "",

                                  },


    # 拉萨公共资源交易网
    "lasagonggongziyuanjiaoyiwang_3_28_1": {"li": '//*[@id="listCon"]/ul/li',  # 标题的上一级
                                  "li_time": "./span/text()",  # 时间
                                  "title": "./a/@title",  # 标题
                                  "href": "./a/@href",  # 标题地址
                                  "domainName_url": "http://ggzy.lasa.gov.cn",  # 拼接域名
                                  "li_area": "",  # 区域
                                   "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":2,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="listCon"]/div/div/a[text()=count]',"params":[]}]
                                       },
                                  "number_xpath": '//*[@id="listCon"]/div/div/a[7]/@onclick',  # 页数区域
                                  "search": "",

                                  },



    #成都公共资源交易中心
    "chengdushigonggongziyuanjiaoyizhongxin_3_29" : {"li" : '//*[@id="contentlist"]/div', #标题的上一级
                          "li_time" : "./div[3]/div[1]/text()" , #时间
                          "title" : "./div[2]/a/text()", #标题
                          "href" : "./div[2]/a/@href", #标题地址
                          "domainName_url" : "https://www.cdggzy.com", #拼接域名
                          "li_area": "./div[1]/text()",  #区域
                          "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="Pager"]/a[text()=count]',"params":[]}]
                                       },
                          "number_xpath" : '//*[@id="Pager"]/a[13]/@href', #页数区域
                          "search" : "",

                          },

    #中国邮政
        "zhongguoyouzheng_3_31_0" :{"li": '//*[@id="Content3"]/div[2]/ul/li[position()<21]',
                                             "li_time": "./span[2]/text()",  # 时间
                                              "title": "./span[1]/a/@title",  # 标题
                                              "href": "./span[1]/a/@href",  # 标题地址
                                              "domainName_url": "http://www.chinapost.com.cn",  # 拼接域名
                                              "li_area": "",  # 区域
                                               "page_name" : {"type":1,"style":"http://www.chinapost.com.cn/html1/category/181313/7338-count.htm","replaceKey":"count","startNum":1},
                                              "number_xpath": '//*[@id="CBLast"]/@href', # 页数区域
                                              "search": "",
                                            },
    #19-2 中国邮政
        "zhongguoyouzheng_3_31_1" :{"li": '//*[@id="Content3"]/div[2]/ul/li[position()<21]',
                                             "li_time": "./span[2]/text()",  # 时间
                                              "title": "./span[1]/a/@title",  # 标题
                                              "href": "./span[1]/a/@href",  # 标题地址
                                              "domainName_url": "http://www.chinapost.com.cn",  # 拼接域名
                                              "li_area": "",  # 区域
                                               "page_name" : {"type":1,"style":"http://www.chinapost.com.cn/html1/category/181313/7334-count.htm","replaceKey":"count","startNum":1},
                                              "number_xpath": '//*[@id="CBLast"]/@href', # 页数区域
                                              "search": "",
                                            },



    # 20 兵团政府采购网
    "bingtuanzhengfucaigouwang_3_32": {"li": '/html/body/div[3]/div[2]/div[2]/div/div[2]/ul/li',
                         "li_time": "./span/text()",  # 时间
                         "title": "./div/a/text()",  # 标题
                         "href": "./div/a/@href",  # 标题地址
                         "domainName_url": "http://cgw.xjbt.gov.cn",  # 拼接域名
                         "li_area": "",  # 区域
                         "page_name": {"type": 1,
                                       "style": "http://cgw.xjbt.gov.cn/cggg/index_count.shtml",
                                       "replaceKey": "count", "startNum": 1},
                         "number_xpath": '/html/body/div[3]/div[2]/div[2]/div/div[3]/table/tbody/tr/td/text()[15]',  # 页数区域
                         "search": "",
                         },



    ########################
    #zl need_login











    # 华中招标网
    "huazhongzhaobiaowang_3_8_0": {
        # 登陆
        "login": {"button": "/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr[5]/td/p/input",
                  "isHasVerify_code": False,
                  "params": [{"type": "xpath", "name": "/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/input", "value": "jbfhn"},
                             {"type": "xpath", "name": "/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr[4]/td[2]/input", "value": "jbfhn82652688"}
                             ],
                  "login_status": {"class": "isLogin_byXpath", "params": "//*[@id='f_meblg']/ul/li[1]"}
                  },#  /html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr[3]/td
        # start页  进入到显示 标题列表的页
        "startPage": {"type": "onclick",
                      "onclick": [{"button": "",
                                   "params": [],
                                   "url": "http://hnzhaobiao.com/zhaobiao.asp?smallclassname=%B7%FE%CE%F1%D5%D0%B1%EA"
                                   },
                                  ],
                      },
        "li": '/html/body/table[4]/tbody/tr/td[2]/table[3]/tbody/tr/td[2]/table[4]/tbody/tr',  # 标题的上一级
        "li_time": "./td[3]/text()",  # 时间
        "title": "./td[1]/a/text()",  # 标题
        "href": "./td[1]/a/@href",  # 标题地址
        "domainName_url": "http://hnzhaobiao.com/",  # 拼接域名
        "li_area": "./td[2]/p/text()",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "http://hnzhaobiao.com/zhaobiao.asp?page=count&bigclassname=%D5%D0%B1%EA%D0%C5%CF%A2&smallclassname=%B7%FE%CE%F1%D5%D0%B1%EA&keywords=&dq=",
                      "replaceKey": "count",
                      "startNum": 1},  # {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath": "",  # 页数区域
        "search": "",
    },


    # 华中招标网
    "huazhongzhaobiaowang_3_8_1": {
        # 登陆
        "login": {"button": "/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr[5]/td/p/input",
                  "isHasVerify_code": False,
                  "params": [{"type": "xpath", "name": "/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/input", "value": "jbfhn"},
                             {"type": "xpath", "name": "/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr[4]/td[2]/input", "value": "jbfhn82652688"}
                             ],
                  "login_status": {"class": "isLogin_byXpath", "params": "//*[@id='f_meblg']/ul/li[1]"}
                  },#  /html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr[3]/td
        # start页  进入到显示 标题列表的页
        "startPage": {"type": "onclick",
                      "onclick": [{"button": "",
                                   "params": [],
                                   "url": "http://hnzhaobiao.com/zhongbiao12.asp"
                                   },
                                  ],
                      },
        "li": '/html/body/table[4]/tbody/tr/td[2]/table[3]/tbody/tr/td[2]/table[4]/tbody/tr',  # 标题的上一级
        "li_time": "./td[3]/p/text()",  # 时间
        "title": "./td[1]/a/text()",  # 标题
        "href": "./td[1]/a/@href",  # 标题地址
        "domainName_url": "http://hnzhaobiao.com",  # 拼接域名
        "li_area": "",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "http://hnzhaobiao.com/zhongbiao12.asp?page=count&bigclassname=%D6%D0%B1%EA%B9%AB%B8%E6&smallclassname=%D6%D0%B1%EA%B9%AB%B8%E6&keywords=&dq=",
                      "replaceKey": "count",
                      "startNum": 1},  # {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath": "",  # 页数区域
        "search": "",
    },




    #河北省招标网
    "hebeizhaobiaocaigouwang_3_9": {
        # 登陆
        "login": {"button": "//*[@id='login_login_btn']",
                  "isHasVerify_code": False,
                  "params": [{"type": "id", "name": "txtusername", "value": "13889891148"},
                             {"type": "id", "name": "txtpassword", "value": "jbf123"}
                             ],
                  "login_status": {"class": "isLogin_byXpath", "params": "//*[@id='f_meblg']/ul/li[1]"}
                  },
        # start页  进入到显示 标题列表的页
        "startPage": {"type": "onclick",
                      "onclick": [{"button": "",
                                   "params": [],
                                   "url": "https://search.bidcenter.com.cn/search?keywords=&diqu=3"
                                   },
                                  ],
                      },
        "li": '//*[@id="jq_project_list"]/tbody/tr',  # 标题的上一级
        "li_time": "./td[7]/text()",  # 时间
        "title": "./td[2]/a/text()",  # 标题
        "href": "./td[2]/a/@href",  # 标题地址
        "domainName_url": "http:",  # 拼接域名
        "li_area": "./td[5]/text()",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "https://search.bidcenter.com.cn/search?keywords=&diqu=3&page=count", "replaceKey": "count",
                      "startNum": 1},  # {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath": "",  # 页数区域
        "search": "",
    },

    #吉林省采购招标网
    "jilinshengcaigouzhaobiaowang_3_11_0": {
        # 登陆
        "login": {"button": '//*[@id="login_frm1"]/span[3]/input',
                  "isHasVerify_code": False,
                  "params": [{"type": "id", "name": "username", "value": "jbf"},
                             {"type": "id", "name": "userpwd", "value": "jbf123"}
                             ],
                  "login_status": {"class": "isLogin_byXpath", "params": ""}
                  },
        # start页  进入到显示 标题列表的页
        "startPage": {"type": "onclick",
                      "onclick": [{"button": "",
                                   "params": [],
                                   "url": "http://jilin.gc-zb.com/lists/pid/9.html"
                                   },
                                  ],
                      },
        "li": '//*[@class="news_list"]/p',  # 标题的上一级
        "li_time": "./b/text()",  # 时间
        "title": "./a/@title",  # 标题
        "href": "./a/@href",  # 标题地址
        "domainName_url": "",  # 拼接域名
        "li_area": "",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "http://jilin.gc-zb.com/lists.html?page=count&zz=city_173&keyword=&pid=9&city=0&time=7", "replaceKey": "count",
                      "startNum": 1},  # {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath": "",  # 页数区域
        "search": "",
    },

    #吉林省采购招标网
    "jilinshengcaigouzhaobiaowang_3_11_1": {
        # 登陆
        "login": {"button": '//*[@id="login_frm1"]/span[3]/input',
                  "isHasVerify_code": False,
                  "params": [{"type": "id", "name": "username", "value": "jbf"},
                             {"type": "id", "name": "userpwd", "value": "jbf123"}
                             ],
                  "login_status": {"class": "isLogin_byXpath", "params": ""}
                  },
        # start页  进入到显示 标题列表的页
        "startPage": {"type": "onclick",
                      "onclick": [{"button": "",
                                   "params": [],
                                   "url": "http://jilin.gc-zb.com/lists.html?page=1&zz=city_173&keyword=&pid=11&city=0&time=7"
                                   },
                                  ],
                      },
        "li": '//*[@class="news_list"]/p',  # 标题的上一级
        "li_time": "./b/text()",  # 时间
        "title": "./a/@title",  # 标题
        "href": "./a/@href",  # 标题地址
        "domainName_url": "",  # 拼接域名
        "li_area": "",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "http://jilin.gc-zb.com/lists.html?page=count&zz=city_173&keyword=&pid=11&city=0&time=7", "replaceKey": "count",
                      "startNum": 1},  # {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath": "",  # 页数区域
        "search": "",
    },


    #12辽宁省采购招标网
    "liaoningshengcaigouzhaobiaowang_3_12_0": {
        # 登陆
        "login": {"button": '//*[@id="login_frm1"]/span[3]/input',
                  "isHasVerify_code": False,
                  "params": [{"type": "id", "name": "username", "value": "jbf"},
                             {"type": "id", "name": "userpwd", "value": "jbf123"}
                             ],
                  "login_status": {"class": "isLogin_byXpath", "params": ""}
                  },
        # start页  进入到显示 标题列表的页
        "startPage": {"type": "onclick",
                      "onclick": [{"button": "",
                                   "params": [],
                                   "url": "http://liaoning.gc-zb.com/lists.html?page=1&zz=city_49&keyword=&pid=9&city=0&time=7"
                                   },
                                  ],
                      },
        "li": '//*[@class="news_list"]/p',  # 标题的上一级
        "li_time": "./b/text()",  # 时间
        "title": "./a/@title",  # 标题
        "href": "./a/@href",  # 标题地址
        "domainName_url": "",  # 拼接域名
        "li_area": "",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "http://liaoning.gc-zb.com/lists.html?page=count&zz=city_49&keyword=&pid=9&city=0&time=7", "replaceKey": "count",
                      "startNum": 1},  # {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath": "",  # 页数区域
        "search": "",
    },

    #12辽宁省采购招标网
    "liaoningshengcaigouzhaobiaowang_3_12_1": {
        # 登陆
        "login": {"button": '//*[@id="login_frm1"]/span[3]/input',
                  "isHasVerify_code": False,
                  "params": [{"type": "id", "name": "username", "value": "jbf"},
                             {"type": "id", "name": "userpwd", "value": "jbf123"}
                             ],
                  "login_status": {"class": "isLogin_byXpath", "params": ""}
                  },
        # start页  进入到显示 标题列表的页
        "startPage": {"type": "onclick",
                      "onclick": [{"button": "",
                                   "params": [],
                                   "url": "http://liaoning.gc-zb.com/lists.html?page=1&zz=city_49&keyword=&pid=11&city=0&time=7"
                                   },
                                  ],
                      },
        "li": '//*[@class="news_list"]/p',  # 标题的上一级
        "li_time": "./b/text()",  # 时间
        "title": "./a/@title",  # 标题
        "href": "./a/@href",  # 标题地址
        "domainName_url": "",  # 拼接域名
        "li_area": "",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "http://liaoning.gc-zb.com/lists.html?page=count&zz=city_49&keyword=&pid=11&city=0&time=7", "replaceKey": "count",
                      "startNum": 1},  # {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath": "",  # 页数区域
        "search": "",
    },




    #大连市招标网
    "dalianshizhaobiaowang_3_13": {
        # 登陆
        "login": {"button": "//*[@id='login_login_btn']",
                  "isHasVerify_code": False,
                  "params": [{"type": "id", "name": "txtusername", "value": "13889891148"},
                             {"type": "id", "name": "txtpassword", "value": "jbf123"}
                             ],
                  "login_status": {"class": "isLogin_byXpath", "params": "//*[@id='f_meblg']/ul/li[1]"}
                  },
        # start页  进入到显示 标题列表的页
        "startPage": {"type": "onclick",
                      "onclick": [{"button": "",
                                   "params": [],
                                   "url": "https://search.bidcenter.com.cn/search?diqu=6&darea=%E5%A4%A7%E8%BF%9E"
                                   },
                                  ],
                      },
        "li": '//*[@id="jq_project_list"]/tbody/tr',  # 标题的上一级
        "li_time": "./td[7]/text()",  # 时间
        "title": "./td[2]/a/text()",  # 标题
        "href": "./td[2]/a/@href",  # 标题地址
        "domainName_url": "http:",  # 拼接域名
        "li_area": "./td[5]/text()",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "https://search.bidcenter.com.cn/search?diqu=6&darea=%E5%A4%A7%E8%BF%9E&page=count", "replaceKey": "count",
                      "startNum": 1},  # {"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath": "",  # 页数区域
        "search": "",
    },

    #深圳千里马
    "shenzhenqinglima_3_21_0":{
        #登陆
        "login":{"button":"//*[@id='deng']",
                 "isHasVerify_code":False,
                 "params":[{"type":"id","name":"abc","value":"18602298203"},
                           {"type":"xpath","name":"//*[@id='kuang']/fieldset/input[2]","value":"123456789"}
                           ],
                 "login_status":{"class":"isLogin_byXpath","params":"//*[@id='light']"}
                 },
        #start页  进入到显示 标题列表的页
        "startPage":{"type":"onclick",
                     "onclick":[{"button":"",
                                 "params":[],
                                 "url":"http://www.qianlima.com/zb/area_316_0_1/"
                                 },
                                ],
        },
        "li" : "/html/body/table[8]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td/table/tbody/tr", #标题的上一级
        "li_time" : "./td[3]/text()" , #时间
        "title" : "./td[2]/a/@title", #标题
        "href" : "./td[2]/a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域
        "isloopBytime": True, #是否控制时间循环
        "page_name" : {"type":1,"style":"http://www.qianlima.com/zb/area_316_0_count/","replaceKey":"count","startNum":1},
        "number_xpath" : "/html/body/table[8]/tbody/tr/td[1]/table[5]/tbody/tr/td/font/text()", #页数区域
        "search" : "",
    },

    #深圳千里马
    "shenzhenqinglima_3_21_1":{
        #登陆
        "login":{"button":"//*[@id='deng']",
                 "isHasVerify_code":False,
                 "params":[{"type":"id","name":"abc","value":"18602298203"},
                           {"type":"xpath","name":"//*[@id='kuang']/fieldset/input[2]","value":"123456789"}
                           ],
                 "login_status":{"class":"isLogin_byXpath","params":"//*[@id='light']"}
                 },
        #start页  进入到显示 标题列表的页
        "startPage":{"type":"onclick",
                     "onclick":[{"button":"",
                                 "params":[],
                                 "url":"http://www.qianlima.com/zb/area_316_3_1/"
                                 },
                                ],
        },
        "li" : "/html/body/table[8]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td/table/tbody/tr", #标题的上一级
        "li_time" : "./td[3]/text()" , #时间
        "title" : "./td[2]/a/@title", #标题
        "href" : "./td[2]/a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域
        "isloopBytime": True, #是否控制时间循环
        "page_name" : {"type":1,"style":"http://www.qianlima.com/zb/area_316_3_count","replaceKey":"count","startNum":1},
        "number_xpath" : "/html/body/table[8]/tbody/tr/td[1]/table[5]/tbody/tr/td/font/text()", #页数区域
        "search" : "",
    },


#深圳千里马
    "heilongjiangzhaobiao_3_10":{
        #登陆
        "login":{"button":"//*[@id='deng']",
                 "isHasVerify_code":False,
                 "params":[{"type":"id","name":"abc","value":"18602298203"},
                           {"type":"xpath","name":"//*[@id='kuang']/fieldset/input[2]","value":"123456789"}
                           ],
                 "login_status":{"class":"isLogin_byXpath","params":"//*[@id='light']"}
                 },
        #start页  进入到显示 标题列表的页
        "startPage":{"type":"onclick",
                     "onclick":[{"button":"",
                                 "params":[],
                                 "url":"http://www.qianlima.com/zb/area_316_3_1/"
                                 },
                                ],
        },
        "li" : "/html/body/table[8]/tbody/tr/td[1]/table[4]/tbody/tr[2]/td/table/tbody/tr", #标题的上一级
        "li_time" : "./td[3]/text()" , #时间
        "title" : "./td[2]/a/@title", #标题
        "href" : "./td[2]/a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "",  #区域
        "isloopBytime": True, #是否控制时间循环
        "page_name" : {"type":1,"style":"http://www.qianlima.com/zb/area_316_3_count","replaceKey":"count","startNum":1},
        "number_xpath" : "/html/body/table[8]/tbody/tr/td[1]/table[5]/tbody/tr/td/font/text()", #页数区域
        "search" : "",
    },

    #重庆国际投资咨询集团有限公司
    "chongqingguojitouzizixun_3_26": {"li": '//*[@id="right"]/div[2]/ul/li',
                         "li_time": "./span/text()",  # 时间
                         "title": "./div/a/@title",  # 标题
                         "href": "./div/a/@href",  # 标题地址
                         "domainName_url": "http://cqiic.com/CZJTweb/zbgg",  # 拼接域名
                         "li_area": "",  # 区域
                         "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="Paging"]/div/div/table/tbody/tr/td[text()=count]',"params":[]}]},
                         "number_xpath": '',  # 页数区域
                         "search": "",
                         },

}

