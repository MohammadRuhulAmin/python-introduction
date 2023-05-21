
import re
import json
from datetime import datetime


dateString = "12-Jun-23"
def convertDate(dateString):
    dateObj = datetime.strptime(dateString, "%d-%b-%y")
    year = str(dateObj.year)
    month = str(dateObj.month)
    day = str(dateObj.day)
    return  (year + "-" + month+"-"+ day)

print(convertDate(dateString))