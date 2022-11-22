# cooling-and-heating-system

## Introduction

#### About the project 

<p>
This is a Cooling and Heating Control System project where the user should be able to control various aspects of the system to there desired temperature. We used Tkinter to create an interface for the user to interact with. The project will get the temperature outside of the building by scraping from the internet the temperature whenever the interface is running. There is 6 zones in our project and you can specify for each zone individually. The user is allowed to get and set the desired temperature they would like each zone in the building to to be aswell as a timer to allow the user to specify the length of time they would like this function to be run. Depending on the desired temperature the Heating or Cooling Fan will turn on and once the temperature required is met the system will maintain the temperature until it is changed or the timer runs out. The Heating and Cooling Fan can both be toggled/overridden manually by the user if desired.  We added a how to use section in the interface to allow a new user to understand the interface quickly. We used Python to implement the project as it was the language the team feeled most comfortable with.
</p>

#### Implementation

##### Main Objectives

* Get the temperature
* Set the temperature
* Set Timer
* Set Zone
* Toggle Fan
* Toggle Heating
* Implement tkinter Interface
* Unit Testing
* Create system to regulate the heat and maintain it at the designated temperature

##### Files

* adminControlPanel.py: Implements all the functions required for the admin interface.
* adminInterface.py: An admin interface to allow personnel with admin authentication to certain aspects of the file.
* interface.py: **The user should run the file from here**. Implements the user inteface.
* TempSensor.py: Uses a web crawler to initalize the temperature and get the current temperature outside the building.
* test_adminControlPanel.py: Creates a set of unit tests for the admin control panel to verify there is no errors in the code.
* test_zoneControlPanel.py: Creates a set of unit tests for the zone control panel to verify there is no errors in the code.
* test.py: prints the temp in the console to ensure the code is running correctly.
* zoneControlPanel.py: Implements the functions required to set changes to each zone individually.

## Installation

#### Requirements

* [Python 3.6](https://www.python.org/downloads/release/python-360/) installed.
* A code editor. Recommended [VS Code](https://code.visualstudio.com/download).
* The Beautiful Soup python libray [bs4](https://pypi.org/project/bs4/)

#### Instructions

* Download the zip file containing the project.
* Extract all from the zip and save the folder to your computer.
* Open the folder in a code editor.
* pip install [bs4](https://pypi.org/project/bs4/) in the terminal(bs4 is required for the function to run).
* To Run the function open the **interface.py** file and run the code.
* To Run the admin version of the function open the **adminInterface.py** file and run code
* Follow the instructions from the **how to use** section of the tkinter window.

* To run the unit tests open a terminal in the same location as where the unit test files are located and use the command "python3 -m unittest test_adminControlPanel.py" or "python3 -m unittest test_zoneControlPanel.py"



### Contributors
- Sean Malone
- Joseph O'Donovan
- Mark Marron
- Eoin O'Sullivan

ADDING MORE THIS COMMIT IS JUST TO SAVE PROGRESS
