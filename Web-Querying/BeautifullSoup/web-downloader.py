from bs4 import BeautifulSoup
import requests
import os
import re

url = "https://prompt.ml"
folder = "Website"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, features='lxml')
soupA = soup.prettify()


def Downloader(url, folder):
    os.mkdir(os.path.join(os.getcwd(), folder))
    os.chdir(os.path.join(os.getcwd(), folder))

    for result in soup.find_all('link'):
        lol = result['href']
        if (lol != '/images/favicon.ico'):
            all_link = lol
            name1 = os.path.basename(lol)
            name1 = name1.replace("/", "*")
            try:
                with open(name1, 'wb') as f:
                    Lmao = requests.get(lol)
                    f.write(Lmao.content)
            except:
                continue

    for image in soup.find_all('img'):
        image_url = image['src']
        all_link += '/n' + image_url
        name = os.path.basename(image_url)
        name = name.replace("/", "*")
        with open(name, 'wb') as f:
            im = requests.get(image_url)
            f.write(im.content)

    hope = all_link.split('\n')
    print(hope)
    for link in hope:
        file_name = link.split('/')[-1]
        path = os.path.abspath(file_name)
        pp = path.split('\n')
        for s in pp:
            soup1 = soupA.replace(link, f'file://{s}')

    soup1 = bytes(soup1, 'utf-8')

    with open(folder + '.html', 'wb') as file:
        file.write(soup1)
    return soup1

Downloader(url=url, folder=folder)
