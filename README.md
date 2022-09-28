# Data_Engineering 

* This project involved scraping data (Menu, Location and Price) from 3 sources and pushing them into database
* Bulding data model for recommendation (Consideringlocation, menu and price options)
* Building Rest API for recommendation (Flask API)

1. [Madchef](https://madchef.com.bd/)
2. [Pizza Hut](https://www.pizzahutbd.com/)
3. [Chillox](https://www.facebook.com/chillox.burgers/)

## The Process Diagram: 

![Process Diagram](https://github.com/espSiyam/Data_Engineering/blob/main/data/Data%20%20Engineering.jpg)

### To use this script, db credential will be required. The format is:
**mysql+pymysql://{user}:{password}@{ip}/{database_name}**

### Input example for REST API ("key" : "value"): 
foods : ['Signature Beef', 'Spicy Chicken (GS)', BeefiChicken Pastrami; Poached Egg', 'Supreme.', 'Veggie Lovers', 'Bbq Temptation .', 'Lemon Iced Tea']
locations : ['Mirpur', 'Cox Bazar', 'Dhanmondi', 'Gulshan', 'Bhatara', 'Khilgaon', 'RM Center', 'Jamuna', 'Mohammadpur', 'Mirpur TFC', 'Adabor']
min_price: 100
max_price: 320
