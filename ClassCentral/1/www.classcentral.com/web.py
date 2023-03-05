import requests
from bs4 import BeautifulSoup
from googletrans import Translator

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = 'https://www.classcentral.com/'

response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')

text_elements = soup.find_all(True)

translator = Translator()
print(len(text_elements))
for element in text_elements:
    if element.name == 'img':
        try:
            print(element['data-src'])
            print(element['src'])
        except:
            print('error')
    if element.name == 'img' and element.has_attr('data-src'):
        element['src'] = element['data-src']

    if element.string is not None and element.name not in ['style', 'script', 'meta']:
        print(element.string)
        translation = translator.translate(element.string, src='auto', dest='hi').text
        element.string = translation
        # print(translation)

with open('text2.txt', 'w', encoding='utf-8') as f:
    f.write(str(text_elements))

print('DONE')
