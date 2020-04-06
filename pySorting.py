'''
Hello! I am the creator of this program - Amigun.
I am 14 years old.
I am from Russia and I do not know much English, so I used a translator.
Sorry if you felt embarrassed due to my clumsy comments, and please if I made you smile!
Enjoy your use!
'''

# Importing libraries and modules
import os
import shutil
from pathlib import Path

# Printing a text logo
print ('╔═══╗╔╗  ╔╗   ╔═══╗╔═══╗╔═══╗╔════╗╔══╗╔═╗ ╔╗╔═══╗')
print ('║╔═╗║║╚╗╔╝║   ║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║╚╣║╝║║╚╗║║║╔═╗║')
print ('║╚═╝║╚╗╚╝╔╝   ║╚══╗║║ ║║║╚═╝║╚╝║║╚╝ ║║ ║║╚╝║║║║ ╚╝')
print ('║╔══╝ ╚╗╔╝    ╚══╗║║║ ║║║╔╗╔╝  ║║   ║║ ║║╚╗║║║║╔═╗')
print ('║║     ║║     ║╚═╝║║╚═╝║║║║╚╗  ║║  ╔╣║╗║║ ║║║║╚╩═║')
print ('╚╝     ╚╝     ╚═══╝╚═══╝╚╝╚═╝  ╚╝  ╚══╝╚╝ ╚═╝╚═══╝')

# To avoid any errors
try:
	url = input('Enter the absolute path to the folder where the files are located: ') # Getting the absolute path to the folder with unsorted files
	prefix = input('Enter the prefix name: ') # We allow the user to choose the prefix themselves
	if prefix == '': # If the user missed the opportunity to choose the prefix himself
		prefix = 'pysort-' # Then set the default prefix
	else: # Otherwise
		prefix = prefix + '-' # Adding a dash to the beginning of the user prefix
	direct = url + '/' # Adding a slash to the end of the absolute path
	files = os.listdir(direct) # The variable contains an array with the files in the directory
	for x in files: # Iterating through each element of the array
		try: # We exclude an error about files with the same names
			if x[:4] == prefix[:4]: # Checking the console to avoid transferring program files
				continue # We continue the cycle skipping the current body
			else: # Otherwise
				pass # Do nothing, continue the cycle further
			ext = direct + x # Absolute path to the file
			extension = ext.split('.')[-1] # Get the file extension
			lenDirect = len(direct) # Getting the length of the absolute path to the directory
			if extension[:lenDirect] == direct: # If this condition is met, then the file does not have an extension and is a folder
				try: # Exclude an error 'FileExistsError'
					os.mkdir(direct + prefix + 'folder') # Creating a program folder for folders
				except FileExistsError:
					pass # Do nothing, continue the cycle further
				shutil.move(ext, direct + prefix + 'folder') # Moving the folder to the folder you created earlier
			else: # Otherwise
				try: # Exclude an error 'FileExistsError'
					os.mkdir(direct + prefix + extension) # Creating a folder for other data types 
				except FileExistsError:
					pass # Do nothing, continue the cycle further
				shutil.move(ext, direct + prefix + extension) # Moving the file to the folder you created earlier
		except shutil.Error:
			print ('The destination folder already has a file named ' + x + '!') # We inform the user that a file with the same name already exists in the assigned folder
	print ('Files are sorted!') # Inform the user about the successful sorting of files
except:
	print ('#404: Unknown error. Something went wrong! The files were not sorted. T%F$W@N#S*') # We inform the user that an unknown error occurred and the files were not sorted. If you remove the glitch symbols from the incomprehensible gibberish, you will get an abbreviation that means "The files were not sorted". This is such a small Easter egg
