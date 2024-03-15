from datetime import date
import csv
import os
import arrow
import pandas as pd
from time import sleep
from utils.db import insert_data
# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(400, 800))
# display.start()


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode.
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model.
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems.
chrome_options.add_argument("--remote-debugging-port=9222")  # Remote debugging port.

driver = webdriver.Chrome(options=chrome_options)

# Initialize WebDriver
driver.maximize_window()


# Navigate to the page
driver.get("https://www.santanderassetmanagement.cl/buscador-de-fondos")
sleep(5)  # Wait for the page to load

# Locate the table
# Adjust the selector if necessary to target the specific table
table = driver.find_element(By.TAG_NAME, "table")

# Extract data from the table
data = []
# Header
headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]
data.append(headers)

# Rows
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")  # or 'td' for data cells
    if cols:  # This skips the header row
        data.append([col.text for col in cols])

# Close the WebDriver
driver.quit()

# Create a DF
df = pd.DataFrame(data[1:], columns=data[0])

# Convert the DataFrame to a list of tuples, one for each row
data_tuples = [tuple(x) for x in df.to_numpy()]

# Call the insert_data function with the prepared data
insert_data(data_tuples)

print('Data insertion complete.')