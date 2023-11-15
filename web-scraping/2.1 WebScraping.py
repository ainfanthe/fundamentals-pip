import bs4
import requests
result = requests.get('http://books.toscrape.com/')
s = bs4.BeautifulSoup(result.text, 'lxml')

# img = s.select('img')
# for i in img:
#     print('{}'.format(i))

img = s.select('.thumbnail')
for i in img:
    print('http://books.toscrape.com/{}'.format(i['src']))
