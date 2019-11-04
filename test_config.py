# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
import datetime
today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))
today = str(today)

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
                                 "url":"https://jl.bidcenter.com.cn/diqumore-1-1-1.html"
                                 },                                
                                ],
        },
        
        "li" : "//table/tbody/tr", #标题的上一级
        "li_time" : "./td[4]/text()" , #时间
        "title" : "./td[1]/a/@title", #标题
        "href" : "./td[1]/a/@href", #标题地址
        "domainName_url" : "https://jl.bidcenter.com.cn", #拼接域名
        "li_area": "",  #区域
        "isloopBytime": True, #是否控制时间循环
        "page_name" : {"type":1,"style":"https://jl.bidcenter.com.cn/diqumore-1-1-count.html","replaceKey":"count","startNum":1},#{"type":0,"style":r'page=\d+',"startNum":1},
        "number_xpath" : "", #页数区域
        "search" : "",
    },


#zl excel colomn3
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
                                                       "page_name" : {
                                                            "type":2,
                                                            "style":"post",
                                                            "startNum":1,
                                                            "headers":{
                                                                'User-Agent': UserAgent().chrome,
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
                                                      "page_name": {
                                                          "type": 2,
                                                          "style": "post",
                                                          "startNum": 1,
                                                          "headers": {
                                                              'User-Agent': UserAgent().chrome,
                                                          },
                                                          "data": {
                                                              "page": "curgage",
                                                              "TimeStr": yesterday + "," + yesterday,
                                                              "AllPtName": "",
                                                              "KeyStr": "",
                                                              "KeyType": ""
                                                          },
                                                          "post_url": "http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp",
                                                          "pageNoKey": "curpage"
                                                      },
                                                      "number_xpath": '//*[@class = "Font9"]/strong/text()',  # 页数区域
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
    "hunanguolianzhaobiaoyouxiangongsi_3_22_0": {"li": '//*[@id="gridcontainer1"]/div/div[1]/div[position()>1]',  # 标题的上一级
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
                                  "li_time": "./span[3]/text()",  # 时间
                                  "title": "./td[1]/@title",  # 标题
                                  "href": "",  # 标题地址 //todo 16-云南招标-找不到链接
                                  "domainName_url": "http://www.yngp.com",  # 拼接域名
                                  "li_area": "./td[3]/@title",  # 区域
                                   "page_name" : {
                                       "type":3,
                                       "style":"onclick",
                                       "startNum":1,
                                       "onclick":[{"replaceKey":"count","button":'//*[@id="bulletinlistid-footer"]/div/div[1]/ul/li/a[text()=count]',"params":[]}]
                                       },
                                  "number_xpath": '//*[@id="bulletinlistid-footer"]/div/div[1]/ul/li/text()',  # 页数区域
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
    #河北省招标网
    "hebeizhaobiaocaigouwang_3_9_0": {
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
        "li": '//*[@id="center_box"]/div/div[2]/div[2]/div[1]/p',  # 标题的上一级
        "li_time": "./b/text()",  # 时间
        "title": "./a/@title",  # 标题
        "href": "./a/@href",  # 标题地址
        "domainName_url": "",  # 拼接域名
        "li_area": "",  # 区域
        "isloopBytime": True,  # 是否控制时间循环
        "page_name": {"type": 1, "style": "http://jilin.gc-zb.com/lists.html?page=count1&zz=city_173&keyword=&pid=9&city=0&time=7", "replaceKey": "count",
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



}

