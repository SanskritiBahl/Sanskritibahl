import pandas as pd
import matplotlib.pyplot as plt

# Load the merged CSV file
merged_file = 'merged_file.csv'
df = pd.read_csv(merged_file)


def convert_to_float(price_str):
    # Split the concatenated price values, remove currency symbol '₹' and commas, then convert to float
    prices = price_str.split('₹')
    cleaned_prices = []
    for price in prices:
        try:
            cleaned_price = float(price.replace(',', '').strip())
            cleaned_prices.append(cleaned_price)
        except ValueError:
            pass
    return sum(cleaned_prices) / len(cleaned_prices) if cleaned_prices else 0.0


df['Price'] = df['Price'].apply(convert_to_float)
df['Original Price (Was Price)'] = df['Original Price (Was Price)'].apply(convert_to_float)
df['Offer Price'] = df['Offer Price'].apply(convert_to_float)

# Filter data for Scarves and Stoles category
scarves_df = df[df['Category'] == 'Scarves and Stoles']

# Filter data for Caps category
caps_df = df[df['Category'] == 'Caps']


# Function to get the top two selling brands in a category
def get_top_selling_brands(category_df):
    brand_counts = category_df['Brand Name'].value_counts()
    top_selling_brands = brand_counts.head(2)
    return top_selling_brands


# Get the top two selling brands for Scarves and Stoles
scarves_top_brands = get_top_selling_brands(scarves_df)

# Get the top two selling brands for Caps
caps_top_brands = get_top_selling_brands(caps_df)

# Plot a bar graph for the top-selling brands in Scarves and Stoles
plt.figure(figsize=(10, 8))
scarves_top_brands.plot(kind='bar', color='skyblue')
plt.xlabel('Brand Name')
plt.ylabel('Number of Products Sold')
plt.title('Top Selling Brands in Scarves and Stoles Category')
plt.xticks()
plt.show()

# Plot a bar graph for the top-selling brands in Caps
plt.figure(figsize=(10, 8))
caps_top_brands.plot(kind='bar', color='lightcoral')
plt.xlabel('Brand Name')
plt.ylabel('Number of Products Sold')
plt.title('Top Selling Brands in Caps Category')
plt.xticks()
plt.show()


def generate_category_stats_and_graph(category_df, category_name):
    # Calculate average Original Price (Was Price) and after discount
    avg_price_before_discount = category_df['Original Price (Was Price)'].mean()
    avg_price_after_discount = category_df['Price'].mean()  # Use the cleaned 'Price' column

    # Calculate minimum and maximum prices
    min_price = category_df['Original Price (Was Price)'].min()
    max_price = category_df['Original Price (Was Price)'].max()

    # Create a bar graph for average prices
    plt.figure(figsize=(10, 8))
    plt.bar(['Average Original Price (Was Price)', 'Average Price After Discount'],
            [avg_price_before_discount, avg_price_after_discount], color=['skyblue', 'lightcoral'])
    plt.xlabel('Category: ' + category_name)
    plt.ylabel('Price (in INR)')
    plt.title('Average Prices for ' + category_name)
    plt.xticks()
    plt.show()

    # Create a bar graph for minimum and maximum prices
    plt.figure(figsize=(10, 8))
    plt.bar(['Minimum Price', 'Maximum Price'], [min_price, max_price], color=['mediumseagreen', 'lightpink'])
    plt.xlabel('Category: ' + category_name)
    plt.ylabel('Price (in INR)')
    plt.title('Minimum and Maximum Prices for ' + category_name)
    plt.xticks()
    plt.show()


# Generate statistics and graphs for Scarves and Stoles category
generate_category_stats_and_graph(scarves_df, 'Scarves and Stoles')

# Generate statistics and graphs for Caps category
generate_category_stats_and_graph(caps_df, 'Caps')


# Calculate average mean prices for Scarves and Stoles before and after discount
avg_mean_price_scarves_before_discount = scarves_df['Original Price (Was Price)'].mean()
avg_mean_price_scarves_after_discount = scarves_df['Price'].mean()

# Calculate average mean prices for Caps before and after discount
avg_mean_price_caps_before_discount = caps_df['Original Price (Was Price)'].mean()
avg_mean_price_caps_after_discount = caps_df['Price'].mean()

