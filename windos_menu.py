import webbrowser
import os
import pyttsx3
import twitter
import wikipediaapi
import subprocess as sp
import openai
# import medium
import smtplib
from geopy.geocoders import Nominatim
import music
import email_er
from twilio.rest import Client
import pygame
import sys
import vlc
import time

def windows_menu():
    api_set = [False]
    
    def notepad():
        os.system("notepad.exe")

    def chrome():
        sp.getoutput(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    def whatsapp():
        webbrowser.open("https://web.whatsapp.com/")

    def email():
        email_er.send_email()

    def sms():
    # Get user input
        account_sid = input("Enter your Twilio Account SID: ")
        auth_token = input("Enter your Twilio Auth Token: ")
        from_number = input("Enter your Twilio phone number (in E.164 format, e.g., +1234567890): ")
        to_number = input("Enter the recipient's phone number (in E.164 format): ")
        message = input("Enter the SMS message: ")

        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        try:
            # Send the SMS
            message = client.messages.create(
                body=message,
                from_=from_number,
                to=to_number
            )
            print(f"SMS sent successfully. SID: {message.sid}")
        except Exception as e:
            print(f"Error: {e}")


    def chatgpt():
        if api_set[0] == False:
            openai.api_key = input("Enter the API key for this Session")
            api_set[0] = True
        user_input = input("How may I help you ? ")
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # Use the appropriate model
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
        ])
        
        assistant_response = response['choices'][0]['message']['content']
        print(assistant_response)

    def geolocation(location):
        geolocator = Nominatim(user_agent="geo_locator")
        location = geolocator.geocode(location)
        if location:
            latitude, longitude = location.latitude, location.longitude
            if latitude is not None and longitude is not None:
                url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
                webbrowser.open_new_tab(url)
            else:
                print("Coordinates not found for the given location.")
        else:
            return None

    def get_twitter_trends():
        # Your Twitter trending topics logic here
        api_key = 'YOUR_TWITTER_API_KEY'
        api_secret_key = 'YOUR_TWITTER_API_SECRET_KEY'
        access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
        access_token_secret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'

        auth = twitter.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)

        api = twitter.API(auth)

        trends = api.trends_place(id=1)  # Assuming worldwide trends
        for trend in trends[0]['trends']:
            print(trend['name'])

    def get_hashtag_posts():
        # Your hashtag posts retrieval logic here
        pass

    def get_wikipedia_data():
        # Your Wikipedia data retrieval logic here
        wiki_wiki = wikipediaapi.Wikipedia('Your-App-Name/1.0')
        page_py = wiki_wiki.page(input("Enter the topic: "))
        print("Page text: %s" % page_py.text[:])
        print("\n\n Press Enter to continue...")
        input()

    def audio_player():
        music.musica()

    def video_player(vpth=r"C:\Users\Asus\Desktop\workspace\VD Recs\bandicam 2023-06-03 11-05-18-508.mp4"):
        media_player = vlc.MediaPlayer(vpth)
 
# start playing video
        media_player.play()
 
# wait so the video can be played for 5 seconds
# irrespective for length of video
        time.sleep(5)
       
    

    def control_speaker_sound():
        # Your speaker sound control logic here
        pass

    while True:
        print("\nMenu:")
        print("1. Notepad")
        print("2. Chrome")
        print("3. WhatsApp")
        print("4. Email")
        print("5. SMS")
        print("6. ChatGPT")
        print("7. Geolocation")
        print("8. Twitter Trends")
        print("9. Hashtag Posts")
        print("10. Wikipedia Data")
        print("11. Audio Player")
        print("12. Video Player")
        print("13. Speaker Sound Control")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            notepad()
        elif choice == '2':
            chrome()
        elif choice == '3':
            whatsapp()
        elif choice == '4':
            email()
        elif choice == '5':
            sms()
        elif choice == '6':
            chatgpt()
        elif choice == '7':
            geolocation(input("Enter location: "))
        elif choice == '8':
            get_twitter_trends()
        elif choice == '9':
            get_hashtag_posts()
        elif choice == '10':
            get_wikipedia_data()
        elif choice == '11':
            audio_player()
        elif choice == '12':
            video_player()
        elif choice == '13':
            control_speaker_sound()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")