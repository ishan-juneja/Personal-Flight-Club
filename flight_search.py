import requests
from datetime import date
import os

API_KEY = os.environ["API_KEY"]
AFFIL_ID = os.environ["AFFIL_ID"]
HOME_CODE =  "SFO"

SERVER = "https://api.tequila.kiwi.com/locations/query"
SERVER2 = "https://api.tequila.kiwi.com/v2/search"



class Flight():
    def search_code(self, city):
        header = {
            "apikey": API_KEY
        }
        params = {
            "term": city,
            "location_types": "airport",
            "locale": "en-US",
            "active_only":"true",
            "limit":5
        }
        flight_details = requests.get(SERVER, params=params, headers=header)
        flight_details = flight_details.json()
        code = flight_details["locations"][0]["id"]
        return code

    def find_flight_price(self, code, stopovers=0):
        print(stopovers)
        header = {
            "apikey": API_KEY
        }
        today = date.today()

        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        month = d1[3:5]
        num = int(month) + 6
        if(num > 12):
            num = num%12
        if(num < 10):
            num = "0" + str(num)
        else:
            num = str(num)

        d2 = today.strftime(f"%d/{str(num)}/%Y")

        params = {
            "fly_from": HOME_CODE,
            "fly_to": code,
            "date_from": d1,
            "date_to": d2,
            "nights_in_dst_from" : "7",
            "nights_in_dst_to" :"28",
            "max_stopovers" : stopovers,
            "flight_type":"round",
            "curr":"USD",
            "limit":1
        }

        flight_details = requests.get(SERVER2, params=params, headers=header)
        flight_details = flight_details.json()

        try:
           return(flight_details["data"][0])
        except:
            if(stopovers < 1):
                return self.find_flight_price(code=code, stopovers=1)
            else:
                return None
        else:
            return (flight_details["data"][0])








