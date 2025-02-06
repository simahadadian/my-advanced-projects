import requests
import re

r=requests.get('https://www.scrapethissite.com/pages/simple/')

from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')

import mysql.connector 
cnx = mysql.connector.connect(
user='root', password='1234', host='127.0.0.1', database='test'
)
cursor = cnx.cursor()


name=soup.find_all('h3', attrs={'class':["country-name"]})
capital=soup.find_all('span', attrs={'class':["country-capital"]})
population=soup.find_all('span', attrs={'class':["country-population"]})
Area=soup.find_all('span', attrs={'class':["country-area"]})


for i in range (20):
 n=re.sub(r'\s+',' ', name[i].text).strip()
 c=re.sub(r'\'+',' ', capital[i].text).strip()
 p=re.sub(r'\s+',' ', population[i].text).strip()
 A=re.sub(r'\s+',' ', Area[i].text).strip()
 cursor.execute('INSERT INTO countries VALUES(\'%s\',\'%s\',\'%s\',\'%s\')'%(n,c,p,A))
 cnx.commit()

# پروژه web scraping