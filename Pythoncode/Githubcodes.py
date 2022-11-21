# 返回下载链接
import requests 


# 返回github api下载链接
def getGithuburl(apiurl):
    response = requests.get(apiurl)
    assets_url = response.json()["assets_url"]
    response1 = requests.get(assets_url)
    r = response1.json()
    for i in r :
        return i["browser_download_url"]