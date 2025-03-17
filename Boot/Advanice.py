# Importing Packaging:
import time
from rich.console import Console
from rich.table import Table
# test = int(input('Count of Prodect: '))

# Global Variables
console = Console()

# Prices of Product
Sale_Price = 49
Import_Price = 14
Shipping_Price = 22
Profit = Sale_Price - (Import_Price + Shipping_Price)

# Information of Packaging
Packaging_Quantity = 500
Price_of_Packaging = 3500

# Financial Information
Available_Amount = 700
Saving_Amount = 0

# Batchs Information
Batch = 0
Quantity_of_Products = 0


# Importing Method
def Importing():
    # Editing Global Variables
    global Quantity_of_Products, Available_Amount
    
    Quantity_of_Products = int(Available_Amount / Import_Price) - 1
    Available_Amount = Available_Amount - (Quantity_of_Products * Import_Price)
    # print(Quantity_of_Products)
    # print(Available_Amount)

    start()

# Packaging Method
def Packaging():
    # Editing Global Variables
    global Available_Amount, Packaging_Quantity
    
    print(Available_Amount)
    if Available_Amount > Price_of_Packaging:
        Available_Amount -= Price_of_Packaging
        Packaging_Quantity = 500
    else:
        raise Exception('Cash is not Enogh For Packaging !')

    start()

# Selling Method
def Selling():
    # Editing Global Variables
    global Quantity_of_Products, Available_Amount, Packaging_Quantity, Batch

    Batch += 1
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Products", justify="center")
    table.add_column("Shipping Price", justify="left")
    table.add_column("Profit", justify="left")
    table.add_column("Deal Price", justify="left")
    table.add_column("Cash", justify="left")
    table.add_row(
        "{:,}".format(Quantity_of_Products),
        "{:,} SAR".format(Quantity_of_Products * Shipping_Price),
        "{:,} SAR".format(Quantity_of_Products * Profit),
        "{:,} SAR".format(Quantity_of_Products * Sale_Price),
        "{:,} SAR".format(Quantity_of_Products * (Sale_Price - Shipping_Price)),
    )
    console.print("\nBatch Num: {}".format(Batch), style="bold yellow")
    # print('\nBatch Num: {}'.format(Batch))
    # print('Quantity of Products: {:,}'.format(Quantity_of_Products))
    # print('Shipping Price: {:,} SAR'.format(Quantity_of_Products * Shipping_Price))
    # print('Profit: {:,} SAR'.format(Quantity_of_Products * Profit))
    # print('Deal Price: {:,} SAR'.format(Quantity_of_Products * Sale_Price))
    # print('Cash: {:,} SAR'.format(Quantity_of_Products * (Sale_Price - Shipping_Price)))
    console.print(table)

    Available_Amount = Quantity_of_Products * (Sale_Price - Shipping_Price)
    Packaging_Quantity -= Quantity_of_Products
    Quantity_of_Products = 0
    
    # print(Available_Amount)
    # print(Packaging_Quantity)

    start()

def start():
    try:
        if Batch < 7:
            if not Available_Amount == 0:
                if not Quantity_of_Products == 0:
                    if not Packaging_Quantity == 0:
                        Selling()
                    else:
                        print(Available_Amount)
                        Packaging()
                else:
                    Importing()
            else:
                raise Exception('error fuck *_*')
        else:
            raise Exception('non')
    except Exception as Error:
        print(Error)

start()