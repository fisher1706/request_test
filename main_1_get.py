# https://www.youtube.com/watch?v=5_J2iQBArbQ&list=PLF4MWzDJPFSZbFLkfLnmy3zKQeyckCdKI&index=1


import requests

"""
GET
"""

url_google = 'http://google.com'
url_website = 'https://jsonplaceholder.typicode.com/posts/1'

url = 'http://127.0.0.1:5000/external-api/test-full2/test-full2/'

resp_1 = requests.get(url=url,
                      params={'q': 'cats'}
                      )

resp_3 = requests.get(url=url)

if __name__ == '__main__':
    print(f"resp_1: {resp_1.url}")
    print(f"resp_1: {resp_1.status_code}")
    print(f"resp_1: {resp_1.json}")


    # print(f'resp_1_code: {resp.status_code}')
    # print(f'resp_1_url: {resp.url}')

    # print(f'resp_1_text: {resp.text}')
    # print(f'resp_1_content: {resp.content}')
    # print(f'resp_1_content_decode: {resp.content.decode(resp.encoding)}')

    # print(f'resp_1_headers: {resp.headers}')
    # print(f'resp_1_headers_content: {resp.headers["Content-Type"]}')
    #
    # print(f'resp_2_json: {resp_2.json()}')

    # print(resp_3)








