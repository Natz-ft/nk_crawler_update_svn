# test.py line 26-33
````
ori_number = model.number_page(parame["number_xpath"], html_str)
#ori_number = re.search('5.{3}' ,ori_number)
number = ''.join(re.findall(r'\d+页', ''.join(ori_number))).replace("页","")
if len(number)==0:
    number = ''.join(re.findall(r'\d+', ''.join(ori_number)))
number = int(number) + 1
 ````           
 r'\d+页' r表示原生字符串
 join()函数 效果 返回一个字符串 ： {'.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs' }



````
    def number_page(self,number_xpath, page_html_str):
        # 把html字符串转换成element对象
        html_element = etree.HTML(page_html_str)
        number = html_element.xpath(number_xpath)
        return number



    a=[1, 2]
    >>> type(a)
    <class 'list'>
``````
 etree.html() 效果 ：构造xpath对象 
 number 是list对象
 ````
 X[start:end:span]
 
 遍历 [start,end)，间隔为 span，当 span>0 时顺序遍历, 当 span<0 时，逆着遍历。
start 不输入则默认为 0，end 不输入默认为长度。
````


get_title_list 
先进行时间判断，时间属于昨天，就对标题进行过滤，标题符合，采集标题/链接/地区存进 存进字典，输出采集信息，返回true

````
getAreaFromStr(item_title)
range(start,stop,step)
返回[start，start+step，... stop-1]
````

````
re.compile
tmp_str = pattern_n.findall(area.area_str)
返回的是一个匹配对象，它单独使用就没有任何意义，需要和findall(), search(), match(）搭配使用。
````