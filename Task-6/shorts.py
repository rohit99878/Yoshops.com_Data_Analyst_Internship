import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_Name = []
Final_Price =[]
Mrp = []
Discount = []
Offers = []
Size = []
Review = []

for i in range(1,10):
    url = "https://www.flipkart.com/search?q=shorts+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")

    pro_name = soup.find_all('a', class_='IRpwTa')
    for i in pro_name:
        name = i.text
        if name and len(Product_Name) < 200:
            Product_Name.append(name)

    price = soup.find_all('div',class_ = '_30jeq3')
    for i in price:
        name = i.text
        if name and len(Final_Price) < 200:
            Final_Price.append(name)

    mrp = soup.find_all('div',class_ = '_3I9_wc')
    for i in mrp:
        name = i.text
        if name and len(Mrp) < 200:
            Mrp.append(name)

    discount = soup.find_all('div',class_ = '_3Ay6Sb')
    for i in discount:
        name = i.text
        if name and len(Discount) < 200:
            Discount.append(name)


    offer = soup.find_all('div',class_ = '_2Tpdn3 _18hQoS')
    for i in offer:
        if len(offer) == 0:
            Offers.append("No offer")
        else:
            name = i.text
            if name and len(Offers) < 200:
                Offers.append(name)


    size = soup.find_all('span',class_ = '_376u-U')
    for i in size:
        name = i.text
        if name and len(Size) < 200:
            Size.append(name)


    review = soup.find_all('div', class_='_3LWZlK _3uSWvT')
    for i in review:
        name = i.text
        if name and len(Review) < 200:
            Review.append(name)

df = pd.DataFrame({"Product_Name" : Product_Name, " Final_Price" : Final_Price, "MRP" : Mrp, "Discount" : Discount, "Offers" : Offers, "Size": Size, "Ratings" : Review})

df.to_csv("C:/Users/Rohit/Desktop/Yoshop_Internship/Tasks/Task-6/shorts.csv")