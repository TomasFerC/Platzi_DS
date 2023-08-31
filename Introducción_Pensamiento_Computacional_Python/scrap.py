import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import namedtuple

Temas = namedtuple('Temas',['title_text','link_href'])
lista_temas = []

url = "https://platzi.com/cursos/estructuras-datos-python/"

r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'html.parser')

content_blocks = soup.find_all('ul', class_='ContentBlock-list')

for ul in content_blocks:
    list_items = ul.find_all('li', class_='ContentBlock-list-item')
    for item in list_items:
        title_element = item.find("span", class_="ContentClass-content-title")
        link_element = item.find("a")
        if title_element and link_element:
            title_text = title_element.get_text()
            link_href = "https://platzi.com"+link_element.get("href")
            lista_temas.append(Temas(title_text,link_href))

data = [{'title_text': tema.title_text, 'link_href': tema.link_href} for tema in lista_temas]
df = pd.DataFrame(data)
csv_file = '/home/tomas/worksource/Platzi_DS/Introducción_Pensamiento_Computacional_Python/temas.csv'
df.to_csv(csv_file, sep=';', index=False, encoding='utf-8-sig')

print("Archivo CSV guardado exitosamente.")
