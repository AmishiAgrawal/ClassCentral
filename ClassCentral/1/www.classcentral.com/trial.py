import requests
from bs4 import BeautifulSoup
# from google.cloud import translate_v2 as translate

# Initialize the translation client
# translate_client = translate.Client()

# Define the webpage URL and language codes
url = 'https://www.classcentral.com/'
source_lang = 'en'
target_lang = 'fr'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
# Fetch the webpage content using requests and parse it with Beautiful Soup
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the HTML elements that contain text
# text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span'])

# # Loop through each text element and translate its contents
# for element in text_elements:
#     # Get the text content of the element
#     text = element.text.strip()
    
#     # Translate the text using the Google Translate API
#     translation = translate_client.translate(text, source_language=source_lang, target_language=target_lang)
    
#     # Replace the original text with the translated text
#     element.string = translation['translatedText']

# # Print the updated HTML content
# print(soup.prettify())

# from googletrans import Translator
from translate import Translator

translator = Translator(to_lang="hi")
translation = translator.translate("who")

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(translation)
