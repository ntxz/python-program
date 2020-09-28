import requests
import bs4


list=[]
def open_url(url):
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51"}
    res = requests.get(url,headers=headers)  #获取网页代码
    return res

def find_data(res):
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    #content = soup.find_all("div",class_="gallery_wrapper")
    content = soup.find(id="hgallery")
    target = content.find_all("img")
    for girl in target:
        link=girl.get("src")
        list.append(link)
    return list
def download_img(url,num):
    # 下载图片
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51"}
    r = requests.get(url, stream=True,headers=headers,allow_redirects=False)
    if r.status_code == 200:
        open('./img_{}.jpg'.format(num), 'wb').write(r.content) # 将内容写入图片
        print("ok")
    else:
        print(r.status_code) # 返回状态码
    del r

def main():
    url="https://www.nvshens.org/g/30991/"
    res=open_url(url)
    data=find_data(res)
    num = 0
    url_list =list
    for url in url_list:
        download_img(url,num)
        num += 1
    #""" with open("res.txt","w",encoding="utf-8") as file:
      #  file.write(res.text) """

if __name__ == "__main__":
    main() 