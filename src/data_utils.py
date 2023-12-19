import re

def find_date(text):
    date_pattern = r'^(\d{1,2}/\d{1,2}/\d{4})'  
    match = re.search(date_pattern, text)
    if match:
        return match.group(1)  
    else:
        return None 