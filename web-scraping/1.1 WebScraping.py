import bs4
import requests

result = requests.get('http://quotes.toscrape.com/')
# print(result.text)
s = bs4.BeautifulSoup(result.text, 'lxml')
# print(s.select('p'))
print(s.select('title')[0].getText())
print(s.select('h2')[0].getText())

"""
Basic syntax:
" - s.select('div'): todos los elementos con la etiqueta 'div'
# - s.select('#estilo_4'): elementos con un id = 'estilo4'
. - s.select('.columna_der): elementos que contengan class = 'columna_der'
(espacio) - soup.select('div span'): cualquier elemento llamado 'span' dentro de un 'div'
> - s.select('div>span'): cualquier elemento llamado 'span' directamente dentro de un
elemento 'div' sin nada de por medio
"""

column = s.select('.col-md-4 span')
for i in column:
    print(i.getText())