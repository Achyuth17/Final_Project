from urllib.request import urlopen
import csv
import lxml
from bs4 import BeautifulSoup
l1=[]
l2=[]

sauce1=urlopen("https://karki23.github.io/Weather-Data/assignment.html").read()
srccode1=BeautifulSoup(sauce1,"lxml")
for i in srccode1.find_all('a'):
    l1.append(i.get('href'))

for i in l1:
    x="https://karki23.github.io/Weather-Data/"
    y=x+i

    sauce2=urlopen(y).read()
    srccode2=BeautifulSoup(sauce2,"lxml")
    table=srccode2.find_all('table')
    header=srccode2.find_all('th')
    data=[i.text for i in header]

    for row in table:
        rowdata=row.find_all('tr')
        for i in rowdata:
            table=i.find_all('td')
            r=[i.text for i in table]
            l2.append(r)

    with open("data.csv",'w') as writefile:
         writer=csv.writer(writefile)
         writer.writerow(data)
    with open("data.csv",'a') as writefile:
        for j in l2:
            writer=csv.writer(writefile)
            writer.writerow(j)
