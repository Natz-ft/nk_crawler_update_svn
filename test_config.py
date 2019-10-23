# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
import datetime
today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))
today = str(today)

#配置xpath
parameter = {
    #中化
    "sinochemitc" : {"li" : '//*[@id="tab1"]/ul/li' , #标题的上一级
                     "li_time" : "./p/text()" , #时间
                     "title" : "./a/text()", #标题
                     "href" : "./a/@href", #标题地址
                     "domainName_url" : "http://e.sinochemitc.com", #拼接域名
                     "li_area": "",  #区域
                     "page_name" :  {"type":0,"style":r'pageNo=\d+',"startNum":1}, #有问题，需要测试   #页数
                     "number_xpath" : '//div[@class="pag-link"]/a[7]/text()', #页数区域
                     "search" : "",


                     },
    #中国人民财产保险
    "zhongguorenminbaoxian" : {"li" : '//div[@class = "contentBox"]/div' , #标题的上一级
                             "li_time" : "./div[3]/text()" , #时间
                             "title" : "./div[2]/a/text()", #标题
                             "href" : "./div[2]/a/@href", #标题地址
                             "domainName_url" : "http://caigou.epicc.com.cn", #拼接域名
                             "li_area": "",  #区域
                             "page_name" :  {"type":0,"style":r'page=\d+',"startNum":1}, #页数
                             "number_xpath" : '//div[@class="page"]/div/span[3]/text()', #页数区域
                             "search" : { "sendTimeMin" : yesterday ,"sendTimeMax" : yesterday, "page" : "1"},

                             
                     },
    #内蒙古招标   "没信息"
    "neimengguzhaobiao" : {"li" : '//table[@class="table_text"]/tbody/tr' , #标题的上一级
                               "li_time" : "./td[5]/text" , #时间
                             "title" : "./td[1]/a/text()", #标题
                             "href" : "./td[1]/a/@href", #标题地址
                             "domainName_url" : "", #拼接域名
                             "li_area": "./td[3]/span/text()",  #区域
                             "page_name" :  {"type":0,"style":r'page=\d+',"startNum":1}, #页数
                             "number_xpath" : '//div[@class="pagination"]/label[1]/text()', #页数区域
                             "search" : { "searchDate" : "1994-10-17" ,"dates" : "300", "categoryId" : "88", "startcheckDate" : yesterday, "endcheckDate" : yesterday , "page" : "1"},

                             
                             },
    #山东省采购与招标网
    "shangdongcaigouyuzhaobiao" : {"li" : '//div[@class="listmian"]//tr' , #标题的上一级
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
    "shanxishenzhaobiaogonggongfuwupingtai" : {"li" : '//ul[@class="on"]//table[@class="download_table"]/tbody/tr' , #标题的上一级
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
    "zhongyuanzhaocai" : {"li" : '//div[@class="List3 Top18"]/ul/li' , #标题的上一级
                          "li_time" : "./span[@class='time']/text()" , #时间
                          "title" : "./a/text()", #标题
                          "href" : "./a/@href", #标题地址
                          "domainName_url" : "", #拼接域名
                          "li_area": "",  #区域
                          "page_name" : {"type":1,"style":"http://www.zybtp.com/ggxx/index_count.jhtml","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
                          "number_xpath" : '//div[@class="Top8 TxtCenter"]/div[2]/a[4]/@href', #页数区域
                          "search" : "",
                          
                          },
    
    #河北省招标投标公共服务平台 页面内跳转  post请求
    "heibeishenzhaobiaotoubiao" : {"li" : '//div[@class="publicont"]/div' , #标题的上一级
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
    "heilongjiangcaigou" : {"li" : "//div[@class='xxei']", #标题的上一级
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
    "guangdongshenzhengfucaigou":{"li" : "//ul[@class='m_m_c_list']/li", #标题的上一级
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
}

