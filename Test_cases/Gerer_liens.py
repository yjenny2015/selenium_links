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

#driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
lienorange = driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc")
lienorange.click()
time.sleep(5)
#driver.close()
driver.quit()
#time.sleep(3)