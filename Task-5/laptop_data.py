import pandas as pd
import requests
from bs4 import BeautifulSoup

Title = []
Price =[]
Processors = []
Ram = []
Operating_System = []
Display = []
Review = []

for i in range(14,19):
    url = "https://www.flipkart.com/search?q=%22laptops+under+25000%22&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=price_desc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D40000&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_ ='_1YokD2 _3Mn1Gg')

    names = box.find_all('div', class_='_4rR01T')
    for i in names:
        name = i.text
        if name and len(Title) < 70:
            Title.append(name)


    price = box.find_all('div', class_='_30jeq3 _1_WHN1')
    for i in price:
        name = i.text
        if name and len(Price) < 70:
            Price.append(name)


    processors = box.find_all('li', class_='rgWa7D')
    for i in processors:
        processor_info = i.text
    # Check if the extracted information contains the keyword "Processor"
        if "Processor" in processor_info:
            if processor_info and len(Processors) <70:
                Processors.append(processor_info)
    


    ram = box.find_all('li', class_='rgWa7D')
    for i in ram:
        ram_info = i.text
        
        # Check if the extracted information contains the keyword "RAM"
        if "RAM" in ram_info:
            if ram_info and len(Ram) < 70:
                Ram.append(ram_info)


    operating_system = box.find_all('li', class_='rgWa7D')
    for i in operating_system:
        os_info = i.text
        if "Operating System" in os_info:
            os_text = os_info.replace('Operating System', '').strip()
            if os_text and len(Operating_System) < 70:
                Operating_System.append(os_text)
            # Append to the list only if the extracted text is not empty and the list length is less than 24



    display = box.find_all('li', class_='rgWa7D')
    for i in display:
        display_info = i.text
        
        # Check if the extracted information contains the keyword "Display"
        if "Display" in display_info:
            if display_info and len(Display) < 70:
                Display.append(display_info)


    review = box.find_all("div",class_ = '_3LWZlK')
    for i in review:
        name = i.text
        if name and len(Review) < 70:
                Review.append(name)

print("Length of Title:", len(Title))
print("Length of Price:", len(Price))
print("Length of Processors:", len(Processors))
print("Length of Ram:", len(Ram))
print("Length of Operating_System:", len(Operating_System))
print("Length of Display:", len(Display))
print("Length of Review:", len(Review))


df = pd.DataFrame({"Title" : Title, "Processors" : Processors, "Ram" : Ram, "Operating System" : Operating_System, "Display" : Display, "Price" : Price, "Review" : Review})

df.to_csv("C:/Users/Rohit/Desktop/Yoshop_Internship/Tasks/Task-5/Laptop.csv")



# np = soup.find("a",class_='_1LKTO3').get('href')
# cnp = "https://www.flipkart.com"+np
# print(cnp)
