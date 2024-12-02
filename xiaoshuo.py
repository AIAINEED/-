import requests
from lxml import etree

url = 'https://1ba44f862155cb3a165498.bi54.cc/html/230373/1.html'
while True:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    resp = requests.get(url, headers=headers)

    e = etree.HTML(resp.text)
    info= '\n'.join(e.xpath('//div[@class="Readarea ReadAjax_content"]/text()'))
    title= e.xpath('//span/text()')[0]
    url = f"https://1ba44f862155cb3a165498.bi54.cc{e.xpath('//div[@class="Readpage_down js_readpage_down"]/a[3]/@href')[0]}"

    print(title)
    # print(info)
    # with open('夜无疆.txt', 'w', encoding='utf-8') as f:
    #     f.write(title+'\n\n'+info+'\n\n')

    