# Calculate the standard deviation for scarves before discount
std_deviation_scarves_before_discount = scarves_df['Original Price (Was Price)'].std()

# Calculate the standard deviation for scarves after discount
std_deviation_scarves_after_discount = scarves_df['Price'].std()

# Calculate the standard deviation for caps before discount
std_deviation_caps_before_discount = caps_df['Original Price (Was Price)'].std()

# Calculate the standard deviation for scarves after discount
std_deviation_caps_after_discount = caps_df['Price'].std()




# Calculate the first quartile before discount
first_quartile_scarves_before_discount = scarves_df['Original Price (Was Price)'].quantile(0.25)
first_quartile_caps_before_discount = caps_df['Original Price (Was Price)'].quantile(0.25)

# Calculate the second quartile before discount 
second_quartile_scarves_before_discount = scarves_df['Original Price (Was Price)'].quantile(0.50)
second_quartile_caps_before_discount = caps_df['Original Price (Was Price)'].quantile(0.50)


# Calculate the third quartile before discount 
third_quartile_scarves_before_discount = scarves_df['Original Price (Was Price)'].quantile(0.75)
third_quartile_caps_before_discount = caps_df['Original Price (Was Price)'].quantile(0.75)


# Calculate the first quartile after discount
first_quartile_scarves_after_discount = scarves_df['Price'].quantile(0.25)
first_quartile_caps_after_discount = caps_df['Price'].quantile(0.25)

# Calculate the second quartile after discount 
second_quartile_scarves_after_discount = scarves_df['Price'].quantile(0.50)
second_quartile_caps_after_discount = caps_df['Price'].quantile(0.50)


# Calculate the third quartile after discount 
third_quartile_scarves_after_discount = scarves_df['Price'].quantile(0.75)
third_quartile_caps_after_discount = caps_df['Price'].quantile(0.75)

# Print the results of average mean
print(f'Average Mean Price Before Discount for Scarves and Stoles: ₹{avg_mean_price_scarves_before_discount:.2f}')
print(f'Average Mean Price After Discount for Scarves and Stoles: ₹{avg_mean_price_scarves_after_discount:.2f}')
print(f'Average Mean Price Before Discount for Caps: ₹{avg_mean_price_caps_before_discount:.2f}')
print(f'Average Mean Price After Discount for Caps: ₹{avg_mean_price_caps_after_discount:.2f}')
# Print the results of standard deviation
print(f'Standard Deviation Before Discount for Scarves: ₹{std_deviation_scarves_before_discount:.2f}')
print(f'Standard Deviation After Discount for Scarves: ₹{std_deviation_scarves_after_discount:.2f}')
print(f'Standard Deviation Before Discount for Caps: ₹{std_deviation_caps_before_discount:.2f}')
print(f'Standard Deviation After Discount for Caps: ₹{std_deviation_caps_after_discount:.2f}')
# Print the results of quartiles before discount
print(f'First Quartile Before Discount for Scarves: ₹{first_quartile_scarves_before_discount:.2f}')
print(f'First Quartile Before Discount for Caps: ₹{first_quartile_caps_before_discount:.2f}')
print(f'Second Quartile Before Discount for Scarves: ₹{second_quartile_scarves_before_discount:.2f}')
print(f'Second Quartile Before Discount for Caps: ₹{second_quartile_caps_before_discount:.2f}')
print(f'Third Quartile Before Discount for Scarves: ₹{third_quartile_scarves_before_discount:.2f}')
print(f'Third Quartile Before Discount for Caps: ₹{third_quartile_caps_before_discount:.2f}')

# Print the results of quartiles after discount
print(f'First Quartile After Discount for Scarves: ₹{first_quartile_scarves_after_discount:.2f}')
print(f'First Quartile After Discount for Caps: ₹{first_quartile_caps_after_discount:.2f}')
print(f'Second Quartile After Discount for Scarves: ₹{second_quartile_scarves_after_discount:.2f}')
print(f'Second Quartile After Discount for Caps: ₹{second_quartile_caps_after_discount:.2f}')
print(f'Third Quartile After Discount for Scarves: ₹{third_quartile_scarves_after_discount:.2f}')
print(f'Third Quartile After Discount for Caps: ₹{third_quartile_caps_after_discount:.2f}')