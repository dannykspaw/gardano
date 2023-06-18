"""
Author(s): 
    Russell Hedrick; hedrickrussell@gmail.com
    Danny Kearney-Spaw; dannykspaw@gmail.com
Date of Last Revision:  
    06/06/2023
Description:
    Main script to be executed for Garden Project.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                  IMPORTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#import climate_shit.random_function as rf
import utils

try:
    pass
except KeyboardInterrupt:
    print("\nProgram terminated as requested.")

except Exception as e:
    print("\nAn unkown error occured at {}:{}. Program terminated.".format(datetime.now().hour, datetime.now().minute))
    print(e)

utils.get_time()



