import os
from bs4 import BeautifulSoup
from googletrans import Translator

input_folder = 'C:\\Users\\amiag\\Desktop\\aaa\\1\\www.classcentral.com\\report'
output_folder = 'C:\\Users\\amiag\\Desktop\\aaa\\1\\www.classcentral.com2\\report'
i = 1
translator = Translator()
for root, dirs, files in os.walk(input_folder):
    print(root)
    print(dirs)
    print(files)
    print('-------------------')
    if i < 20:
        i = i + 1
        continue
    for file in files:
        if file.endswith('.html'):
            input_file = os.path.join(root, file)
            output_dir = os.path.join(output_folder, os.path.relpath(root, input_folder))
            print(output_dir)
            print(input_file)
            output_file = os.path.join(output_dir, file)
            print(output_file)
            os.makedirs(output_dir, exist_ok=True)
            with open(input_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            text_elements = soup.find_all(True)
            for element in text_elements:
                if element.name == 'img' and element.has_attr('data-src'):
                    element['src'] = element['data-src']
                if element.string is not None and element.name not in ['style', 'script', 'meta']:
                    translation = translator.translate(element.string, src='auto', dest='hi').text
                    element.string = translation
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Translated {input_file} to {output_file}")
