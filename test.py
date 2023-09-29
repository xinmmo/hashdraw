
import requests
import http.cookiejar as cookielib
import hashlib
cookies = cookielib.LWPCookieJar(filename='cookies.txt')  #加载cookie
cookies.load(ignore_discard=True, ignore_expires=True)#忽略关闭浏览器丢失，忽略失效
COOKIE_VALUE = requests.utils.dict_from_cookiejar(cookies)['SESSDATA']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Referer': "https://www.bilibili.com/",
    'Cookie' : "SESSDATA=" + COOKIE_VALUE
}
if __name__ == '__main__':
    responce = requests.get(url='https://api.bilibili.com/x/credit/blocked/list?jsonp=jsonp&otype=0&pn=1&ps=1', headers=headers)
    data = responce.json()['data'][0]
    data = data['reasonTypeName']+" " +str(data['originContentModify'])
    print(data)
    hash_object = hashlib.sha256(data.encode('utf-8'))
    print("中奖钥匙为",hash_object.hexdigest())

