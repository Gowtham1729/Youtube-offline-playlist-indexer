import requests
from bs4 import BeautifulSoup
url = raw_input("Please Enter Youtube url : ")

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()
x = 0
a = open(('order.txt'), 'w')
b = open(('order links'+'.txt'), 'w')
title = soup.find('a', {'class' : "yt-simple-endpoint style-scope yt-formatted-string"})
for i in soup.find_all('a', attrs = {'class' : "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link "}):
   x = x+1
   a.write(str(str(x) + str(i.string)))
   b.write('https://www.youtube.com'+i.get('href')+ '\n')

a.close()
b.close()


import os
names = open("order.txt")
l = []
for i in names:
    l.append(str(i))
for i in range(0, len(l)):
    l[i] = l[i][:-1]
l = l[:-1]

for i in range(1, len(l)):
    if i%2 == 0:
        l[i] = l[i][4:]
    else:
        l[i] = l[i][6:]

for i in range(0, len(l)):
    if i%2 == 0:
        l[i] = int(l[i])


for i in range(0, len(l)):
    x = ""
    if i%2 == 1:
        for j in range(0,len(l[i])):
            if l[i][j] == '|':
                x = x+'_'
            else:
                x = x+l[i][j] 
        l[i] = x+".mp4"

new_names = []

for i in range(0, len(l)):
    if i%2 == 0:
       new_names.append(str(l[i]) + '.' + l[i+1])

old_names = []
for i in range(0, len(l)):
    if i%2 == 1:
       old_names.append(str(l[i]))

for i in range(0,len(new_names)):
    print i
    print(old_names[i])
    try:
        os.rename(old_names[i], new_names[i])
    except:
        None
