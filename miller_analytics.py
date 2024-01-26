'''Module 3 
Acquiring data from the web and writing data
from different file types. Then processing data to 
generate output
'''

#standard library imports
import csv
import pathlib
from pathlib import Path
from io import StringIO
import io

#External library imports (require a virtual environment)
import requests
import pandas as pd

#Import local modules
import miller_projsetup
import miller_utils

#acquiring text data
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text) #call function saves content
    else:
        print(f"failed to fetch data: {response.status_code}")
#call and write text file, creating data.txt
def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) #join paths
    #create folder if one doesn't already exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open('w', encoding='utf-8') as file:
        file.write(data)
#process text data
def process_txt_file(folder_name, input_filename, output_filename):
    #fetch data
    url = 'https://www.gutenberg.org/ebooks/1112.txt.utf-8'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        write_txt_file(folder_name, input_filename, data)

        write_txt_requests_file(folder_name, output_filename, input_filename)

    else: 
        print(f"Failed to fetch data: {response.status_code}")
#Function generates stats from text data
def write_txt_requests_file(txt_folder_name, data_txt_file, input_filename):

    file_path  = Path(txt_folder_name).joinpath(input_filename)
    file_path_re = Path(txt_folder_name).joinpath(data_txt_file)

    with file_path.open('r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    with file_path_re.open('w', encoding='utf-8') as file:
        file.write(f"\nWord count of file: {word_count}\n")
        print(f"Word count in (dat_txt_file)")

#exception handling
def fetch_txt_data(folder_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        #will raise an HTTPError
        #if HTTP request returns unsuccessful

        #response content is text data
        file_path = Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data save to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

#acquiring excel data
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else: 
        print(f"Failed to fetch Excel data: {response.status_code}")
#write excel data
def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)
    #create folder if one doesn't already exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data save to {file_path}")

#process excel data
def process_excel_file(excel_folder_name, input_filename, output_filename):
    #fetch excel data
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    response = requests.get(excel_url)

    if response.status_code == 200:
        data = response.content
        write_excel_file(excel_folder_name, input_filename, data)
        #panda is used to read excel data from binary
        excel_data = pd.read_excel(io.BytesIO(data), sheet_name='Sheet1')
        #creates csv data from excel data
        processed_data = excel_data.to_csv(index=False)
        #write data to csv file
        csv_output_filename = output_filename.replace('.xls', '.csv')
        write_csv_file(excel_folder_name, csv_output_filename, processed_data)

    else: 
        print(f"Failed to fetch data: {response.status_code}")
    

#acquiring csv data
def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")
#write csv data
def write_csv_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)
    #create folder if one doesnt exist
    file_path.parent.mkdir(parents=True, exist_ok=True)
    #parse the data
    csv_data = parse_csv_data(data)

    with file_path.open('w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_data)
        print(f"CSV data saved to {file_path}")

def parse_csv_data(csv_text):
    csv_data = []
    csv_reader = csv.reader(StringIO(csv_text))
    for row in csv_reader:
        csv_data.append(row)
    return csv_data
#process CSV data
def process_csv_file(csv_folder_name, input_filename, output_filename):

    csv_url = 'https://raw.githubusercontent.com/balsama/us_counties_data/main/data/counties.csv'
    response = requests.get(csv_url)
    
    if response.status_code == 200:
        data = response.text
        write_csv_file(csv_folder_name, input_filename, data)

        create_data_csv(csv_folder_name, output_filename, input_filename)
    else:
        print(f"Failed to fetch data: {response.status_code}")
#analyze csv file data
def create_data_csv(csv_folder_name, data_csv_file, input_filename): 

    file_path = Path(csv_folder_name).joinpath(input_filename)
    file_path_re = Path(csv_folder_name).joinpath(data_csv_file)

    tuple_data = ()
    tuple_list = list(tuple_data)
    #variables that are counted
    Missouri_count = 0
    Alabama_count = 0
    Washington_count =0

    with file_path.open('r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i in reader:
            tuple_list.append(i)
            tuple_data = tuple(tuple_list)

    for county_data in tuple_data:

        County, State, FIPS_Code, Population, Area, Density = county_data
        if State == 'Missouri':
            Missouri_count += 1
        elif State == 'Alabama':
            Alabama_count += 1
        elif State == 'Washington':
            Washington_count += 1

    with file_path_re.open('w', encoding='utf-8') as file:
        file.write(f"\nNumber of counties in Missouri: {Missouri_count}")
        file.write(f"\nNumber of counties in Alabame: {Alabama_count}")
        file.write(f"\nNumber of counties in Washington: {Washington_count}")
        file.write(f"\nDisplay tuple in columns:")
        for ii in tuple_data:
            file.write(f"{ii}\n")
        
        print(f"Displayed csv data in tuple {data_csv_file}")
#acquire json data
def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch json data:{response.status_code}")
#write json data
def write_json_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename)


    with file_path.open('wb') as file:
        file.write(data)
        print(f"Binary data saved to {file_path}")
#preocess the data
def process_json_file(json_folder_name, input_filename, output_filename):

    json_url = 'https://www.boredapi.com/api/activity'
    response = requests.get(json_url)

    if response.status_code == 200:
        data = response.content
        write_json_file(json_folder_name, input_filename, data)
        write_json_file(json_folder_name, output_filename, data)

    else:
        print(f"Failed to fetch data: {response.status_code}")



def main():
    '''Main function to demonstrate module capabilities'''

print(f"Name: {'datafun-03-analytics-Graham Miller'}")

txt_url = 'https://www.gutenberg.org/ebooks/1112.txt.utf-8'

excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'

csv_url = 'https://raw.githubusercontent.com/balsama/us_counties_data/main/data/counties.csv'

json_url = 'https://www.boredapi.com/api/activity'

txt_folder_name = 'data-txt'
excel_folder_name = 'data-excel'
csv_folder_name = 'data-csv'
json_folder_name = 'data-json'

txt_filename = 'data.txt'
excel_filename = 'data.xls'
csv_filename = 'data.csv'
json_filename = 'data.json' 

fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)
fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
fetch_and_write_json_data(json_folder_name, json_filename,json_url)

process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
process_json_file(json_folder_name,'data.json', 'results_json.txt')


if __name__ == "__main__":
    main()


