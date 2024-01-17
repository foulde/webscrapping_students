from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv

# Configure Selenium to use Chrome in headless mode
options = Options()
options.headless = True

# Path to your ChromeDriver
chromedriver_path = 'C:/Users/hugod/AppData/Local/Programs/Python/Python310/chromedriver.exe'

# Initialize Selenium WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL to scrape
# url = 'https://example.com/promotions'  # Replace with the actual URL
url= 'https://www.auchan.fr/boutique/promos'

# Selenium navigates to the page
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)  # Adjust time as needed

# Get the page source from Selenium
page_source = driver.page_source

# Close the Selenium WebDriver
driver.quit()

# Now use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find elements containing the product information
product_elements = soup.find_all('p', class_='product-thumbnail__description')

# CSV file path
csv_file_path = 'promotion_auchan.csv'  # Update this path

# Create a CSV file to store the data
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Brand', 'Description'])

    for product in product_elements:
        brand = product.find('strong', itemprop='brand').text if product.find('strong', itemprop='brand') else 'N/A'
        description = product.get_text(separator=' ', strip=True)
        writer.writerow([brand, description])

print(f'Data written to {csv_file_path}')
