# Class Link Clipboard

This program uses different modules (shelve, pyperclip, sys) to automate the copy pasting process of the class (zoom/meet) links.

Inspired by automate the boring stuff with python book, this program helps students have their class links in the clipboard so that they can just paste it instead of finding the link for the class, copying it, and then pasting it.


## NOTE

### 1. Python and the Pyperclip Module must be installed on the user's device.

1. The user must first install python from https://www.python.org/
    - Note that the shelve and re module are part of the built-in package
2. Install pyperclip using pip
    - To ensure that PIP is installed, enter `pip help` into the terminal/command prompt.
        - pip is installed if there's a message explaining how it's used
        - pip is not installed if an error message is displayed
    - Install pip by using different commands (depending on your operating system):
        - Windows: `python get-pip.py`
        - Ubuntu: `sudo apt install python3-pip`
        - MacOS: `python3 -m ensurepip --upgrade`
    - Use `pip install pyperclip` to install the pyperclip module
    - You can also use the requirements.txt file to install all modules by entering `pip3 install -r requirements.txt` on Linux

<br />

### 2. How to use it
Depending on your operating system, there are different ways on running the program.

Make sure that the python file must be installed on your device.
- Enter `git clone https://github.com/Airiseru/class-link-clipboard` on the terminal
- Use any other method such as Download ZIP, SSH, or GitHub CLI (green button that has the word 'code')

#### General Usage
`python <filename> save <keyphrase>` - Saves to clipboard the keyword and its link

`python <filename> <keyphrase>` - Loads the link to the clipboard

`python <filename> list` - Loads all keywords (in a list) to clipboard

`<filename>` is where the python script file is located
- Make sure to include the .py extension
    - e.g. D:\python\main.py (Windows)
           /home/me/Desktop/main.py (Linux)
           /Downloads/main.py (Mac)

`<keyphrase>` in this class is the name of the class
- Once the class is entered into the command line, the program searches for the word in the data file
    - If the keyphrase is in the data file, the link of the class is placed into the clipboard for easy pasting
    - If the keyphrase is not in the data file, no link will be placed in the clipboard

`save`
- Allows you to add a new class and its respective link
- When using this command, the keyphrase is the name of the class. Make sure that you have the link of the class copied.

#### Windows
On the command prompt, enter: `python <filename> <commands>`

You can also run "Run" by pressing windows+r and entering `python <filename> <commands>` there

#### Mac and Linux
Note: I'm not sure with Mac since I don't own a Mac device. If it doesn't work, google will be your friend.

On the terminal (alt+t), enter: `python3 <filename> <commands>`

<br />

### 3. How it works
1. The program will create or find the data file using the Shelve module

2. The program then takes the command of the user and checks if it's a valid input

3. If the input is valid, it will check whether it's 'save' 'list' or the name of the class
    - If it's 'save,' it will put the link of the class (which is in your clipboard, the one that is last copied) into the file with the name of the variable being the class name (keyphrase)
    - If it's 'list,' it will put into your clipboard the list of the classes that are in the data file
    - If it's name of the class (or keyphrase), it will check the data file.
        - If it's in the data file, it will put the link of the classs into the clipboard for easy pasting.
        - If it's not, nothing will happen unless the program is run in the terminal. If so, it will print a message saying that there's no link for said class.

If the program doesn't work, dm me on twitter @airiseru and I'll do my best to help :)
