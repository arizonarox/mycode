#!/usr/bin/python3
"""Alta3 || Tracking ISS"""
import requests
#import urllib.request
#import json

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
        
    ## Call the webservice
    #groundctrl = urllib.request.urlopen(MAJORTOM)
    #groundctrl = requests.get(MAJORTOM)
    
    ## put fileobject into helmet
    #helmet = groundctrl.read()
    #helmetson = groundctrl.json()
    helmetson = requests.get(MAJORTOM).json()
    ## decode JSON to Python data structure
    #helmetson = json.loads(helmet.decode('utf-8'))
    
    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)
    
    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)
    
main()
