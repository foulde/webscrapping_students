# # import requests
# # from bs4 import BeautifulSoup
# # import csv

# # # URL of the page to scrape
# # # url = 'https://www.adidas.fr/hommes-outlet'
# # url = 'https://www.adidas.fr/hommes-outlet'

# # # Send a GET request to the page
# # response = requests.get(url)

# # # Check if the request was successful
# # if response.status_code == 200:
# #     # Parse the HTML content of the page
# #     soup = BeautifulSoup(response.text, 'html.parser')
    
# #     # Find all elements with the class 'grid-item'
# #     grid_items = soup.find_all('div', class_='grid-item')

# #     # Open a CSV file to write the data
# #     with open('adidas_promo.csv', mode='w', newline='', encoding='utf-8') as file:
# #         writer = csv.writer(file)
# #         # Write the header of the CSV file
# #         writer.writerow(['Product Name', 'Original Price (€)', 'Current Price (€)', 'Promotion Percentage'])

# #         # Loop over all grid items found
# #         for item in grid_items:
# #             # You would need to adjust these find operations based on the actual HTML structure
# #             # Extract the product name
# #             name = item.find('grid-item').text.strip()

# #             # Extract the original and current prices
# #             original_price = item.find('SOME_SELECTOR_FOR_ORIGINAL_PRICE').text.strip().replace('€', '').replace(',', '.').replace(u'\xa0', u' ')
# #             current_price = item.find('SOME_SELECTOR_FOR_CURRENT_PRICE').text.strip().replace('€', '').replace(',', '.').replace(u'\xa0', u' ')
            
# #             # Calculate the promotion percentage
# #             try:
# #                 original_price = float(original_price)
# #                 current_price = float(current_price)
# #                 promotion_percentage = ((original_price - current_price) / original_price) * 100
# #                 promotion_percentage_str = f'{promotion_percentage:.2f}%'
# #             except ValueError:  # In case of conversion error, set the values to None or an appropriate default
# #                 promotion_percentage_str = None

# #             # Write the product data to the CSV file
# #             writer.writerow([name, original_price, current_price, promotion_percentage_str])
# # else:
# #     print('Failed to retrieve the webpage')


# import requests
# from bs4 import BeautifulSoup
# import csv

# # URL of the page to scrape
# # url = 'URL_OF_THE_WEBSITE'
# url = 'https://www.adidas.fr/hommes-outlet'

# # Send a GET request to the page
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     print("tomate")
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find all elements with the class 'grid-item'
#     grid_items = soup.find_all('div', class_='grid-item')

#     # Open a CSV file to write the data
#     with open('adidas_scrapped.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         # Write the header of the CSV file
#         writer.writerow(['Product Name', 'Original Price (€)', 'Current Price (€)', 'Promotion Percentage'])

#         # Loop over all grid items found
#         for item in grid_items:
#             # Extract the product name (You need to replace 'product-card-content-badges-wrapper___2RWqS' with the actual class for the product name if different)
#             name_link = item.find('a', class_='product-card-content-badges-wrapper___2RWqS')
#             name = name_link.text.strip() if name_link else "Unknown Product"

#             # Extract the original and current prices and the promotion percentage
#             price_container = item.find('div', class_='badge-container___1TJjk discount-badge___318Q7')
#             if price_container:
#                 promotion_percentage = price_container.text.strip().replace('%', '')
#                 original_price_text = price_container.find_next_sibling('div').find('div', class_='gl-price-item gl-price-item--crossed notranslate')
#                 current_price_text = price_container.find_next_sibling('div').find('div', class_='gl-price-item gl-price-item--sale notranslate')

#                 if original_price_text and current_price_text:
#                     original_price = original_price_text.text.strip().replace('€', '').replace(',', '.').replace(u'\xa0', u' ')
#                     current_price = current_price_text.text.strip().replace('€', '').replace(',', '.').replace(u'\xa0', u' ')

#                     # Write the product data to the CSV file
#                     writer.writerow([name, original_price, current_price, promotion_percentage])
# else:
#     print('Failed to retrieve the webpage')



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv

# URL of the page to scrape
url = 'https://www.adidas.fr/hommes-outlet'
driver_path = 'C:/Users/hugod/AppData/Local/Programs/Python/Python310/chromedriver.exe'

# Set up the Selenium WebDriver
options = Options()
options.headless = True  # Running in headless mode
service = Service(executable_path=driver_path)  # Update this path
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the page
driver.get(url)

# Wait for the dynamic content to load
time.sleep(5)  # The time may need to be adjusted

# Now that the page is loaded, we can pass the HTML to BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all elements with the class 'grid-item'
grid_items = soup.find_all('div', class_='grid-item')

# Open a CSV file to write the data
with open('adidas_scrapped.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header of the CSV file
    writer.writerow(['Product Name', 'Original Price (€)', 'Current Price (€)', 'Promotion Percentage'])

    # Loop over all grid items found
    for item in grid_items:
        # The rest of your code to extract the data goes here...
        # ...

# Don't forget to close the driver after the scraping is done
        driver.quit()
