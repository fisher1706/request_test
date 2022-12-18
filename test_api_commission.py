import requests

url = 'http://localhost:9090/commission/purchase'

resp = requests.post(url=url,
                     json={"transaction_id": 9001482820},
                     headers={'Content-Type: application/json'})

print(resp)