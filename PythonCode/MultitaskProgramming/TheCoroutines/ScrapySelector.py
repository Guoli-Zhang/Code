import requests
from scrapy import Selector


def get_page_items(*, start_page_num: int=1, end_page_num: int=2, step: int=1):
    items = []
    for page_num in range(start_page_num, end_page_num, step):
        base_url = 'https://www.xiuaa.com/qcmn/2062_1.html'
        req = requests.get(base_url.format(genre='cute', page_num=1))
        content = req.content.decode('gbk')
        selector = Selector(text=content)
        item_urls = list(set(selector.css('#maincontent a::attr(href)').extract()))
        items.extend(url for url in item_urls if url.startswith('https://www.xiuaa.com/qcmn/'))
    return items


print(get_page_items())
