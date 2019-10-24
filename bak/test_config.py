# -*- coding: utf-8 -*-
import datetime

#配置xpath
from fake_useragent import UserAgent

today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))
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
    "shanxishenzhaobiaogonggongfuwupingtai" : {"li" : '//ul[@class="on"]//table[@class="download_table"]//tr' , #标题的上一级
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
                          "page_name" : {"type":1,"style":"http://www.zybtp.com/ggxx/index_count.jhtml","startNum":1}, #页数  index_pageNo.jhtml
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
                                           'Accept': '*/*',
                                           'Accept-Encoding': 'gzip, deflate',
                                           'Accept-Language': 'zh-CN,zh;q=0.9',
                                           'Connection': 'keep-alive',
                                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                           'Origin': 'http://www.hebeieb.com',
                                           'Referer': 'http://www.hebeieb.com/tender/xxgk/list.do?selectype=zbgg',
                                           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
                                           'X-Requested-With': 'XMLHttpRequest',
                                           'Cookie':'JSESSIONID=73417900EA05C1C288F37A7A9EDEA197; __51cke__=; __tins__19687679=%7B%22sid%22%3A%201571627619812%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201571629503848%7D; __51laig__=2'
                                           },
                                       "data":{
                                           "page": "0",
                                           "TimeStr": yesterday+","+yesterday,
                                           "AllPtName": "",
                                           "KeyStr": "",
                                           "KeyType": "ggname"
                                           },                                       
                                       "post_url":"http://www.hebeieb.com/tender/xxgk/zbgg.do",
                                       }, #页数  index_pageNo.jhtml
                                   "number_xpath" : '//*[@id="zbggPagination"]/a[4]/text()', #页数区域
                                   "search" : "",                                               
                                                                                                        
                                   },
#内蒙古自治区政府采购网
    "neimengguzizhiquzhengfucaigou":{"li" : "//*[@id='itemContainer']/tbody/tr", #标题的上一级
                          "li_time" : "./td[@class='feed-time']/span/text()" , #时间
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
    #天津市政府采购平台 post
    "tianjinshizhengfucaigoupingtai" : {"li" : '//*[@id="reflshPage"]/ul/li',
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
                                     },  # 页数  index_pageNo.jhtml
                                     "number_xpath": '//*[@id="pagesColumn"]/div/span[2]/b/text()',  # 总区域
                                     "search": "",

                                     },

    # 内蒙古自治区公共资源交易平台  todo
    "neimengguzizhiqugonggongziyuanjiaoyiwang": {"li": '/html/body/div[2]/div[2]/div/div[4]/table/tbody//tr',
                                       "li_time": "./td[4]/text()",  # 时间
                                       "title": "./td[3]/a/@title",  # 标题
                                       "href": "./td[3]/a/@href",  # 标题地址
                                       "domainName_url": "http://ggzyjy.nmg.gov.cn",  # 拼接域名
                                       "li_area": "",  # 区域
                                       "page_name" : {"type":1,"style":"http://ggzyjy.nmg.gov.cn/jyxx/jsgcZbgg?currentPage=count","startNum":1}, #页数
                                       "number_xpath": '/html/body/div[2]/div[2]/div/div[5]/div/a[7]/text()', # 页数区域
                                       "search": "",
                                     },
    # 5山东省政府采购信息公开平台 get
    "shandongshengzhengfucaigouxinxigongkaipingtai": {"li": '/html/body/table[4]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[5]/td[2]/table/tbody/tr[position()<21]//td[@class="Font9"]',
                                                      "li_time": "./text()[2]",  # 时间  todo :时间格式不对
                                                      "title": "./a/@title",  # 标题
                                                      "href": "./a/@href",  # 标题地址
                                                      "domainName_url": "http://www.ccgp-shandong.gov.cn",  # 拼接域名
                                                      "li_area": "",  # 区域
                                                       "page_name" : {
                                                            "type":2,
                                                            "style":"post",
                                                            "startNum":1,
                                                            "headers":{
                                                            #'Accept': '*/*',
                                                            #'Accept-Encoding': 'gzip, deflate',
                                                            #'Accept-Language': 'zh-CN,zh;q=0.9',
                                                            #'Connection': 'keep-alive',
                                                            #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                                            #'Origin': 'http://www.hebeieb.com',
                                                            #'Referer': 'http://www.hebeieb.com/tender/xxgk/list.do?selectype=zbgg',
                                                            'User-Agent': UserAgent().chrome,
                                                            #'X-Requested-With': 'XMLHttpRequest',
                                                            #'Cookie':'JSESSIONID=73417900EA05C1C288F37A7A9EDEA197; __51cke__=; __tins__19687679=%7B%22sid%22%3A%201571627619812%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201571629503848%7D; __51laig__=2'
                                                        },
                                                        "data":{
                                                            "page": "curgage",
                                                            "TimeStr": yesterday+","+yesterday,
                                                            "AllPtName": "",
                                                            "KeyStr": "",
                                                            "KeyType": ""
                                                        },
                                                        "post_url":"http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp",
                                                        "pageNoKey":"curpage"
                                                        },
                                                       "number_xpath": '//*[@id="page"]/option[1759]/text()', # 页数区域
                                                       "search": "",
                                                       },

    #6 上海公共资源交易网
    "shanghaigonggongziyuanjiaoyiwang" :{"li": '/html/body/div[5]/div[1]/div[4]/div[2]/table/tbody/tr',
                                         "li_time": "./td[5]/text()",  # 时间
                                          "title": "./td[1]/a/@title",  # 标题
                                          "href": "./td[1]/a/@href",  # 标题地址
                                          "domainName_url": "http://www.zgazxxw.com",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://www.zgazxxw.com/sh-000012-count.html","replaceKey":"count","startNum":1},
                                          "number_xpath": '/html/body/div[5]/div[1]/div[5]/div[1]/a[last()]/@href', # 页数区域
                                          "search": "",
                                        },

#11 广西招标投标公共服务平台
    "guangxizhaobiaotoubiaogonggongfuwupingtai" :{"li": '/html/body/table/tbody/tr[position()>1]',
                                         "li_time": "./td[5]/text()",  # 时间
                                          "title": "./td[1]/a/@title",  # 标题
                                          "href": "./td[1]/a/@href",  # 标题地址
                                          "domainName_url": "http://ztb.gxi.gov.cn/",  # 拼接域名
                                          "li_area": "./td[3]/span/@title",  # 区域
                                          "page_name" : {"type":1,"style":"http://zbtb.gxi.gov.cn:9000/xxfbcms/category/bulletinList.html?searchDate=1994-10-23&dates=300&word=&categoryId=88&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=1&page=count","replaceKey":"count","startNum":1},
                                          "number_xpath": '/html/body/div[2]/a[2]/@onclick', # 页数区域
                                          "search": "",

                                        },

#12 海南省公共资源交易网
    "hainanshenggonggongziyuanjiaoyiwang" :{"li": '/html/body/div[5]/div[1]/div[4]/div[2]/table/tbody/tr',
                                         "li_time": "./td[5]/text()",  # 时间
                                          "title": "./td[1]/a/@title",  # 标题
                                          "href": "./td[1]/a/@href",  # 标题地址
                                          "domainName_url": "http://www.zgazxxw.com",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://www.zgazxxw.com/hi-001012l772-count.html","replaceKey":"count","startNum":0},
                                          "number_xpath": '/html/body/div[5]/div[1]/div[5]/div[1]/a[last()]/@href', # 页数区域
                                          "search": "",
                                        },



    }



    


