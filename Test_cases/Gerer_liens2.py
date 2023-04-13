# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.bdeb.qc.ca/formation-continue/")
driver.maximize_window()
time.sleep(3)
#compter le nombre de liens sur le site
liens = driver.find_elements(By.XPATH, "//a")
# print("Nombre de lien sur le site du college est:",len(liens))
# print(len(liens))

#Afficher le texte de chaque lien
# for lien in liens:
#     #print(lien.text)
#     #print(lien.get_attribute("href"))

liens_colonne_gauche = driver.find_elements(By.XPATH, "//aside//a")
print(type(liens_colonne_gauche))
print("Nombre de liens colonnes gauche sur le site est: ", len(liens_colonne_gauche))

for lien in liens_colonne_gauche:
    print(lien.text)
    if lien.text=="Cours de perfectionnement":
        lien.click()
        time.sleep(3)

driver.quit()