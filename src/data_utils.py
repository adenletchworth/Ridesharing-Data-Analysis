import re

def standardize_date(text):
    date_patterns = [
        r'^(\d{1,2})/(\d{1,2})/(\d{4})$',  
        r'^(\d{1,2})-(\d{1,2})-(\d{4})$', 
    ]

    for pattern in date_patterns:
        match = re.match(pattern, text)
        if match:
            month = match.group(1).zfill(2)  
            day = match.group(2).zfill(2)  
            year = match.group(3)
            return f"{month}/{day}/{year}"
    
    return text 

# Helper function for finding date pattern in raw data strings
def find_date(text):
    date_pattern = r'^(\d{1,2}/\d{1,2}/\d{4})'  
    match = re.search(date_pattern, text)
    if match:
        return match.group(1)
    else:
        return None 

import datetime


def get_day_of_week_from_string(date_string):

    month, day, year = map(int, date_string.split('/'))


    date_obj = datetime.datetime(year, month, day)

    day_of_week = date_obj.strftime('%A')  

    return day_of_week
