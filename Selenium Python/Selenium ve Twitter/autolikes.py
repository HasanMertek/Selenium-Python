from selenium import webdriver
import time
import loginInfo
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



browser = webdriver.Firefox()
browser.get("https://x.com")
time.sleep(3)


giris_yap = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span")
giris_yap.click()


time.sleep(3)

username=browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
username.send_keys(loginInfo.username)
username_ileri=browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div")
username_ileri.click()
time.sleep(3)
password=browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password.send_keys(loginInfo.password)
login = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span")

login.click()


time.sleep(5)
ara = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")
ara.send_keys("#yazilimayolver")
ara.send_keys(Keys.ENTER)
time.sleep(5)

lenOfPage=browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight")
match=False
while(match==False):
    lastCount=lenOfPage
    time.sleep(3)
    lenOfPage=browser.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight")
    if lastCount==lenOfPage:
        match=True
time.sleep(5)

elements = browser.find_elements(By.CSS_SELECTOR, "button[data-testid='like']")
for element in elements:                             
    element.click()
    time.sleep(2)

  
time.sleep(10)   
browser.close()