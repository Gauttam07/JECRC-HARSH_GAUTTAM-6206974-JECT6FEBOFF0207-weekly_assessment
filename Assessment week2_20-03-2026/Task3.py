from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 10)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)

searching = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@class='gLFyf']")))
searching.send_keys("Selenium Python")

sugg = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))

for i in sugg:
    print(i.text)

sugg[0].click()
sleep(20)
driver.quit()