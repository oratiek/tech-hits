import requests
from bs4 import BeautifulSoup
import re

def qiita(keyword):
    query = f"https://qiita.com/search?q={keyword}"
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'html.parser')
    span = soup.find("span", class_="style-ro5zzw")
    result = re.search(r'\d+', span.text)
    hit_num = int(result.group())
    return hit_num

def zenn(keyword):
    query = f"https://zenn.dev/search?q={keyword}"
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'html.parser')
    span = soup.find("span", class_="WithKeywordContent_tabLinkCount__n9jPY")
    return int(span.text)

def stackoverflow(keyword):
    query = f"https://stackoverflow.com/questions/tagged/{keyword}"
    res = requests.get(query)
    soup = BeautifulSoup(res.text, 'html.parser')
    div = soup.find("div", class_="fs-body3 flex--item fl1 mr12 sm:mr0 sm:mb12")
    result = re.search(r'.*\d+', div.text)
    hit_num = result.group()
    if "," in hit_num:
        comma_index = hit_num.find(",")
        hit_num = hit_num[0:comma_index] + hit_num[comma_index+1:]
    return int(hit_num)

engines = [qiita, zenn, stackoverflow]
names = ["qiita", "zenn", "stackoverflow"]

def search(keyword):
    res = []
    for keyword in keywords:
        tmp = {"keyword":keyword,"res":{}}
        for i in range(len(engines)):
            hit_num = engines[i](keyword)
            tmp["res"][names[i]] = hit_num
        res.append(tmp)
    return res

if __name__ == "__main__":
    keywords = ["flask","django"]
    res = search(keywords)
    print(res)
