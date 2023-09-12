import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_Name = []
Final_Price =[]
Mrp = []
Discount = []
Ram = []
Display = []
Camera = []
Battery = []
Warranty = []
Size = []
Review = []

for i in range(1,25):
    url = "https://www.flipkart.com/search?q=mobiles+under+10000+rupees&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_14_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_14_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobiles+under+10000+rupees%7CMobiles&requestId=892eca98-6503-40b9-ab02-630b420ee6d6&as-backfill=on&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_ ='_1YokD2 _3Mn1Gg')

    pro_name = box.find_all('div', class_='_4rR01T')
    for i in pro_name:
        name = i.text
        if name and len(Product_Name) < 300:
            Product_Name.append(name)
    
    price = box.find_all('div', class_='_30jeq3 _1_WHN1')
    for i in price:
        name = i.text
        if name and len(Final_Price) < 300:
            Final_Price.append(name)
    
    mrp = box.find_all('div',class_ = '_3I9_wc _27UcVY')
    for i in mrp:
        name = i.text
        if name and len(Mrp) < 300:
            Mrp.append(name)
    
    discount = box.find_all('div',class_ = '_3Ay6Sb')
    for i in discount:
        name = i.text
        if name and len(Discount) < 300:
            Discount.append(name)

    ram = box.find_all('li', class_='rgWa7D')
    for i in ram:
        ram_info = i.text
        if "RAM" in ram_info:
            if ram_info and len(Ram) < 300:
                Ram.append(ram_info)
    
    display = box.find_all('li', class_='rgWa7D')
    for i in display:
        name = i.text
        if "Display" in name:
            if name and len(Display) < 300:
                Display.append(name)
    
    camera = box.find_all('li', class_='rgWa7D')
    for i in camera:
        name = i.text
        if "Camera" in name:
            if name and len(Camera) < 300:
                Camera.append(name)

    battery = box.find_all('li', class_='rgWa7D')
    for i in battery:
        name = i.text

        if "Battery" in name:
            if name and len(Battery) < 300:
                Battery.append(name)
    
    warranty = box.find_all('li', class_='rgWa7D')
    for i in warranty:
        name = i.text

        # Check if the extracted information contains the keyword "RAM"
        if "Warranty" in name:
            if name and len(Warranty) < 300:
                Warranty.append(name)

    review = box.find_all("div",class_ = '_3LWZlK')
    for i in review:
        name = i.text
        if name and len(Review) < 300:
                Review.append(name)
    



print(len(Product_Name))
print(len(Final_Price))
print(len(Mrp))
print(len(Discount))
print(len(Ram))
print(len(Display))
print(len(Camera))
print(len(Battery))
print(len(Warranty))
print(len(Review))

df = pd.DataFrame({"Product Name" : Product_Name, "Final Price" : Final_Price, "MRP" : Mrp, "Discount" : Discount, "Ram" : Ram, "Display" : Display
                   , "Camera" : Camera, "Battery" : Battery, "Warranty" : Warranty, "Review" : Review})

df.to_csv("C:/Users/Rohit/Desktop/Yoshop_Internship/Tasks/Task-7/Mobile.csv")