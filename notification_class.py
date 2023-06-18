import requests
from twilio.rest import Client
import smtplib
import os

# Your Account Sid and Auth Token from twilio.com / console
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]

client = Client(account_sid, auth_token)




class Notification:
    def notify(self, flight_details, email_list):
        print(flight_details)
        departure_date = flight_details["route"][0]["local_departure"][0:10]
        arrival_date = flight_details["route"][-1]['local_arrival'][0:10]
        text = f"Found a flight from {flight_details['cityFrom']} to {flight_details['cityTo']} for ${flight_details['price']} from {departure_date} to {arrival_date}"
        if(len(flight_details["route"]) > 2):
            text = text + f". This flight includes 1 stopover at {flight_details['route'][0]['cityTo']}."

        #Text Message
        message = client.messages \
            .create(
            body=text,
            from_='+18777647140',
            to=os.environ["MY_NUMBER"]
        )

        #Emailing
        sender = "ishanj101ishanj101@gmail.com"
        password = os.environ["EMAIL_PASSWORD"]
        receivers = email_list

        message = f"""Subject: Flight Deal Found!
        \n\n
        To our flight club member,\n
        {text}\n
        From,
        Ishan's Flight Club
        """


        smtpObj = smtplib.SMTP("smtp.gmail.com", port=587)
        smtpObj.starttls()
        smtpObj.login(user=sender,password=password)
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.quit()
        print("Successfully sent email")