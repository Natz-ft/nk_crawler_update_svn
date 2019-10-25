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
                          "page_name" : {"type":1,"style":"http://www.zybtp.com/fwzb/index_count.jhtml","replaceKey":"count","startNum":1}, #页数  index_pageNo.jhtml
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
<<<<<<< .mine


    #3天津市政府采购平台 post
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
                                         "pageNoKey":"page"
                                     },  # 页数  index_pageNo.jhtml
                                     "number_xpath": '//*[@id="pagesColumn"]/div/span[2]/b/text()',  # 总区域
                                     "search": "",
                                     "type"  : "招标"

                                     },

    # 4内蒙古自治区公共资源交易平台  todo
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

    #7 上海公共资源交易网
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
     #8 浙江省公共资源交易网
    "zhejiangshenggonggongziyuanjiaoyiwang" :{"li" : '/html/body/div/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/div/table/tbody/tr'    ,
                                         "li_time": "./td[3]/text()",  # 时间
                                          "title": "./td[2]/a/@title",  # 标题
                                          "href": "./td[2]/a/@href",  # 标题地址
                                          "domainName_url": "http://new.zmctc.com/zjgcjy/",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://new.zmctc.com/zjgcjy/jyxx/004001/004001003/?Paging=count","replaceKey":"count","startNum":1},
                                          "number_xpath": '/html/body/div/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/div/div/div/table/tbody/tr/td[23]/@title', # 页数区域
                                          "search": "",
            },
    #9 江苏政府采购网
    "jiangsuzhengfucaigouwang" :{"li" : '//*[@id="newsList"]/ul/li' ,
                                         "li_time": "./text()[2]",  # 时间
                                          "title": "./a/text()",  # 标题
                                          "href": "./a/@href",  # 标题地址
                                          "domainName_url": "http://new.zmctc.com/zjgcjy/",  # 拼接域名
                                          "li_area": "",  # 区域
                                           "page_name" : {"type":1,"style":"http://www.ccgp-jiangsu.gov.cn/ggxx/gkzbgg/index_count.html","replaceKey":"count","startNum":1},
                                          "number_xpath": '//*[@id="newsPage"]/div/a[2]/@href', # 页数区域
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
                                          "type" : "招标"
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



#14 安招采网
    "anzhaocai": {"li": '//*[@id="gridcontainer1"]/div/div[1]/div[position()>1]',  # 标题的上一级
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
    #15江西国政招标有限公司
        "jiangxiguozhengzhaobiaoyouxiangongsi" :{"li": '/html/body/div[3]/div/div/div[2]/ul/li',
                                             "li_time": "./span/text()",  # 时间
                                              "title": "./a/@title",  # 标题
                                              "href": "./a/@href",  # 标题地址
                                              "domainName_url": "http://www.jxgzzb.com.cn",  # 拼接域名
                                              "li_area": "",  # 区域
                                               "page_name" : {"type":1,"style":"http://www.jxgzzb.com.cn/Index/notice/inftype/1/page/count.html","replaceKey":"count","startNum":1},
                                              "number_xpath": '/html/body/div[3]/div/div/div[2]/div[2]/ul/li[8]/a/text()', # 页数区域
                                              "search": "",
                                            },



    #18成都公共资源交易中心
    "chengdushigonggongziyuanjiaoyizhongxin" : {"li" : '//*[@id="contentlist"]/div', #标题的上一级
                          "li_time" : "./div[3]/div[1]/text()" , #时间
                          "title" : "./div[2]/a/text()", #标题
                          "href" : "./div[2]/a/@href", #标题地址
                          "domainName_url" : "https://www.cdggzy.com", #拼接域名
                          "li_area": "./div[1]/text()",  #区域
                          "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":2,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="Pager"]/a[text()=count]',"params":[]}]
                                       },
                          "number_xpath" : '//*[@id="Pager"]/a[13]/@href', #页数区域
                          "search" : "",

                          },

    #19 中国邮政
        "zhongguoyouzheng" :{"li": '//*[@id="Content3"]/div[2]/ul/li[position()<21]',
                                             "li_time": "./span[2]/text()",  # 时间
                                              "title": "./span[1]/a/@title",  # 标题
                                              "href": "./span[1]/a/@href",  # 标题地址
                                              "domainName_url": "http://www.chinapost.com.cn",  # 拼接域名
                                              "li_area": "",  # 区域
                                               "page_name" : {"type":1,"style":"http://www.chinapost.com.cn/html1/category/181313/7338-count.htm","replaceKey":"count","startNum":1},
                                              "number_xpath": '//*[@id="CBLast"]/@href', # 页数区域
                                              "search": "",
                                            },
    # 20 兵团政府采购网
    "bingtuanzhengfucaigouwang": {"li": '/html/body/div[3]/div[2]/div[2]/div/div[2]/ul/li',
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
||||||| .r432
=======
    #福建省公共资源交易中心
    "fujianshengonggongziyuanjiaoyi":{
        "li" : "//*[@id='itemContainer']/tbody/tr", #标题的上一级
        "li_time" : "./td[@class='feed-time']/span//text()" , #时间
        "title" : "./td[@class='title']/a/@title", #标题
        "href" : "./td[@class='title']/a/@href", #标题地址
        "domainName_url" : "", #拼接域名
        "li_area": "./td[2]/span/text()",  #区域        
        },
    
    #千里马
    "qinglima":{
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
                                 "url":"http://www.qianlima.com/zb/area_26_0_1/"
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
        "page_name" : {"type":1,"style":"http://www.qianlima.com/zb/area_26_0_count/","replaceKey":"count","startNum":1},
        "number_xpath" : "/html/body/table[8]/tbody/tr/td[1]/table[5]/tbody/tr/td/font/text()", #页数区域
        "search" : "",              
    }, 
    ##吉林招标网   非会员只能看免费信息type=0（只有招标）time=7  一周(30 月...)  (会员：招标信息（type=1），中标信息（type=4))
    ##登陆异常验证： 滑动条形框
    #"jilinzhaobiao":{
        ##登陆
        #"login":{"button":"//*[@id='login_login_btn']",
                 #"isHasVerify_code":False,
                 #"params":[{"type":"id","name":"txtusername","value":"13889891148"},
                           #{"type":"id","name":"txtpassword","value":"jbf123"}
                           #],
                 #"login_status":{"class":"isLogin_byXpath","params":"//*[@id='f_meblg']/ul/li[1]"}
                 #},
        ##start页  进入到显示 标题列表的页
        #"startPage":{"type":"onclick",
                     #"onclick":[{"button":"",
                                 #"params":[],
                                 #"url":"https://search.bidcenter.com.cn/search?diqu=7&time=7&type=0&page=1"
                                 #},                                
                                #],
        #},
        
        #"li" : "//table/tbody/tr", #标题的上一级
        #"li_time" : "./td[4]/text()" , #时间
        #"title" : "./td[1]/a/@title", #标题
        #"href" : "./td[1]/a/@href", #标题地址
        #"domainName_url" : "https://jl.bidcenter.com.cn", #拼接域名
        #"li_area": "",  #区域
        #"isloopBytime": True, #是否控制时间循环
        #"page_name" : {"type":0,"style":r'page=\d+',"startNum":1},
        #"number_xpath" : "", #页数区域
        #"search" : "",              
    #},
>>>>>>> .r433
}

