import requests


url = 'http://127.0.0.1:5000/external-api/test-full2/test-full2/'

resp = requests.post(url=url,
                     json={
                        'appKey': 13,
                        'accessKey': 'my new post',
                     }
                     )


if __name__ == '__main__':
    print(f"resp_1: {resp.url}")
    print(f"resp_1: {resp.status_code}")
    print(f"resp_1: {resp.json()}")











