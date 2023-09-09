import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

# Function to scroll to the bottom of the page to load more products
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Adjust the sleep time as needed
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Function to extract product details from a product item
def extract_product_details(product_item):
    product_data = {
        "S.No": "",
        "Product Code": None,
        "Brand Name": None,
        "Product Name": None,
        "Price": None,
        "Original Price (Was Price)": None,
        "Discount Percentage": None,
        "Offer Price": None,
        "URL": None
    }

    try:
        product_data["Product Code"] = product_item.find('a', class_='rilrtl-products-list__link')['href'].split('/')[
            -1]
    except AttributeError:
        pass

    try:
        product_data["Brand Name"] = product_item.find('div', class_='brand').text.strip()
    except AttributeError:
        pass

    try:
        product_data["Product Name"] = product_item.find('div', class_='nameCls').text.strip()
    except AttributeError:
        pass

    try:
        product_data["Price"] = product_item.find('span', class_='price').text.strip()
    except AttributeError:
        pass

    try:
        product_data["Original Price (Was Price)"] = product_item.find('span', class_='orginal-price').text.strip()
    except AttributeError:
        product_data["Original Price (Was Price)"] = product_data["Price"]

    try:
        product_data["Discount Percentage"] = product_item.find('span', class_='discount').text.strip()
    except AttributeError:
        product_data["Discount Percentage"] = "(0% off)"

    try:
        product_data["Offer Price"] = product_item.find('span', class_='offer-pricess').text.strip()
    except AttributeError:
        product_data["Offer Price"] = product_data["Price"]

    try:
        product_data[
            "URL"] = f"https://www.ajio.com{product_item.find('a', class_='rilrtl-products-list__link')['href']}"
    except AttributeError:
        pass

    return product_data


# Initialize the WebDriver
print("Initializing the WebDriver...")
driver = webdriver.Chrome()
print("WebDriver initialized successfully.")
# Navigate to the AJIO URL
ajio_url = 'https://www.ajio.com/s/clothing-4461-74581?query=:relevance:l1l3nestedcategory:Men%20-%20Scarves&curated=true&curatedid=clothing-4461-74581&gridColumns=3&segmentIds='
driver.get(ajio_url)

# Scroll to the bottom of the page to load all items
scroll_to_bottom(driver)

# Get the HTML content of the page
page_html = driver.page_source
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_html, 'html.parser')

fields = [
    "S.No",
    "Product Code",
    "Brand Name",
    "Product Name",
    "Price",
    "Original Price (Was Price)",
    "Discount Percentage",
    "Offer Price",
    "URL"
]

# Create a CSV file for writing
with open('product_data_html.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(fields)  # Write the header row

    # Find all product items in the HTML
    product_items = soup.find_all('div', class_='item')

    # Loop through each product item and extract details
    for i, product_item in enumerate(product_items, start=1):
        product_data = extract_product_details(product_item)
        product_data["S.No"] = i

        # Write the data to the CSV file
        row = [product_data[field] for field in fields]
        writer.writerow(row)

print("CSV file 'product_data_html.csv' has been created.")








