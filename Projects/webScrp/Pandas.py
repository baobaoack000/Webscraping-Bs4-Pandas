import Pandas as pd
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

text1 = []
text = []
for i in range(len(containers)):
    store = containers[i].findAll("div", {"class": "branch-name"})
    text = store[0].text
    print(text)
    store1 = containers[i].findAll("div", {"class": "branch-add"})
    text1 = store1[0].text
    print(text1)
    
df = pd.DataFrame(text, text2)
                             



