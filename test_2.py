# https://www.youtube.com/watch?v=3Tm34b7p_cM&t=6s

import requests

url_get = 'https://httpbin.org/get'
url_post = 'https://httpbin.org/post'

headers = {
    "User-Agent": "zapel"
}

params = {
    'a': 'b'
}

json = {
    'username': 'supersecret'
}

"""
GET
"""

resp_get = requests.get(url=url_get,
                        headers=headers,
                        params=params)

"""
POST
"""

resp_post = requests.post(url=url_post,
                          headers=headers,
                          params=params,
                          json=json
                          )


if __name__ == '__main__':
    if resp_get.status_code == 200:
        print('ok')

    if resp_get.ok:
        print('ok')

    print(resp_get.raise_for_status())
    print(resp_get.text)
    print(resp_get.json()['headers']['Host'])

    print("*"*100)

    print(resp_post.text)


