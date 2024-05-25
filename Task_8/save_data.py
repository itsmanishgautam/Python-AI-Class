import csv

def get_product_data():
    product_name = input("Enter the product name: ")
    cost = float(input("Enter the cost of the product: "))
    category = input("Enter the category of the product: ")
    color = input("Enter the color of the product: ")
    container = input("Enter the container type: ")

    product_data = {
        "Product Name": product_name,
        "Cost": cost,
        "Category": category,
        "Color": color,
        "Container":container
    }

    return product_data

csv_filename = "Task_8/csv/product_data.csv"

while True:
    product_data = get_product_data()

    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=product_data.keys())

        writer.writeheader()

        writer.writerow(product_data)

    choice = input("Do you want to enter data for another product? (yes/no): ")
    if choice.lower() != 'yes':
        break

print(f"Product data exported to {csv_filename}")
