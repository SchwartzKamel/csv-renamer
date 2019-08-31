#! python3
# fileRename.py - Adds a date prefix in mmddyy format to files in a specified directory
import glob, os

# path for the script to work in, just change it to suit your needs
os.chdir('C:\\Users\\tweber\\Downloads\\PowerBI')

# gets the date to add in front of the filename
print('Enter the date you wish in mmddyy format')
date = input()

# adds the date prefix
for f in glob.glob('*.csv'):
	new_filename = f.replace(" ","_")
	new_filename = date + new_filename
	os.rename(f,new_filename)