import requests
import os
from bs4 import BeautifulSoup


response = requests.get('https://ekantipur.com/pradesh-1').text
soup = BeautifulSoup(response,'lxml')
dates = soup.find_all('div',class_="date cat_date")

articles = soup.find_all('article',class_="normal")

for x in dates:
    y = x.find('span')
    os.makedirs(y.text,exist_ok= True)
jes7 = []
jes8 = []

for link in articles:
    links = link.find('a')
    a=links['href']
    title = link.find('h2')
    
    
    if('2021/05/21' in a):
        
        jes7.append(a)
        jes7.append(title.text)
        
    elif('2021/05/22' in a):
        jes8.append(a)
        jes8.append(title.text)
        
    
# for jestha 7   
with open(os.path.join('जेष्ठ ७, २०७८', 'link.txt'), 'w') as f:
    for i in range(0,len(jes7)-1,2):
        f.write('https://ekantipur.com'+jes7[i]+'\n')
    f.close()
with open(os.path.join('जेष्ठ ७, २०७८', 'title.txt'), 'w',encoding='utf-8') as f:
    for i in range(1,len(jes7),2):
        f.write(jes7[i]+'\n')
    f.close()
file = open(os.path.join('जेष्ठ ७, २०७८', 'news.txt'), 'w',encoding='utf-8')
for i in range(0,len(jes7)-1,2):
    res = requests.get('https://ekantipur.com'+jes7[i]).text
    s = BeautifulSoup(res,'lxml')
    
    news_content = s.find_all('div',class_='description')
    print(news_content)
    
    for news in news_content:
        final_news = news.find_all('p')
        
        for i in final_news:
            file.write(i.text)
            file.write('\n')
        date = news.find('span',class_='published-at')
        file.write(date.text)
    file.write('\n****************************************\n')
file.close()

# for jestha 8   
file = open(os.path.join('जेष्ठ ८, २०७८', 'news.txt'), 'w',encoding='utf-8')
for i in range(0,len(jes8)-1,2):
    res = requests.get('https://ekantipur.com'+jes8[i]).text
    s = BeautifulSoup(res,'lxml')
    
    news_content = s.find_all('div',class_='description')
    print(news_content)
    
    for news in news_content:
        final_news = news.find_all('p')
        
        for i in final_news:
            file.write(i.text)
            file.write('\n')
        date = news.find('span',class_='published-at')
        file.write(date.text)
    file.write('\n****************************************\n')
file.close()

     
with open(os.path.join('जेष्ठ ८, २०७८', 'link.txt'), 'w') as f:
    for i in range(0,len(jes8)-1,2):
        f.write('https://ekantipur.com'+jes8[i]+'\n')
    f.close()
with open(os.path.join('जेष्ठ ८, २०७८', 'title.txt'), 'w',encoding='utf-8') as f:
    for i in range(1,len(jes8),2):
        f.write(jes8[i]+'\n')
    f.close() 



