import ssl
import csv
import requests
from bs4 import BeautifulSoup
from urllib3 import poolmanager


class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)


url = input('Укажите ссылку на текст песни: ')

session = requests.session()
session.mount('https://', TLSAdapter())
res = session.get(url)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(res.text)

with open('index.html', encoding='utf8') as file:
    src = file.read()
    
src = src\
    .replace('<br />', '')\
    .replace('original">  ', 'original">')\
    .replace('translate">  ', 'translate">')

soup = BeautifulSoup(src, 'lxml')

track_name = soup.find('div', class_='texts col').find(class_='original').next_element.text
track_artist = soup.find('div', id='location_texts').previous_element.previous_element.previous_element.previous_element.previous_element.text

original_text = soup.find('div', class_='texts col').find(id='click_area').find_all(class_='original')
translate_text = soup.find('div', class_='texts col').find(id='click_area').find_all(class_='translate')

with open(f'data/{track_artist} - {track_name}.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    
    for i in range(len(original_text)):
        if translate_text[i].text == '':
            writer.writerow(original_text[i])
        else:
            writer.writerow(original_text[i])
            writer.writerow(translate_text[i])
