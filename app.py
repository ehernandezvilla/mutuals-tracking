from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from datetime import date
import os
import arrow
import pandas as pd
from time import sleep
from pyvirtualdisplay import Display


display = Display(visible=0, size=(400, 800))
display.start()

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
driver.maximize_window()

#login flow

#open the webpage
driver.get("URL")

#target email
email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
#enter username and password
email.clear()
email.send_keys('ID_EMAIL')

#target password
password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
#enter and password
password.clear()
password.send_keys('PASSW_KEY')


submit = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
driver.implicitly_wait(20)
#after_codeclick = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
#We are logged in!


#FLUJO DE DESCARGA 

#Ingreso a seccion rides

rides = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-home-layout/div/app-nav/header/nav/a[4]/span"))).click()

arw = arrow.utcnow()
today = arw.shift(days=-1).format('DD') 
today = int(today)
today = today - 1
today = str(today)

#Date selection 

driver.find_element(By.XPATH, '/html/body/app-root/app-home-layout/div/app-order/app-order-list/div[1]/div/div/div[2]/div[2]/div[1]/mat-form-field[1]/div/div[1]/div[2]/mat-datepicker-toggle/button').click()

alldates=driver.find_elements(By.XPATH,'//table[@class="mat-calendar-table"]//div[@class="mat-calendar-body-cell-content"]')

for dateselements in alldates:
    date=dateselements.text
    #print(date)
    if date==today: 
        dateselements.click()
        break

#Descarga de documentos

download = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-home-layout/div/app-order/app-order-list/div[1]/div/div/div[2]/div[2]/div[2]/button/span/mat-icon"))).click()