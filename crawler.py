#import libs
import urllib3
from bs4 import  BeautifulSoup

#Specify the URL:
# quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
# quote_page = 'https://www.baidu.com'
quote_page = 'http://www.szse.cn/market/index.html'
#query the url and return html to the variable'page'
http = urllib3.PoolManager()
r = http.request('GET', quote_page)
# print(r.status)
page = r.data
# print(page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page,'html.parser')

# # Take out the <div> of name and get its value
phone_number = soup.find('span', attrs={'class':'footer-ipone'})


# name = name_box.text.strip()

print(phone_number)

# # get the index price
email = soup.find('span', attrs={'class':'footer-email'})
# price = price_box.text
print(email)