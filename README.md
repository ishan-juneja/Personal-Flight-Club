# Personal-Flight-Club
This program emails and messages you flight deals from now to 6 months in the future that are lower than your desired price threshold.

## Structure
- `data_manager.py` adds all specified flight details into a spreadsheet
- `flight_search.py` retrieves flight details from a database
- `notification_class.py` informs the user via email and message of any flight deals found
- `main.py` ties together all classes and behaves as the nucleus
## Dependencies & Configurations
1. The [Sheety API](https://sheety.co/) used for storing our desired prices and the flight data we retrieve and our email list.
   - Create 1 spreadsheet specifying cities and price points you wish to track.
   - Create 1 spreadsheet for an email list of members part of the flight club.
   - Add to `data_manager.py`
2. The [Tequila Kiwi API](https://tequila.kiwi.com/) to find all our flight info.
   - Retrieve your **API_KEY** & **AFFIL_ID** once you create your account
   - Add to `flight_search.py`
3. The [Twilio API](https://www.twilio.com/docs) to message ourselves our details of the flight.
   - Retrieve your **ACCOUNT_SID** & **AUTH_TOKEN** once you create your account
   - Add to `notification_class.py`
   - Change the phone numbers to your Twilio Assigned Number and your personal phone number within the `notification_class.py` in the `notify` method

## Demo
The spreadsheet with our desired prices and locations. The program automatically fills in the IATA codes for you!
![Screenshot 2023-07-04 at 11 43 21 PM](https://github.com/ishan-juneja/Personal-Flight-Club/assets/69048541/d35e7a4f-90d0-49ed-ad28-e9ce995d6d55)

The programs sifts through the API data to retrieve us the relevant prices we want and compares them to what we had previously specified. 
<img width="1402" alt="Screenshot 2023-07-04 at 11 46 53 PM" src="https://github.com/ishan-juneja/Personal-Flight-Club/assets/69048541/e03230d4-cdee-402b-abb9-28c61a9d4c49">

If the program has found a match, then we recieve an email and text message!
![Screenshot 2023-07-04 at 11 48 05 PM](https://github.com/ishan-juneja/Personal-Flight-Club/assets/69048541/5777d90d-5e9d-43e3-a40c-a9e9469867b3)

![IMG_8822](https://github.com/ishan-juneja/Personal-Flight-Club/assets/69048541/aa90803f-aeff-4c8b-b856-c82f5562eeea)
