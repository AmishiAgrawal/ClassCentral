import requests
from bs4 import BeautifulSoup
from translate import Translator

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = 'https://www.classcentral.com/'

response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')

text_elements = soup.find_all(True)
# text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span'])
# text_elements = soup.find_all('img')
translator = Translator(to_lang='hi')
print(len(text_elements))
for element in text_elements:
    if element.name == 'img' :
        try:
            print(element['data-src'])
            print(element['src'])
        except:
            print('error')
    if element.name == 'img' and element.has_attr('data-src'):
        element['src'] = element['data-src']
        # print('_-----------------------')
            
    # print(element['data-src'])
    if element.string is not None and element.name != 'style' and element.name != 'script' and element.name != 'meta':
        print(element.string)
        translation = translator.translate(element.string)
        # translation = translator.translate(element.string)
        element.string = translation
        print(text_elements.index)
        # print(element.string)

with open('final.html', 'w',encoding='utf-8') as f:
    f.write(str(soup))
