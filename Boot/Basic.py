# Importing Packaging:
import os
from rich.console import Console
from rich.table import Table

# Global Variables
console = Console()
newLine = '\n'

# Prices of Product
Sale_Price = 49
Import_Price = 14
Shipping_Price = 22
Profit = Sale_Price - (Import_Price + Shipping_Price)

# Financial Information
Available_Amount = int(input('Enter Your Capital: '))
Saving_Amount = 0

# Batchs Information
Batch = 0
BatchMax = int(input('Enter Batches: '))
Quantity_of_Products = 0


table = Table(show_header=True, header_style="bold red")
table.add_column("Batch", justify="left")
table.add_column("Products", justify="left")
table.add_column("Deal Price", justify="left")
table.add_column("Shipping Price", justify="left")
table.add_column("Profit", justify="left")
table.add_column("Cash", justify="left")
for i in range(BatchMax):
    Batch += 1
    Quantity_of_Products = int(Available_Amount / Import_Price)
    table.add_row(
        "{}".format(Batch),
        "{:,}".format(Quantity_of_Products),
        "{:,} SAR".format(Quantity_of_Products * Sale_Price),
        "{:,} SAR".format(Quantity_of_Products * Shipping_Price),
        "{:,} SAR".format(Quantity_of_Products * Profit),
        "{:,} SAR".format(Quantity_of_Products * (Sale_Price - Shipping_Price)),
    )

    Available_Amount = Quantity_of_Products * (Sale_Price - Shipping_Price)

console.print(table)