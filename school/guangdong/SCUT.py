from urllib import request
import re


import tomxin.getInfo

def getSCUT():
#华南理工大学
#if __name__ == '__main__':
    url = "http://jyzx.6ihnep7.cas.scut.edu.cn/jyzx/xs/zpxx/wlzp/"
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'class="list">','page_detail')
    title = tomxin.getInfo.get_content(info,'_blank">','</a>')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url:
        r_city="广东"
        r_school="华南理工大学"
        r_title=title[i]
        r_trait = "SCUT" + u[-13:]#这里要自己写提取规则
        r_url = "http://jyzx.6ihnep7.cas.scut.edu.cn" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '</h3>', '<div class="close">')
        print(r_title + "\n" + r_url)
        i += 1
