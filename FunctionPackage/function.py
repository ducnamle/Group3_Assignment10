# Name: Assignment 10 Group 3
# email: le2dc@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: November 9 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: retrieves information from a public APIs database, parsing the data into a dictionary. It then prints out the name and description of the first API entry
# Citations: n/a
# Anything else that's relevant: n/a

#function

import json
import requests

def get_api_data(url):

    response = requests.get(url)
    json_string = response.content
    parsed_json = json.loads(json_string)

    return parsed_json['entries'] #Return the list of API entries