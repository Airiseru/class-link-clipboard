"""
main.py contains the script to automate the copy pasting process of the class link.

NOTE:
The class_link_file will be created/accessed on the current working directory unless specified.
If you want the class_link_file to be on a different location (e.g. D:\python on Windows), make the suggested edits:

file_path = str(Path('D:/python/classes_data'))
class_link_file = shelve.open(file_path)

"""

# Import of modules
import pyperclip
import sys
import shelve
from pathlib import Path

if __name__ == "__main__":
    # Create or Access the Shelve File
    class_link_file = shelve.open('classes_data')

    # Checks if the arguments are valid
    if len(sys.argv) < 2:
        print("Usage of file is incorrect. Please check the README.md file")
        sys.exit()

    # Adds the new link from clipboard to the data storage
    elif len(sys.argv) == 3 and sys.argv[1] == 'save':
        new_phrase = sys.argv[2]
        class_link_file[new_phrase] = pyperclip.paste()
        print("Link for " + new_phrase + " has been saved")

    # Checks for different cases depending on the keyphrase entered
    elif len(sys.argv) == 2:
        keyphrase = sys.argv[1]

        if keyphrase.lower() == 'list':
            pyperclip.copy(str(list(class_link_file.keys())))
            print("The list of classes that are in the data file is in your clipboard")
        elif keyphrase in class_link_file.keys():
            pyperclip.copy(class_link_file[keyphrase])
            print("Link for " + keyphrase + " has been copied.")
        else:
            print("Link doesn't exist for " + keyphrase)

    class_link_file.close()

