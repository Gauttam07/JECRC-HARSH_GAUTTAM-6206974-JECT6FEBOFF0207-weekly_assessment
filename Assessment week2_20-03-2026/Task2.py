from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://automationexercise.com/signup")

sleep(2)

driver.find_element(By.NAME, "name").send_keys("Geeeats")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("geetsa123@gmail.com")

driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

sleep(2)

driver.find_element(By.ID, "id_gender1").click()

newsletter = driver.find_element(By.ID, "newsletter")
offers = driver.find_element(By.ID, "optin")

newsletter.click()
offers.click()

print("Newsletter selected:", newsletter.get_attribute("checked"))
print("Offers selected:", offers.get_attribute("checked"))