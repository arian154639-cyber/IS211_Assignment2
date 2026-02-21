"""There are still a couple of errors left in my code, mainly the way printed statements return to the user 
and the error log message only stating the line number instead of both the line number and the id number. 
I was a bit confused with the instructions which is why improperly formatted dates return a custom message (see line 45)."""

import argparse
import urllib.request
import logging
import datetime

logger = logging.getLogger("assignment2")
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler("error.log")
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter) 
logger.addHandler(file_handler)

def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")

def processData(data_downloader):
    result ={}
    rows = data_downloader.splitlines()
    for line_number, row in enumerate(rows[1:], start=2):
        information = row.split(',')
        try:
            id = information[0] 
            name = information[1] 
            birthday = datetime.datetime.strptime(information[2], "%d/%m/%Y")
        except ValueError:
            logger.error(f"Error processing line ({line_number})")
            birthday = "improperly_formatted_date_detected"
        result[id] = (name, birthday)
    return result

def displayPerson(id_input, personData):
    key = str(id_input)
    if key not in personData:
        raise ValueError("No person found with that id.")
    name, birthday = personData[key]
    if isinstance(birthday, datetime.datetime):
        corrected_birthday = birthday.strftime("%Y/%m/%d")
    else:
        corrected_birthday = "(improper birthday information formatting detected)"
    print(f"Person {id} is {name} with a birthday of {corrected_birthday}.")
    return True

def main(url):
    print(f"Running main with URL = {url}...")
    try:    
        csv_data = downloadData(url)
    except Exception as error_message:    
       print(f"Failed to run.")
       exit(1)   
    return csv_data
if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    csvData = main(args.url)
    personData = processData(csvData)
while True:
    id_number = input("Enter a valid id: ")
    if id_number not in personData:  
        print("Invalid id submitted.")
        exit(1)         
    displayPerson(id_number, personData)
