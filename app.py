from datetime import date
import csv
import os
import arrow
import pandas as pd
from time import sleep
from utils.db import insert_data, create_table, create_database
# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(400, 800))
# display.start()

# create_database()


# Set up WebDriver Options
chrome_options = Options()
options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")  # Run Chrome in headless mode.
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model.
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems.
chrome_options.add_argument("--remote-debugging-port=9222")  # Remote debugging port.
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


# Navigate to the page
driver.get("https://www.santanderassetmanagement.cl/buscador-de-fondos")

sleep(10)

# table = driver.find_element(By.TAG_NAME, "table")

# Use CSS selector to locate the table
table = driver.find_element(By.CSS_SELECTOR, "table.table")


# Extract data from the table
data = []


# Header: Use CSS selector to find 'th' elements within the table
headers = [header.text for header in table.find_elements(By.CSS_SELECTOR, "thead th")]
data.append(headers)

# Rows: Use CSS selector to find 'tr' elements within the table body 'tbody'
rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
for row in rows:
    # For each row, find 'td' elements representing the cells
    cols = row.find_elements(By.CSS_SELECTOR, "td")
    if cols:  # This skips any rows without 'td' elements
        data.append([col.text for col in cols])



# Close the WebDriver
driver.quit()

print('processing')

# create_table()

# Create a DF
df = pd.DataFrame(data[1:], columns=data[0])

# Convert the DataFrame to a list of tuples, one for each row
data_tuples = [tuple(x) for x in df.to_numpy()]

# Call the insert_data function with the prepared data
insert_data(data_tuples)

print('Data insertion complete.')

# print(df)

print('end')

