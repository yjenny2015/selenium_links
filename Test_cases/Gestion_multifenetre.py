# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)

Title = driver.title
print("Title of first page is:", Title)
first_page_url = driver.current_url
print("Current page url is:", first_page_url)

lienorange = driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc")

parent_handle = driver.current_window_handle

print(parent_handle)
lienorange.click()

window_ids = driver.window_handles
parent_id_0 = window_ids[0]
child_id_1 = window_ids[1]
driver.switch_to.window(child_id_1)

print(len(window_ids))
# print(window_ids[0])
# print(window_ids[1])

second_page_title = driver.title
print("Second page title: ", second_page_title)
second_page_url = driver.current_url
print("Second page url is:", second_page_url)

driver.switch_to.window(parent_id_0)
time.sleep(5)

driver.quit()