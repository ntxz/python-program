import requests

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


if __name__ == '__main__':
    # 下载要的图片
    url_list = ['https://img.tupianzj.com/uploads/allimg/140710/1-140G01010250-L.jpg', 'https://img.tupianzj.com/uploads/allimg/202009/9999/54e62bb14f.jpg', 'https://img.tupianzj.com/uploads/allimg/202008/9999/0844e1056b.jpg', 'https://img.tupianzj.com/uploads/200423/30-2004231035195T.jpg', 'https://img.tupianzj.com/uploads/allimg/202004/9999/rn36a341917b.jpg', 'https://img.tupianzj.com/uploads/allimg/202003/9999/rn18909b92fa.jpg', 'https://img.tupianzj.com/uploads/allimg/202003/9999/rnd2a8013b09.jpg', 'https://img.tupianzj.com/uploads/allimg/202002/9999/rn18909b92fa.jpg', 'https://img.tupianzj.com/uploads/allimg/202001/9999/rn74ed1af175.jpg', 'https://img.tupianzj.com/uploads/allimg/200224/30-2002241013470-L.jpg', 'https://img.tupianzj.com/uploads/allimg/200219/30-20021Z920270-L-lp.jpg', 'https://img.tupianzj.com/uploads/allimg/190617/29-1Z61G621090-L.jpg', 'https://img.tupianzj.com/uploads/allimg/201908/9999/rn03c2672c6b.jpg', 'https://img.tupianzj.com/uploads/allimg/200211/29-2002111420430-L.jpg', 'https://img.tupianzj.com/uploads/allimg/202001/9999/rn53d6a6fbdc.jpg', 'https://img.tupianzj.com/uploads/allimg/201907/9999/rn6fbcd942b8.jpg']
    num = 0
    for url in url_list:
        download_img(url,num)
        num += 1