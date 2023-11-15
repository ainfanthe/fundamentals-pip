import bs4
import requests
urlBase = 'http://books.toscrape.com/catalogue/page-{}.html'
# for i in range(1,11):
#     print(urlBase.format(i))

result = requests.get(urlBase.format('1'))
s = bs4.BeautifulSoup(result.text, 'lxml')
lib = s.select('.product_pod')
# print(lib[0].select('.star-rating.Four'))
print(lib[0].select('a')[1]['title'])