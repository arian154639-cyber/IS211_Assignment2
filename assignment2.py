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
        try:
            id, name, birthday = row.split(',')
            birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
            result[id] = (name, birthday)
        except Exception as error_text:
            id_number = row.split(',')[0] if ',' in row else "error2"
            logger.error(f"Error processing line ({line_number}) for id ({id_number})")
    return result

def displayPerson(id, personData):
    items = list(personData.items())
    
    if id <= 0 or id > len(items):
        print("No user found with that id.")
        return
    
    key, value = items[id-1]
    name, birthday = value
    valid_date = birthday.strftime("%Y/%m/%d") 

    print(f"Person {id} is {name} with a birthday of {valid_date}.")
    

def main(url):
    print(f"Running main with URL = {url}...")

    try:    
        csv_data = function1(url)
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
    try:
        id_input = input("Enter a valid id: ")
        id_number = int(id_input)
        displayPerson(id_number, personData)
    except:
        print("Invalid id submitted.")
        exit(1)


    import argparse

import argparse







  

