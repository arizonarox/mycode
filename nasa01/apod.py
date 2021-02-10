#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard libray
# import webbrowser

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=ijdpvNTBcvJZpl7Hx5Q8eS1OMN1TZBKi4yHniM1Z' ## this is our api key

date_choice = input("Would you like to enter a date? yes or no: ")
if date_choice == "yes":
    date = "date="+input("Enter the date in year-mo-da format, id 2017-12-23: ")+"&"
    print(date)
else:
    date = "&"

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = requests.get(NASAAPI + date + MYKEY) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))


    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()

