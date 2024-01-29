# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Set up the WebDriver (example with Chrome)
# # driver_path = 'path_to_your_chromedriver.exe'  # Replace with the path to your ChromeDriver
# driver_path = 'C:/Users/hugod/AppData/Local/Programs/Python/Python310/chromedriver.exe'

# driver = webdriver.Chrome(driver_path)

# # Navigate to the website
# url = 'https://www.fnac.com/Toutes-nos-Offres-TV-Video-Home-cinema/shi74185/w-4#bl=MMtvh'
# driver.get(url)

# # Give some time for the page to load
# time.sleep(5)

# # Find elements by class name and extract text
# prices_red = driver.find_elements(By.CLASS_NAME, 'price.red')
# standard_prices = driver.find_elements(By.CLASS_NAME, 'Prix.standard')
# discounts = driver.find_elements(By.CSS_SELECTOR, 'span.stimuliOPC-flyer-price span')

# # Extract and print the data
# for price in prices_red:
#     print(price.text)

# for price in standard_prices:
#     print(price.text)

# for discount in discounts:
#     print(discount.text)

# # Close the browser
# driver.quit()












# ////////////////////////
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

# Set up the WebDriver with Service
driver_path = 'C:/Users/hugod/AppData/Local/Programs/Python/Python310/chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# # ////////////////////
# # Set up the WebDriver (example with Chrome)
# driver_path = 'C:/Users/hugod/AppData/Local/Programs/Python/Python310/chromedriver.exe'
# driver = webdriver.Chrome(driver_path)

# Navigate to the website
url = 'https://www.fnac.com/Toutes-nos-Offres-TV-Video-Home-cinema/shi74185/w-4#bl=MMtvh'
driver.get(url)

# Give some time for the page to load
time.sleep(14)

# Find elements by class name and extract text
prices_red = driver.find_elements(By.CLASS_NAME, 'price.red')
standard_prices = driver.find_elements(By.CLASS_NAME, 'Prix.standard')
discounts = driver.find_elements(By.CSS_SELECTOR, 'span.stimuliOPC-flyer-price span')

# Prepare data for CSV
data = []
for price, standard_price, discount in zip(prices_red, standard_prices, discounts):
    data.append([price.text, standard_price.text, discount.text])

# Write data to a CSV file
with open('product_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price (Red)', 'Standard Price', 'Discount'])
    writer.writerows(data)

# Close the browser
driver.quit()
