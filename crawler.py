#import libs
'''
 This project is a demo script of using urllib3 and beautifulsoup4 to crawl website.
 We will use www.szse.cn as a data source.
 We will crawl every page on this website 
'''
import urllib3
from bs4 import  BeautifulSoup

#Specify the URL:
quote_page = 'http://www.szse.cn/market/index.html'
#query the url and return html to the variable'page'
http = urllib3.PoolManager()
r = http.request('GET', quote_page)
# print(r.status)
page = r.data
# print(page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page,'html.parser')

# Take out the <span> of name and get its value
phone_number = soup.find('span', attrs={'class':'footer-ipone'})


# name = name_box.text.strip()

print(phone_number)

email = soup.find('span', attrs={'class':'footer-email'})

print(email)