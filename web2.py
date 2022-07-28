# web2.py 
#웹크롤링 
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request

#웹서버에 요청해서 실행된 문자열 받기 
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색할 객체
soup = BeautifulSoup(data, "html.parser")
# <td class="title">
# 	<a href="/webtoon/detail?titleId=20853">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)