import requests
from data_manager import DataManager
from flight_search import Flight
from notification_class import Notification
from pprint import pprint


search_engine = Flight()
data_manager = DataManager()
notifier = Notification()


sheet_data = data_manager.get_flight_info()

for row in sheet_data:
    row_number = data_manager.row_number(row["city"])
    code = search_engine.search_code(row["city"])
    flight_price = search_engine.find_flight_price(code)
    if flight_price == None:
        continue
    else:
        flight_price = flight_price["price"]
        wanted_price = sheet_data[row_number]["lowestPrice"]
        # print(wanted_price)
        if(flight_price <= wanted_price):
            notifier.notify(search_engine.find_flight_price(code), data_manager.get_email_list())
            print(f"Found a target in {row['city']} for {flight_price}")
