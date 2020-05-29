import pandas as pd
from urllib.request import urlopen as Req 
from bs4 import BeautifulSoup as Soup 


my_url = 'https://batdongsan.com.vn/nha-dat-can-thue'

#graping the page
Uclient = Req(my_url)
page_html = Uclient.read()
Uclient.close()

#checking file and translate (parser)
page_soup = Soup(page_html, "html.parser")

#selecting
containers = page_soup.findAll("div", {"class":"branch"})

text
text1
final = []
final1 =[]
final3 = []
for i in range(len(containers)):
    store = containers[i].findAll("div", {"class": "branch-name"})
    text = store[0].text
    print("Title : "+text)
    store1 = containers[i].findAll("div", {"class": "branch-add"})
    text1 = store1[0].text
    print("Info : "+text1)
    final.append(text)
    final1.append(text1)

for i in final:
    print(i)


for f1, f2 in zip(final,final1):
    final3.append({"Title":f1,"Information":f2})
       
df = pd.DataFrame(final3)
df.to_csv('pandas2.csv')
