import requests


url = 'http://127.0.0.1:5000/HttpServices/api/inner/9001539162'

data = {
    'code': 'CHABAC ZAPEL'
}

resp = requests.post(url=url, json=data)


if __name__ == '__main__':
    print(resp.json())