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

if __name__ == "__main__":
    qiita_hits = qiita("flask")
    print(qiita_hits)
