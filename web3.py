# web2.py 
#웹크롤링 
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request

for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    #웹서버에 요청해서 실행된 문자열 받기 
    data = urllib.request.urlopen(url)
    #검색할 객체
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text.strip()
        print(title)
