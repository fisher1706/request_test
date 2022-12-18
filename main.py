import requests

if __name__ == '__main__':
    url = 'http://localhost:9090/commission/purchase'


    headers = {
        'Content-Type': "application/json",
        # 'User-Agent': "PostmanRuntime/7.15.0",
        # 'Accept': "*/*",
        # 'Cache-Control': "no-cache",
        # 'Postman-Token': "99c061e5-a3c7-403b-b5ef-77b857879093,e0810f55-51cf-47fb-8971-3e6003f2686a",
        # 'Host': url,
        # 'accept-encoding': "gzip, deflate",
        # 'content-length': "35",
        # 'Connection': "keep-alive",
        # 'cache-control': "no-cache"
    }

    data = {
        "transaction_id": 9001485176
    }

    resp = requests.post(
        url=url,
        headers=headers, json=data)

    print(resp.text)

    ids = ['8905', '12951']
    data = ','.join(i for i in ids)
    print(data)