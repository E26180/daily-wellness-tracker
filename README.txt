DAILY WELLNESS TRACKER
======================

STUDENT INFORMATION
-------------------
Name: Ahmet Ege Baykoz
Student Number: 303068470
P Number: P509320
Course Code: IY499
Module: Introduction to Programming

PROJECT DESCRIPTION
-------------------
Daily Wellness Tracker is a menu-based Python program for recording and
reviewing daily wellness habits. Each entry contains a date, mood, water
intake, exercise time and sleep duration. Records are stored in a CSV file so
they remain available after the program closes.

The program can display all entries, search by date, sort by water intake,
filter by a date range and calculate average water, exercise and sleep values.
It also displays a water-intake chart and saves the chart to a text file.

QUESTIONS ANSWERED BY THE PROJECT
---------------------------------
1. How much water did I drink each day?
2. How much exercise did I complete?
3. How many hours did I sleep?
4. What was my mood on a selected date?
5. What patterns appear in my wellness summary?

MAIN FEATURES
-------------
- Add and validate a daily wellness entry.
- Reject invalid dates, future dates and duplicate dates.
- Validate mood, water, exercise and sleep inputs.
- Save and load entries using wellness_data.csv.
- View all valid saved entries.
- Search entries by date using linear search.
- Sort water intake in either direction using bubble sort.
- Filter entries between a start date and an end date.
- Calculate averages and display a text-based chart.
- Save the generated chart to water_intake_chart.txt.
- Handle missing files, invalid CSV rows and file permission errors.

PROGRAMMING TECHNIQUES
----------------------
The project uses functions, lists, dictionaries, selection statements, loops,
CSV file input/output, validation, exception handling, calculations, linear
search, bubble sort and text-based data visualisation.

SEARCHING ALGORITHM
-------------------
The date-search feature checks each entry in order and returns entries whose
date matches the user's target. This is a linear search with a worst-case time
complexity of O(n).

SORTING ALGORITHM
-----------------
The water-intake feature uses a manually implemented bubble sort. It compares
neighbouring records and swaps them when they are in the wrong order. The user
can select lowest-to-highest or highest-to-lowest order. Its worst-case time
complexity is O(n^2).

ERROR HANDLING AND VALIDATION
-----------------------------
The program checks for:
- Empty mood input or mood text longer than 40 characters.
- Invalid calendar dates, incorrect formats and future dates.
- Non-numeric input where a whole number is required.
- Water values outside 0 to 30 glasses.
- Exercise values outside 0 to 300 minutes.
- Sleep values outside 0 to 24 hours.
- Duplicate dates.
- Missing CSV headings and damaged CSV rows.
- Missing files, permission errors and other file errors.
- Invalid menu and sorting choices.
- An end date occurring before the start date.

Invalid CSV rows are skipped with a warning so valid rows can still be used.
A structurally invalid CSV file is not overwritten automatically.

DATASET
-------
wellness_data.csv contains 10 fictional demonstration records. The dates are
in the past and the mood, water, exercise and sleep values are deliberately
varied. This allows searching, sorting, filtering, averages and the chart to
produce meaningful results.

CSV headings:
date,mood,water,exercise,sleep

Example record:
2026-06-09,energetic,12,60,9

CHART OUTPUT
------------
Choosing Show summary displays the chart and saves it as
water_intake_chart.txt. Each # symbol represents one glass of water.

LIBRARIES
---------
The program uses only Python standard-library modules:
- csv: reads and writes CSV data.
- os: creates reliable project file paths.
- datetime: validates real dates and rejects future dates.

No external packages are required.

INSTALLATION AND RUNNING
------------------------
1. Keep main.py and wellness_data.csv in the same folder.
2. Make sure Python 3 is installed.
3. Open a terminal in the project folder.
4. On macOS or Linux, run: python3 main.py
5. On Windows, run: python main.py

MENU GUIDE
----------
1. Add daily entry
2. View all entries
3. Search entry by date
4. Sort entries by water intake
5. Filter entries by date range
6. Show summary and save chart
7. Exit

SUBMISSION FILES
----------------
main.py
README.txt
requirements.txt
wellness_data.csv
water_intake_chart.txt

GITHUB REPOSITORY
-----------------
https://github.com/E26180/daily-wellness-tracker

DECLARATION OF OWN WORK
-----------------------
I confirm that this assignment is my own work.

Where I have referred to online sources, I have provided comments detailing
the reference and included a link to the source.
