# https://www.youtube.com/watch?v=tTnquxuOUxc&list=PLF4MWzDJPFSZbFLkfLnmy3zKQeyckCdKI&index=2


import requests

"""
POST
"""

website = 'https://jsonplaceholder.typicode.com/posts/'

response_1 = requests.post(url=website, data={
    'userId': 13,
    'title': 'my new post',
    'body': 'body for my post',
    'photo': {'1.jpg', '2.jpg', '3.jpg'}
})


response_2 = requests.post(url=website,
                           json={
    'userId': 13,
    'title': 'my new post',
    'body': 'body for my post'
})


if __name__ == '__main__':
    print(response_1.text)
    print(response_1.content)
    # print(response_1.status_code)
    # print(response_1.json())

    # print(response_2.status_code)
    # print(response_2.json())

