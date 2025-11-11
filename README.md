Group 32 
----------------------------
Mohid Sohail, Mohammad Burhan, Hanzlah Imran


:open_file_folder: Project Overview and File folder
---------------------------------
This project uses Django ORM to create a stand-alone cash register application. It includes a Graphical User Interface (GUI) that allows the user to simulate adding products to their cart based on their UPC code and computes the total bill of all items. Products to be sold can be entered into the database with their name, price, and UPC code.


The scanner.py is the user interface for the cash register system, the items are created and populate the database in main.py, and the model for the product object is created in db/models.py.
```

django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
├── main.py
├── manage.py
├── README.md
└── settings.py
└── scanner.py
└── db.sqlite3
```

Step 1
----------
Initlize the virtuql machine
<img width="1043" height="81" alt="image" src="https://github.com/user-attachments/assets/9b99c097-5fe9-44bd-a304-fb829da39f43" />

Step 2
-------
In order to build the database structure, we ran the migrations
<img width="1484" height="253" alt="image" src="https://github.com/user-attachments/assets/6c75b67f-e8a2-4f61-972a-bf04813d9d25" />

step 3 
---------
Populate the data base and shows us the items
<img width="1413" height="272" alt="image" src="https://github.com/user-attachments/assets/f3f50737-b49b-4558-a5c0-5f164eac1ea2" />

step 4
--------
Scanning the upc codes until the UI is closed

<img width="1456" height="698" alt="image" src="https://github.com/user-attachments/assets/41d5fa09-a34e-457f-b4ea-d7a1da2161fa" />



