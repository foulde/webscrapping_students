from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up WebDriver
# driver_path = 'path_to_your_chromedriver.exe'  # Replace with your ChromeDriver path
driver_path = 'C:/Users/hugod/AppData/Local/Programs/Python/Python310/chromedriver.exe'

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the website
url = 'https://www.franprix.fr/courses/promotions'
driver.get(url)

# Wait for the dynamic content to load
time.sleep(8)

# Find elements containing the promotions
promotions = driver.find_elements(By.CSS_SELECTOR, 'div.product-item__promo__regular span')

# Extract text from each element
promo_texts = [promo.text for promo in promotions]

# Process text to extract percentage values
percentages = []
for text in promo_texts:
    if '%' in text:
        # Extract and clean the percentage value
        percentage = text.split('%')[0].strip()
        percentages.append(percentage)

# Create a DataFrame
df = pd.DataFrame(percentages, columns=['Discount Percentage'])
df.to_csv('promotions_franprix.csv', index=False)
# Close the browser
driver.quit()

# Output the DataFrame
print(df)
