from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import ast
import pandas as pd
# Module for data modeling
from modules.recommendation import data_modeling

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        # Taking input (Food list, location list, maxium price and minimum price)
        food_list = str(request.form.get("foods"))
        food_list = ast.literal_eval(food_list)

        location_list = str(request.form.get("locations"))
        location_list = ast.literal_eval(location_list)

        min_price = int(request.form.get("min_price"))
        max_price = int(request.form.get("max_price"))

        # Calling data modeling function to build our recommendation dataframe
        recommendation_data = data_modeling(location_list, food_list, min_price, max_price) 

        print(recommendation_data)
        return jsonify(recommendation_data.to_json()) 

api.add_resource(Hello, '/')  
  
if __name__ == '__main__':
    app.run(debug = True) # As it is for test purpose now