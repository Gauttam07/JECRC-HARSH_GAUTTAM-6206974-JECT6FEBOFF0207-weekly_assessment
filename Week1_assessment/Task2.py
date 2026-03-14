from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1. Start browser
driver = webdriver.Chrome()

# 2. Navigate to wikipedia
driver.get("https://www.wikipedia.org/")
sleep(2)

# 3. Find the search input field
search_box = driver.find_element(By.ID, "searchInput")
print("Search box found")

# 4. Find the "English" language
english_lang = driver.find_element(By.ID, "js-link-box-en")
print("English language found:", english_lang.text)

# 5. Find the main Wikipedia logo image
logo = driver.find_element(By.CSS_SELECTOR, "div.central-textlogo img")
print("Wikipedia logo located")

# 6. Count language links in central block
languages = driver.find_elements(By.CSS_SELECTOR, "div.central-featured-lang a")
print("Number of language links:", len(languages))

english_lang.click()
sleep(2)

# 7. Navigate back
driver.back()
sleep(2)

# 8. Navigate forward
driver.forward()
sleep(2)

# 9. Refresh page
driver.refresh()
sleep(2)

# 10. Print final page title
print("Final Page Title:", driver.title)

# 11. Quit browser
driver.quit()