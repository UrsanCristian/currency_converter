# Currency Converter App

## Overview

The Currency Converter App is a simple Python application that allows users to convert currency values using the Open Exchange Rates API. It features a graphical user interface built with Tkinter and utilizes the ttkthemes library to apply a theme for improved aesthetics.

## Features
Convert currency from one unit to another.
User-friendly graphical interface.
Utilizes the Open Exchange Rates API for up-to-date exchange rates.

## Prerequisites
Before running the application, make sure you have the following installed:

- Python 3.x
- requests - `pip install requests`
- tkinter - built-in
- ttkthemes - `pip install ttkthemes`

## Getting Started
1. Copy the Python code from `main.py`
2. Insert the code into an IDE or a text editor.
3. Replace `"Insert Your Open Exchange Rates API Key Here"` 
with your actual Open Exchange Rates API key.
    - You can get one by registering for free on https://openexchangerates.org/
4. Save the file.
5. Run the code in the IDE.
    - If you use a text editor Open a terminal or command prompt 
in the directory where you saved the main.py file and run the app with
the following comand:
        - `python main.py`
6. After completing previous steps your Currency Converter App 
window should appear.

## Usage
- Enter the amount of currency in the "Amount of currency" field.
- Select the base currency from the "First Currency" dropdown.
- Select the target currency from the "Second Currency" dropdown.
- Click the "Convert" button to see the conversion result in the "Result" field.

### Themes

The app uses the ttkthemes library to apply themes. 
You can customize the appearance by changing the theme name 
in the ThemedTk constructor. 
Example: 
- `interface = ThemedTk(theme='adapta')`

### App Images

![Alt text](https://i.imgur.com/rul3KF7.png)
![Alt text](https://i.imgur.com/7sL6VCd.png)
