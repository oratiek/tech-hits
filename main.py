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

if __name__ == "__main__":
    qiita_hits = qiita("flask")
    print(qiita_hits)
    zenn_hits = zenn("flask")
    print(zenn_hits)
    sof = stackoverflow("flask")
    print(sof)
