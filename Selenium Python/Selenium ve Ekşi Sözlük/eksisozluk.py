from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()
url="https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pageCount=1
entries=[]
entryCount=1
while pageCount<=10:
    randomPage=random.randint(1,1290)
    newUrl=url+str(randomPage)
    browser.get(newUrl)
    time.sleep(3)

    elements=browser.find_elements(By.CSS_SELECTOR,".content")
    for element in elements:
        entries.append(element.text)
    
    pageCount+=1


with open("entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+ "\n"+ entry +"\n")
        file.write("***********************\n")
        entryCount+=1

browser.close()


