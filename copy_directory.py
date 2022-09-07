import requests
from bs4 import BeautifulSoup
import os

url = "http://34.79.2.235/back_up_05_07_2022/anisse9/test_algo2/binance/cocotier/env_botmax/share/python-wheels/"


u = 'root'
page = requests.get(url)
soup = BeautifulSoup(page.content,'lxml')
type = soup.find_all("tr")
parent_dir = './'+u
directory = ''
file = ''

for i in type :
    try :
        if (i.td.img['alt'] == '[TXT]' or i.td.img['alt'] == '[   ]'):
            file = i.find_all_next('td')[1].text
            destination = f'{parent_dir}/{file}'
            pagepage = requests.get(url+'/'+file)
            with open(destination,'w') as f:
                f.write(pagepage.text)
        elif (i.td.img['alt'] == '[DIR]'):
            directory = i.find_all_next('td')[1].text
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)

    except AttributeError:
        pass

