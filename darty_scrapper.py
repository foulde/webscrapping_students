import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape
url = 'https://www.darty.com/nav/operation/bons-plans-gros-electromenager#dartyclic=PO-bons-plan_BLGF_deco-nos-prom_0_gros-elec'

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all article elements that have a class 'product'
    products = soup.find_all('article', class_='product')

    # Open a CSV file to write the data
    with open('darty_promo1.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header of the CSV file
        writer.writerow(['Product Name', 'Original Price (€)', 'Current Price (€)', 'Promotion Percentage'])

        # Loop over all product articles found
        for product in products:
            # Extract the product name
            name = product.find('a', class_='name').text.strip()

            # Extract the original and current prices
            price_promo = product.find('div', class_='price price_promo').text.strip().replace('€', '').replace(',', '.').replace(u'\xa0', u' ')
            striped_price = product.find('div', class_='striped_price').text.strip().replace('€', '').replace(',', '.').replace(u'\xa0', u' ')
            
            # Calculate the promotion percentage
            original_price = float(striped_price)
            current_price = float(price_promo)
            promotion_percentage = ((original_price - current_price) / original_price) * 100

            # Write the product data to the CSV file
            writer.writerow([name, original_price, current_price, f'{promotion_percentage:.2f}%'])
else:
    print('Failed to retrieve the webpage')
