import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Завантаження та парсинг XML
sitemap_url = 'https://itorrents-igruha.org/sitemap.xml'
response = requests.get(sitemap_url)
sitemap_content = response.content

# Парсинг XML для витягнення всіх URL
root = ET.fromstring(sitemap_content)
namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

urls = [elem.text for elem in root.findall('.//ns:loc', namespaces)]







# Функція для витягнення дати та часу з HTML-сторінки
def get_date_time_from_page(url):
    page_response = requests.get(url)
    soup = BeautifulSoup(page_response.text, 'html.parser')
    
    # Пошук потрібного елемента з інформацією про оновлення
    article_info = soup.find('div', {'id': 'article-film-full-info'})
    if article_info:
        time_element = article_info.find('time', {'class': 'published'})
        if time_element:
            return time_element.get('datetime')
    return None



# Структура для збереження даних
data = {
    "name": "Torrents-Igruha",
    "downloads": []
}



urls = urls[:57]

# Пройдемо по кожному URL та дістанемо дані
for index, url in enumerate(urls, start=1):
    date_time = get_date_time_from_page(url)
    if date_time:

        print(f'{index}. {url}: {date_time}')

        # Приклад: тут замість реальних файлів і назв можна витягнути реальні назви і дані
        # download_info = {
        #     "title": url.split('/')[-1].replace('.html', ''),  # Назва файлу, припустимо, остання частина URL
        #     "uris": [url],
        #     "uploadDate": date_time,
        #     "fileSize": "N/A"  # Тут можна додати функцію для витягнення розміру файлу
        # }
        download_info = {
            "title": "shapez 2",  # Назва файлу, припустимо, остання частина URL
            "uris": [url],
            "uploadDate": "2019-03-21T20:02:00Z",
            "fileSize": "178.7 MB"  # Тут можна додати функцію для витягнення розміру файлу
        }
        data["downloads"].append(download_info)
    else:
        print(f'{index}. {url}: Date could not be found')


current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f'downloads_{current_time}.json'

# Збереження у JSON файл
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print(f"The data is saved in file {filename}")





