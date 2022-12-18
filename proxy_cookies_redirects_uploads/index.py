import requests


url_1 = 'http://ukr.net'
# url_1 = 'https://ukr.net'
url_2 = 'http://httpbin.org/redirect/3'
url_3 = 'http://httpbin.org/absolute-redirect/3'
url_4 = 'https://www.flagman.kiev.ua/?utm_campaign=january&utm_source=domik&utm_medium=banner&utm_content=brands_info'
url_5 = 'http://httpbin.org/anything'

file = 'index.html'
file_large = 'index_large.html'
file_jpg = 'TestRail.png'

proxy = {
    'http': 'localhost:8080',
    'https': 'localhost:8080'
}

headers = {
    'Cookie': 'uid=Cj1tBGD/uaVp4eoZBpTMAg==; snr=9'
}

cookies = {
    'uid': 'Cj1tBGD/uaVp4eoZBpTMAg==',
    'snr': '9'
}

"""
PROXY
"""

resp_proxy = requests.get(url=url_1, proxies=proxy, verify=False)


"""
COOKIES
"""

resp_cookies = requests.get(url=url_1, proxies=proxy, verify=False)

"""send cookies"""
resp_cookies_headers = requests.get(url=url_1, proxies=proxy, headers=headers, verify=False)
resp_cookies_cookies = requests.get(url=url_1, proxies=proxy, cookies=cookies, verify=False)


"""
REDIRECT/TIMEOUT
http://httpbin.org/redirect/ do not work
"""

resp_redirect = requests.get(url=url_2, proxies=proxy)
resp_redirect_absolute = requests.get(url=url_3, proxies=proxy, allow_redirects=True)
resp_redirect_timeout = requests.get(url=url_2, proxies=proxy, timeout=1)


"""
DOWNLOAD
"""

def download(url, file):
    resp = requests.get(url=url, proxies=proxy, verify=False)
    
    with open(file, 'wb') as f:
        f.write(resp.content)

def download_chunk(url, file):
    resp = requests.get(url=url, proxies=proxy, verify=False, stream=True)

    with open(file, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            print('CHUNK!')
            f.write(chunk)


"""
UPLOAD
"""

def upload(url, file):
    with open(file, 'rb') as f:
        requests.post(url=url, proxies=proxy, data=f)




if __name__ == '__main__':
    print(resp_proxy.status_code)
    print('*' * 130)

    print(resp_cookies.cookies.items())
    print(resp_cookies_cookies.cookies.items())
    print(resp_cookies_headers.cookies.items())
    print('*' * 130)

    print(resp_redirect.history)
    print(resp_redirect_absolute.history)
    print(resp_redirect_timeout.history)
    print('*' * 130)

    # download(url_1, file)
    # download_chunk(url_4, file_large)
    upload(url_5, file_jpg)







