''' This module provides functions for creating a series of project folders. '''
import pathlib
import os
import time
import miller_utils


def create_folders_for_range(start_year,end_year):
   """
   Creates folders from a given range
   :param start is first year to be created
   :param end is last year to be created
   """
   for year in range(start_year, end_year + 1):
       pathlib.Path(str(year)).mkdir(exist_ok=True)


def create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False):
    """Create folders from a list of names.
    
    param: folder_list: List of folder names to be created.
    param: to_lowercase: Convert folder names to lowercase if True.
    param: remove_spaces: Remove spaces from folder names if True.
    
    returns: list of created folder paths
    """
    folders = []
    for name in folder_list:
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(" ", "")
        folder_path = pathlib.Path(name)
        folder_path.mkdir(exist_ok=True)
        folders.append(str(folder_path))
    return folders


def create_prefixed_folders(folder_list, prefix):
   #creates prefixed folders from a list of names
   #param: folder_list: names of folders
   #param: prefix: prefix added to each folder name
   cities = ['St. Louis', 'Kansas City', 'Chicago','Milwaukee']
   prefix = "Ballpark-"
   pre_res = []
   for items in cities:
      pre_res.append(prefix + items)

list = [
   'Ballpark-St. Louis', 'Ballpark-Kansas City', 'Ballpark-Chicago','Ballpark-Milwaukee'
]
for items in list:
   if not os.path.exists(items):
      os.mkdir(items)

def create_folders_periodically(delay_seconds):
   """creates folders every 1 minute
   delay_minutes: delay between creation of Files 
   """
   num_folders = 5 # number of folders to be created 
   next_file = 1   #Int to start while loop


   while next_file <= num_folders:
       pathlib.Path("folder-" + str(next_file)).mkdir(exist_ok=True)
       next_file += 1
       time.sleep(delay_seconds)

def main():
 '''main funtion for module'''
 #print byline from module imported
print(f"Byline{miller_utils.byline}")

#function to create folders for the range 2012-2018
create_folders_for_range(start_year=2012, end_year=2018)

#function that creates folders from a list
list= ["infield", "outfield", "catcher"]
create_folders_from_list(list)


folder_list = ['St. Louis', 'Kansas City', 'Chicago', 'Milwaukee']
prefix= 'Ballpark-'
create_prefixed_folders(folder_list, prefix)

#function to create files periodically
duration_secs = 15
create_folders_periodically(duration_secs)

#option to force lowercase and remove spaces
regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

# conditional script execution
if __name__ == '__main__':
  main()
