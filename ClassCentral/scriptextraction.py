import requests
from bs4 import BeautifulSoup
import urllib


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}


url = 'https://www.classcentral.com/'
webpack_folder = 'C:\\Users\\amiag\\Desktop\\CC\\ClassCentral\\1\\www.classcentral.com\\webpack' # replace with your webpack named folder

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all script tags
scripts = soup.find_all('script')
print(scripts)
# Filter script tags by webpack named folder
filtered_scripts = [s for s in scripts if webpack_folder in s.get('src', '')]

# Download JavaScript files
for s in filtered_scripts:
    js_url = urllib.parse.urljoin(url, s['src'])
    js_filename = js_url.split('/')[-1]
    urllib.request.urlretrieve(js_url, js_filename)
