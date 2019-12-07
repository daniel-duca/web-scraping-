
import requests
from bs4 import BeautifulSoup
import pandas

price=[]
vtype=[]
year=[]
hand=[]
engine_size=[]
date=[]
data=[]
title=[]
zone_of_sale=[]

def fix_name(strList,res):
    temp_res=""
    for i in strList:
        if (i[0]<='z' and i[0]>='a') or (i[0]<='Z' and i[0]>='A') or (i[0] <='9' and i[0]>='0'):
            pass
        else:
            i=i[::-1]
        temp_res=temp_res+i+' '
    res.append(temp_res)  
max_page=69
for page in range(1,max_page):
    
    r = requests.get("https://www.yad2.co.il/vehicles/motorcycles?page="+str(page), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"feeditem table"})

    for item in all:
        temp_price=item.find("div",{"class":"price"}).text.replace(" ","").replace("\n","")
        if temp_price=='לאצויןמחיר':
            temp_price="None"
        price.append(temp_price)
        name=item.find("span",{"class":"title"}).text.replace("\n","").split()
        fix_name(name,title)
        vtype.append(item.find("span",{"class":"subtitle"}).text.replace(" ","").replace("\n","")[::-1])
        date.append(item.find("div",{"class":"showDateInLobby"}).text.replace(" ","").replace("\n",""))
        data=item.find_all("span",{"class":"val"})
        year.append(data[0].text.replace(" ","").replace("\n",""))
        hand.append(data[1].text.replace(" ","").replace("\n",""))
        engine_size.append(data[2].text.replace(" ","").replace("\n",""))

df=pandas.DataFrame({"Title":title,"Type":vtype,"Year":year,"Engine Size":engine_size,"Hand":hand,"Date Added":date,"Price":price})
df.to_csv("Yad2.csv")




    





        

    
    






