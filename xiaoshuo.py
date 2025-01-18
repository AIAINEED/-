import requests
from lxml import etree
import time
import random

url = 'https://1ba44f862155cb3a165498.bi54.cc/html/230373/1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

while True:
    try:
        # 添加随机延迟
        time.sleep(random.uniform(1, 3))
        
        # 发送请求
        resp = requests.get(url, headers=headers)
        e = etree.HTML(resp.text)
        
        # 提取章节标题和内容
        title = e.xpath('//span/text()')[0]
        info = '\n'.join(e.xpath('//div[@class="Readarea ReadAjax_content"]/text()'))
        
        # 将章节标题和内容写入文件
        with open('夜无疆.txt', 'a', encoding='utf-8') as f:
            f.write(title + '\n\n' + info + '\n\n')
        
        print(f"已爬取: {title}")
        
        # 提取下一页的链接
        next_page = e.xpath('//a[@id="pb_next"]/@href')
        print("下一页链接:", next_page)  # 调试：打印下一页链接
        
        # 检查是否有下一页
        if not next_page:
            print("已到达最后一章，爬取结束。")
            break
        
        # 更新 URL
        url = f"https://1ba44f862155cb3a165498.bi54.cc{next_page[0]}"
        print("下一页 URL:", url)  # 调试：打印下一页的完整 URL
    
    except Exception as e:
        print(f"发生错误: {e}")
        break