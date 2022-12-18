## https://www.youtube.com/watch?v=tTnquxuOUxc&list=PLF4MWzDJPFSZbFLkfLnmy3zKQeyckCdKI&index=2


import requests

"""
PUT
"""

website = 'https://jsonplaceholder.typicode.com/posts/1'

response_3 = requests.put(url=website,
                          data={
                                'userId': 12,
                                'title': 'my new post',
                                'body': 'body for my post zapel',
                                'photo': {'1.jpg', '2.jpg', '3.jpg'}
                                })


if __name__ == '__main__':
    print(response_3.url)
    print(response_3.text)
    print(response_3.status_code)
    print(f'reason: {response_3.reason}')
    print(response_3.url)
    print(response_3.json())