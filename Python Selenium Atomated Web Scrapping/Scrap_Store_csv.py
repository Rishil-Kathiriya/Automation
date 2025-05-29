from bs4 import BeautifulSoup
import os
import pandas as pd


d={'Product_Name':[],'Price':[],'Link':[]}
for file in os.listdir("data"):
    try:
        with open(f"data/{file}",'r',encoding='utf-8') as f:
            doc=f.read()
        soup=BeautifulSoup(doc,"html.parser")

        n=soup.find("h2")
        name=n.get_text(strip=True)

        l=soup.find("a")
        link="https://amazon.com/"+l['href']
        # link = f'=HYPERLINK("https://amazon.com{l["href"]}", "View Product)'

        p=soup.find("span",attrs={"class" : 'a-price-whole'})
        price=p.get_text(strip=True)
        
        d['Product_Name'].append(name)
        d['Price'].append(price)
        d['Link'].append(link)
    except Exception as e:
        print(e)

df=pd.DataFrame(d)
df.to_csv("data.csv",index=False)
print("Data Stored Successfully...")


