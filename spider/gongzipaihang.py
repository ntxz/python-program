import requests
import bs4
import re
import openpyxl

def open_url(url):
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51"}
    res = requests.get(url,headers=headers)  #获取网页代码
    return res

def find_date(res):
    data=[]
    soup = bs4.BeautifulSoup(res.text,"html.parser") #解析网页，括号为解析方式parser为默认 lxml解析器更强大
    content = soup.find(id="Cnt-Main-Article-QQ")
    target = content.find_all("p",style="TEXT-INDENT: 2em")
    target=iter(target) #使用iter函数将target变为迭代器
    for each in target:
        if each.text.isnumeric():
            data.append([
                re.search(r'\[(.+)\]',next(target).text).group(1),     #\[(.+)\]正则表达式，选中中括号\[\]里的所有内容(.+)
                re.search(r'\d.*',next(target).text).group(),          #使用正则表达式选中数字后的所有内容
                re.search(r'\d.*',next(target).text).group(),
                re.search(r'\d.*',next(target).text).group(),
            ])
            return data
        #print(each.text)

def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types=True
    ws = wb.active
    ws.append(['城市','平均房价','平均工资','房价工资比'])
    for each in data:
        ws.append(each)
        
    wb.save("2017年中国主要城市房价工资比排行榜.xlsx")

def main():
    url = "https://news.house.qq.com/a/20170702/003985.htm"
    res = open_url(url)
    data = find_date(res)
    to_excel(data)
    #''' with open("text.txt","w",encoding="utf-8") as file:
    #   file.write(res.text) '''
    

if __name__=="__main__":
    main()