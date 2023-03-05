import os
from bs4 import BeautifulSoup
from googletrans import Translator

input_folder = 'C:\\Users\\amiag\\Desktop\\aaa\\1\\www.classcentral.com\\university'
output_folder = 'C:\\Users\\amiag\\Desktop\\aaa\\1\\www.classcentral.com2'

translator = Translator()
i = 0
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.html'):
            print(file)
            input_file = os.path.join(root, file)
            output_file = os.path.join(output_folder, file)
            with open(input_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            text_elements = soup.find_all(True)
            for element in text_elements:
                if element.name == 'img' and element.has_attr('data-src'):
                    element['src'] = element['data-src']
                if element.string is not None and element.name not in ['style', 'script', 'meta']:
                    # translation = translator.translate(element.string, src='auto', dest='hi').text
                    translation = translator.translate(element.string, src='auto', dest='hi').text

                    element.string = translation
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print('loop1')
    print('loop2')
print('loop3')
            
