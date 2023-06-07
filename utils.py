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
import csv


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                 FUNCTIONS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def write_data(data, file_name):
    with open(file_name, 'a', newline='') as file_data:
        csvWriter = csv.writer(file_data, delimiter=',')
        csvWriter.writerow(data)
