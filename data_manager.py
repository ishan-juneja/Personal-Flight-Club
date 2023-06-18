import json

import requests
from pprint import pprint

SPREADSHEET_URL = "https://api.sheety.co/b740399a8f58c5c9d016c566fb68be9a/flightDeals/prices/"
SPREADSHEET_URL_2 = "https://api.sheety.co/b740399a8f58c5c9d016c566fb68be9a/flightDeals/users"

#RETRIEVING ALL THE INFORMATION ABOUT THE FLIGHTS
sheet_data = requests.get(SPREADSHEET_URL)
print(sheet_data.status_code)
sheet_data = sheet_data.json()
# sheet_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}

#RETRIEVING ALL THE INFORMATION ABOUT THE EMAILS
email_data = requests.get(SPREADSHEET_URL_2)
email_data = email_data.json()
print(email_data)
email_list = []
for row in email_data["users"]:
    email_list.append(row["email"])


class DataManager:
    def populate_row(self, row_number, code):
        row_data = sheet_data['prices'][row_number]
        row_data = {
            'price':{
                "city":row_data['city'],
                "iataCode":code,
                "lowestPrice":row_data['lowestPrice'],
                "id": row_number+2
            }
        }
        temporary_URL = f"{SPREADSHEET_URL}/{row_number+2}"
        data = requests.put(temporary_URL, json=row_data)

    def flight_code(self, city):
        for row in sheet_data:
            if (row['city'] == city):
                return row['iataCode']
        return "NA"

    def row_number(self, city):
        counter = 0
        city = str(city)
        for row in sheet_data['prices']:
            if (row['city'].lower() == city.lower()):
                return counter
            counter += 1
        return -1

    def get_flight_info(self):
        return sheet_data["prices"]

    def get_email_list(self):
        return email_list





