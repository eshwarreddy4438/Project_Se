from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
options = Options()
# Path to your ChromeDriver executable
service = Service(r"C:\Users\eshwa\.cache\selenium\chromedriver\win64\130.0.6723.91\chromedriver.exe")

# Initialize the driver with options and service
driver = webdriver.Chrome(service=service, options=options)

# Open Google
driver.get("https://www.google.com")
driver.maximize_window()
# Add any required waits or further code here
time.sleep(5)  # Example wait to keep the browser open for 5 seconds
driver.get('https://www.youtube.com')
time.sleep(3)
driver.back()
time.sleep(2)
driver.forward()
# Close the browser after the actions are done
driver.quit()
