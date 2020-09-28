import requests
import bs4
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
res = requests.get("https://movie.douban.com/top250",headers=headers)
soup = bs4.BeautifulSoup(res.text,"html.parser")
targets = soup.find_all("div",class_="hd")  #class是关键字，所以必须加_
for each in targets:
    print(each.a.span.text)
