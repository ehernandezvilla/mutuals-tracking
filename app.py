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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(400, 800))
# display.start()


# Set up WebDriver Options
chrome_options = Options()
options = webdriver.ChromeOptions()

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode.
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model.
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems.
chrome_options.add_argument("--remote-debugging-port=9222")  # Remote debugging port.
chrome_options.add_argument("--window-size=1920,1080")


# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


# Navigate to the page
driver.get("https://www.santanderassetmanagement.cl/buscador-de-fondos")

# driver.save_screenshot('screenshot.png')
# Locate the table
# Adjust the selector if necessary to target the specific table
# wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
table = driver.find_element(By.TAG_NAME, "table")

# print(driver.page_source)

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

print('processing')

# Create a DF
df = pd.DataFrame(data[1:], columns=data[0])

print(df)

# Save the extracted data to a CSV file
# csv_file_path = "funds_data.csv"
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print(f"Data saved to {csv_file_path}")
print('end')