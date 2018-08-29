import requests

#get Github's public timeline
r = requests.get('https://api.github.com/events')
print(r.content)

#how to make an HTTP POST request:
# r = requests.post('http://httpbin.org/post',data= { 'key':'value'})
#other request types
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')


#parsing parameters in URLs
payload = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get',params=payload)
print(r.url)

#pass a list of items as a value
payload = {'key1':'value1','key2':['value2','value3']}
r = requests.get('http://httpbin.org/get',params=payload)

#Response Content
r = requests.get('https://api.github.com/events')
# print(r.content)
print(r.text)
print(r.encoding)
r.encoding = 'ISO-8859-1'

#you can also create an image from binary data returned by a request
from PIL import Image
from io import BytesIO
# i = Image.open(BytesIO(r.content))

#Json response content
print(r.json)

r = requests.get('https://api.github.com/events',stream=True)
print(r.raw)
filename = "./response_raw"
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

#Custom headers
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url,headers=headers)
#More complicated Post requests

payload = { 'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data=payload)
print(r.text)

payload_tuples = [('key1','value1'),('key2','value2')]
r1 = requests.post('http://httpbin.org/post',data=payload_tuples)
payload_dict = {'key1':['value1','value2']}
r2 = requests.post('http://httpbin.org/post',data=payload_dict)
print(r1.text)
print(r2.text)
print(r1.text == r2.text)

#use json file as the post data
import json

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))

#Response status code
r = requests.get('http://httpbin.org/get')
print(r.status_code)
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)

#Response headers,headers names are case-insensitive
print(r.headers)
#Cookies
# >>> url = 'http://example.com/some/cookie/setting/url'
# >>> r = requests.get(url)

# >>> r.cookies['example_cookie_name']
# 'example_cookie_value'
# >>> url = 'http://httpbin.org/cookies'
# >>> cookies = dict(cookies_are='working')

# >>> r = requests.get(url, cookies=cookies)
# >>> r.text
# '{"cookies": {"cookies_are": "working"}}'
# >>> jar = requests.cookies.RequestsCookieJar()
# >>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# >>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# >>> url = 'http://httpbin.org/cookies'
# >>> r = requests.get(url, cookies=jar)
# >>> r.text
# '{"cookies": {"tasty_cookie": "yum"}}'






