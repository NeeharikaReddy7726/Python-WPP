
products = {}

#1:product names and prices
while True:
    name = input("Enter product name (or 'done' to stop): ").strip()
    if name.lower() == 'done':  
        break
    try:
        price = float(input(f"Enter price for {name}: "))
        products[name] = price 
    except ValueError:
        print("Invalid price. Please enter a valid number.")

#2: userto look up prod price
print("\nProduct lookup:")
while True:
    query = input("Enter a product name to get its price (or 'exit' to stop): ").strip()
    if query.lower() == 'exit': 
        break
    price = products.get(query)
    if price is not None:
        print(f"The price of {query} is ${price:.2f}")
    else:
        print(f"{query} not found in the product list.")