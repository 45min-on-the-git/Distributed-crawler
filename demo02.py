import urllib.request
import random
from lxml import etree

#（1）请求对象的定制及请求访问
def create_request(page):
    if page==1:
        url = 'https://sc.chinaz.com/tupian/meishitupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/meishitupian_'+ str(page) +'.html'        
    headers = {
        'User-Agent':'',
        'Cookie':''
    }
    request = urllib.request.Request(url = url,headers = headers)
    
    return request

    
#（2）获取服务器响应数据
def get_content(request):
    
    
#+------------------------------------------------------------------------------------------------------------------------+
    #校验时间 2022-8-15  14:56 ,若代理池不可用，注释掉分割线内的内容，并将分割线下方的response取消注释
    free_proxies_pool = [
        {'http':'223.94.85.131:9091'},
        {'http':'217.60.194.52:8080'},
        {'http':'79.122.202.21:8080'},
        {'http':'18.130.252.7:8888'},
        {'http':'36.94.174.243:8080'},
        {'http':'103.119.67.41:3125'},
    ]
    proxies = random.choice(free_proxies_pool)
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
#+------------------------------------------------------------------------------------------------------------------------+   
    
    
    #response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

#（3）下载及清洗数据
def download_clean(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="item"]/img/@alt')
    src_list = tree.xpath('//div[@class="item"]/img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:'+src
        print(name)
        print(url)
        urllib.request.urlretrieve(url=url,filename=name+'.jpg')

if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1,1):
        request = create_request(page)
        content = get_content(request)
        download_clean(content)