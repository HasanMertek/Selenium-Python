from selenium import webdriver
import time
import loginInfo
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



browser = webdriver.Firefox()
browser.get("https://www.instagram.com")
time.sleep(3)

username=browser.find_element(By.NAME,"username")
username.send_keys(loginInfo.username)
time.sleep(2)
password=browser.find_element(By.NAME,"password")
password.send_keys(loginInfo.password)
login = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]")
login.click()
time.sleep(9)
bilgi=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
bilgi.click()
time.sleep(2)
bildirim=browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
bildirim.click()
time.sleep(7)


hesap = browser.find_element(By.XPATH, "//div[@class='x1iyjqo2 xh8yej3']//span[text()='Ara']")
hesap.click()
time.sleep(5)


ara = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
ara.send_keys("yb_ankara")
time.sleep(5)
blog = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/a[1]/div[1]/div/div")
blog.click()
time.sleep(5)

takip = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[3]/a")
takip.click()
time.sleep(5)

jscommand="""
followers = document.querySelector("._aano");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage = followers.scrollHeight;
return lenOfPage;

"""


lenOfPage=browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount=lenOfPage
    time.sleep(2)
    lenOfPage=browser.execute_script(jscommand)
    if lastCount==lenOfPage:
        match=True
time.sleep(5)

liste=[]
followers=browser.find_elements(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade")
for follower in followers:
    liste.append(follower.text)

    

with open("followers.txt","w",encoding="UTF-8") as file:
    for follower in liste:
       file.write(follower + "\n")
elements=browser.find_elements(By.CSS_SELECTOR,".css-146c3p1.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim")

tweets=[]
for element in elements:
    tweets.append(element.text)



    
tweetCount=1
with open("tweets.txt","w",encoding="UTF-8") as file :

    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet +"\n")
        file.write("*******************\n")
        tweetCount+=1

browser.close()

