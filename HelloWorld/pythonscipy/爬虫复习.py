# import requests
# url = 'https://www.baidu.com'
# response = requests.get(url)
# response.content.decode()
#
# print(response)
# print(response.text)

# '''
# @author : cyl
# @file : GetGirlImage
# @time : 2019/06/03
# '''
#
# import requests
# import re
# import os
#
#
# search_key = input("请输入关键字\n")
# headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' ,
#            'Referer': 'https://www.mzitu.com/'}
#
#
#
# response = requests.get('https://www.mzitu.com/search/'+search_key+'/', headers = headers)
# image_field = re.findall('<div class="postlist">([\s\S]*?)<nav class="navigation pagination" role="navigation">', response.text)
#
# # 1.找到每个图片的链接
# img_hrefs = re.findall('<li><a href="(.*?)"', image_field[0])
# name_list = re.findall("alt='(.*?)'", image_field[0])
#
#
# for n in range(len(img_hrefs)):
#
#     # 2.创建对应的文件夹
#     dir_name = name_list[n].replace(' ','')
#
#     if not os.path.exists('./girl_images/'+ dir_name):
#         os.mkdir('./girl_images/'+dir_name)
#
#     # 3.进入链接,并找到页数
#     detail_response = requests.get(img_hrefs[n], headers=headers)
#     tmp_text = re.findall('<div class="pagenavi">([\s\S]*?)</div>', detail_response.text)
#     page_list = re.findall('<span>(\d*?)</span>',tmp_text[0])
#     page_count = int(page_list[-1])
#
#     # 4.获取该图集的每一个链接
#     for page in range(1,page_count+1):
#         page_url = img_hrefs[n]+'/'+str(page)
#         page_response = requests.get(page_url,headers=headers)
#         page_field = re.findall('<div class="main-image">([\s\S]*?)</div>', page_response.text)
#         main_image_url_list = re.findall('<img src="(.*?)"', page_field[0])
#
#         with open('./girl_images/' + dir_name+'/'+ str(page)+'.jpg', 'wb') as image:
#             image.write(requests.get(main_image_url_list[0], headers=headers).content)



import requests
from pyquery import PyQuery as pq
from requests.exceptions import RequestException
import os
from hashlib import md5
from multiprocessing import Pool

headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Referer':'http://jandan.net/ooxx',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie':'__cfduid=d0f8f8aef303ad3b55cd071a426e7a59c1504854664; _ga=GA1.2.986719823.1501079288; _gid=GA1.2.1585289570.1506061387',
}

def get_page(url):
    response=requests.get(url,headers=headers)
    try:
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_page(html):
    doc=pq(html)
    links=doc('.commentlist .row .text p a')
    for link in links:
        image_url='http:'+pq(link).attr('href')
        yield image_url

def download_image(url):
    response=requests.get(url,headers=headers)
    try:
        if response.status_code==200:
            return response.content
        return None
    except RequestException:
        return None

def save_image(content):
    path_name='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(path_name):
        with open(path_name,'wb') as f:
            f.write(content)
            f.close()

def main(page):
    print('===============开始抓取第%r页==============='%page)
    url = 'http://jandan.net/ooxx/page-{}#comments'.format(page)
    html=get_page(url)
    if html:
        urls=parse_page(html)
        for url in urls:
            print('正在下载:%r'%url)
            content=download_image(url)
            save_image(content)


if __name__=='__main__':
    pool=Pool()
    pool.map(main,[page*1 for page in range(1,13)])