############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

Product.objects.all().delete()

products = [
    ("001", "Milk", "5.99"),
    ("002", "Eggs", "4.00"),
    ("003", "Bread", "2.99"),
    ("004", "Butter", "4.99"),
    ("005", "Protein Powder", "65.99"),
    ("006", "Cottage Cheese", "14.99"),
    ("007", "Kiwi", "7.99"),
]
print("Added Products:")
for p in products:
    product = Product.objects.create(upc=p[0], name=p[1], price=p[2])
    print(product.upc, product.name, product.price)


import tkinter as tk
from scanner import CashRegisterGUI

root = tk.Tk()
CashRegisterGUI(root)
root.mainloop()
