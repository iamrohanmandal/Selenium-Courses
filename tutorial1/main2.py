import os
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
os.environ['PATH'] += r"G:/python datascience ml/Selenium Course/SeleniumDrivers"

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
# driver.find_element_by_id()
driver.implicitly_wait(5)
try:
    no_button = driver.find_element(By.CLASS_NAME,'at-cm-no-button')
    no_button.click()
except:
    print('No element of this class So Skipping....')
sum1 = driver.find_element(By.ID,'sum1')
sum2 = driver.find_element(By.ID,'sum2')
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(165)
btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()