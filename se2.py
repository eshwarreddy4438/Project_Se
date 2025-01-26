from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Import the By class
import time

options = Options()

service = Service(r"C:\Users\eshwa\.cache\selenium\chromedriver\win64\130.0.6723.91\chromedriver.exe")

driver = webdriver.Chrome(service = service, options = options)

#driver.get('https://www.w3schools.com/html/exercise.asp?x=xrcise_intro1')
#time.sleep(3)
#driver.find_element(By.XPATH, '//*[@id="qobj_options"]/div[3]/label').click()
#time.sleep(3)

#driver.get('https://www.youtube.com/results?search_query=selenium+tutorial+for+beginners')
#links = driver.find_elements(By.TAG_NAME, 'a')
#for i in links:
#    print(i.text)

driver.get('https://testautomationpractice.blogspot.com/')
#driver.find_element(By.XPATH, '//*[@id="alertBtn"]').click()
# Switch to the alert and accept it
#time.sleep(3)
#driver.switch_to.alert.accept()
#time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-input"]').send_keys('hello')
time.sleep(3)
driver.quit()