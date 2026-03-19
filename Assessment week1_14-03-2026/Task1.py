from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)
driver.get("https://the-internet.herokuapp.com/login")
sleep(1)

username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
print("Username field located")


password = driver.find_element(By.CSS_SELECTOR, "input#password")
print("Password field located")


login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print("Login button located")


footer_link = driver.find_element(By.CSS_SELECTOR, 'div[style="text-align: center;"] a')
print("Footer link located:", footer_link.text)

driver.quit()