from os import write
import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets').text
soup = BeautifulSoup(response,'lxml')
tablets = soup.find_all('div',class_ = "col-sm-4 col-lg-4 col-md-4")
file = open('final.csv','w',newline='')
writer = csv.writer(file)
writer.writerow(['Tablet Name','Description','Price'])
for tab in tablets:
    tablet_name = tab.find('a',class_='title')
    tablet_price = tab.find('h4',class_="pull-right price")
    tab_desc = tab.find('p',class_ = 'description')
    print(tablet_name.text,tablet_price.text,tab_desc.text)
    writer.writerow([(tablet_name.text),(tab_desc.text),(tablet_price.text)])
file.close()
