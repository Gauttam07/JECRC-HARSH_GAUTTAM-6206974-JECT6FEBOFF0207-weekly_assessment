from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

print("Title:", driver.title)
print("URL:", driver.current_url)

wait = WebDriverWait(driver, 10)

drop = wait.until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))
select = Select(drop)
select.select_by_visible_text("Books")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Harry Potter")
search_box.send_keys(Keys.RETURN)

wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")))

item = driver.find_elements(By.XPATH, "//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']/span")

print("\nFirst Five Product Names:")
for i in range(5):
    print(f"{i+1}.",item[i].text)

item[0].click()

sleep(5)
driver.quit()