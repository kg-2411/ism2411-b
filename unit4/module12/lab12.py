# REFLECTION
# 1. Python and Excel can both organize data, calculate totals, and create reports.
# Python is better for automating repetitive tasks and handling large amounts of data.
# Excel is easier for quickly viewing data, making charts, and doing calculations manually.

# 2. A business could use an append-mode log file to track daily sales.
# Append mode is useful because it saves each new entry without deleting previous records.


import csv
from datetime import datetime


# EXERCISE 2: Read and print raw rows


with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# EXERCISE 3: Skip the header


with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4: Compute totals


total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"].strip()
        price = float(row["price"].strip())
        quantity = int(row["quantity"].strip())

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")


# EXERCISE 5: Filter and Write


original_count = 0
written_count = 0

with open("data/sales.csv", "r") as infile:
    reader = csv.DictReader(infile)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row["product"].strip()
            price = float(row["price"].strip())
            quantity = int(row["quantity"].strip())

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1

print(f"Original rows: {original_count}")
print(f"Rows written: {written_count}")


# EXERCISE 6: csv.DictReader


dict_total = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"].strip()
        price = float(row["price"].strip())
        quantity = int(row["quantity"].strip())

        total = price * quantity
        dict_total += total

print(f"Total Revenue using DictReader: ${dict_total:.2f}")

# csv.reader accesses information using column positions (indexes).
# DictReader uses column names, making the code easier to read and understand.


# EXERCISE 7: Sales Summary by Product


sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"].strip()
        price = float(row["price"].strip())
        quantity = int(row["quantity"].strip())

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# EXERCISE 8: Append Mode Log


current_time = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(
        f"{current_time}: Total Revenue = ${total_revenue:.2f}\n")
    
