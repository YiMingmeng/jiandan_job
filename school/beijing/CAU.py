from urllib import request
import re


import tomxin.getInfo

def getCAU():
#中国农业大学
# if __name__ == '__main__':
    url = "http://scc.cau.edu.cn/f/recruitmentinfo/frontRecruitinfo"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'recInfoList','pageWrap')
    title = tomxin.getInfo.get_content(info,'eName">','<')
    url = tomxin.getInfo.get_content(info,'href="','"')
    i=0
    for u in url[:]:
        r_title = title[i]
        r_city="北京"
        r_school="中国农业大学"
        r_trait = "CAU" + u[-32:]#这里要自己写提取规则
        r_url = "http://scc.cau.edu.cn" + u
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '<!-- main -->', '<script type="text/javascript">')
        print(r_title + "\n" + r_url)
        i += 1
