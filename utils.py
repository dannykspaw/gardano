"""
Author(s): 
    Russell Hedrick; hedrickrussell@gmail.com
Date of Last Revision:  
    06/06/2023
Description:
    General utility functions for file handling and read/write tasks.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                  IMPORTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import csv
import datetime

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                 FUNCTIONS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def file_setup(file_name, location, headers):
    if not os.path.isfile(file_name):
        print(f"Adding new file: {file_name}\n")
        write_data(["gardano Weather Data:"], file_name)
        write_data(["Location:", location], file_name)
        write_data([""], file_name)
        write_data(headers, file_name)
    else:
        print("Log File exists. Appending to existing file.")

def write_data(data, file_name):
    with open(file_name, 'a', newline='') as file_data:
        csvWriter = csv.writer(file_data, delimiter=',')
        csvWriter.writerow(data)

def get_time():
    timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M") #:%S to add seconds
    return timestamp

