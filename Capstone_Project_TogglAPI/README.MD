# Final Project
A bit more about the Final Project: 
This is my final project for an introductory Python class using Python 3.5.1. 

## Purpose
This project fetches workspace, project information, and client information from various Toggl APIs. It is a very basic/crude 
project management application. 

## Disclaimers 
1. APIs were not covered in class. I did my best to figure it out. 
2. There is a lot more functionality to add - for example, user information. 
3. Eventually this will become a basic project management web app.
4. In future releases, additional child classes will be created from the TogglWorkSpace class 

## Code
These files are active:


[TogglMain.py](https://github.com/jdegrave/Python/blob/master/Capstone_Project_TogglAPI/TogglMain.py)


[TogglWorkspace.py](https://github.com/jdegrave/Python/blob/master/Capstone_Project_TogglAPI/TogglWorkSpace.py)
This file is in progress:


[ToggleAPIReports.py](https://github.com/jdegrave/Python/blob/master/Capstone_Project_TogglAPI/ToggleAPIReports.py)

## Example Output
Four csv files can be created from the TogglWorkspace class:
* [Workspace Report](https://github.com/jdegrave/Python/tree/master/TogglAPI): contains essential information about the Toggl workspace
* [Projects Report](https://github.com/jdegrave/Python/tree/master/TogglAPI): contains essential information for each project in the workspace, including the total number of active projects
* [Client Report](https://github.com/jdegrave/Python/tree/master/TogglAPI): contains basic client information for each client in the workspace
* [Summary Report](https://github.com/jdegrave/Python/tree/master/TogglAPI): combines essential information from the other csv files into one csv file.
