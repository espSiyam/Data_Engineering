from sqlalchemy import create_engine
import pandas as pd
from modules.load_table import table
import json

def data_modeling(location_list, food_list, min_price, max_price):
    
    # Load tables
    database_credential = json.load(open('credentials.json'))
    connection = create_engine(database_credential['db'])
    location = table(connection, 'location_data')
    madchef = table(connection, 'madchef')
    pizzahut = table(connection, 'pizzahut')
    chillox = table(connection, 'chillox')

    restaurants = chillox.append(pizzahut).append(madchef).reset_index(drop=True)
    restaurants["price"] = pd.to_numeric(restaurants["price"])

    # Filtering data by preferrer location
    location_filter = location[location['location'].isin(location_list)]
    
    # Filtering data by preffered food
    food_filter = restaurants[restaurants['name'].isin(food_list)]
    
    # Filtering data within the price range
    price_filter = food_filter[(food_filter['price']>=min_price) &  (food_filter['price']<=max_price)].reset_index(drop=True)

    # Filtering restaurants from perffered locations and providing the best result
    location_filtered_list = list(set(location_filter['restaurant']))
    final_data = price_filter[price_filter['restaurant'].isin(location_filtered_list)]
    
    return final_data