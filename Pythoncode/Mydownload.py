import os
import requests
from urllib.parse import urlparse

# 下载位置  URL
def Mydownload(root , url):
    fileend = False
    filename = os.path.basename(urlparse(url).path)
    fileend = os.path.splitext(filename)[-1]
    path = root + filename
    if fileend == False: path += ".未确定文件.file"
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as fq:
                fq.write(r.content)
                print("成功")
        else:
            print('文件已存在')
    except Exception as e :
        print("出现异常" , e)

