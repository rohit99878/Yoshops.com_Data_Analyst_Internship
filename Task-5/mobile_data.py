import pandas as pd
import requests
from bs4 import BeautifulSoup

Title = []
Processors = []
Ram = []
Battery = []
Discounted_Price =[]
Review = []

for i in range(14,33):
    url = "https://www.flipkart.com/search?q=Mobile+under+12000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=price_desc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_ ='_1YokD2 _3Mn1Gg')

    names = box.find_all('div', class_='_4rR01T')
    for i in names:
        name = i.text
        if name and len(Title) < 170:
            Title.append(name)

    price = box.find_all('div', class_='_30jeq3 _1_WHN1')
    for i in price:
        name = i.text
        if name and len(Discounted_Price) < 170:
            Discounted_Price.append(name)


    processors = box.find_all('li', class_='rgWa7D')
    for i in processors:
        processor_info = i.text
        # Check if the extracted information contains the keyword "Processor"
        if "Processor" in processor_info:
            if processor_info and len(Processors) <170:
                Processors.append(processor_info)

    ram = box.find_all('li', class_='rgWa7D')
    for i in ram:
        ram_info = i.text

        # Check if the extracted information contains the keyword "RAM"
        if "RAM" in ram_info:
            if ram_info and len(Ram) < 170:
                Ram.append(ram_info)

    battery = box.find_all('li', class_='rgWa7D')
    for i in battery:
        battery_info = i.text

        # Check if the extracted information contains the keyword "RAM"
        if "Battery" in battery_info:
            if battery_info and len(Battery) < 170:
                Battery.append(battery_info)


    review = box.find_all("div",class_ = '_3LWZlK')
    for i in review:
        name = i.text
        if name and len(Review) < 170:
                Review.append(name)

df = pd.DataFrame({"Title" : Title, "Processors" : Processors, "Ram" : Ram, "Battery" : Battery, "Price" : Discounted_Price, "Review" : Review})

df.to_csv("C:/Users/Rohit/Desktop/Yoshop_Internship/Tasks/Task-5/Mobile.csv")
