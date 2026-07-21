# Daily Wellness Tracker

## Student Information

- **Name:** Ahmet Ege Baykoz
- **Student Number:** 303068470
- **P Number:** P509320
- **Course Code:** IY499
- **Module:** Introduction to Programming

## Project Description

Daily Wellness Tracker is a menu-based Python program for recording and
reviewing daily wellness habits. Each entry contains a date, mood, water
intake, exercise time and sleep duration. The program keeps the information in
a CSV file so that saved records remain available after the program closes.

The user can view all entries, find a record by date, sort records by water
intake, filter records between two dates and display a summary with averages.
The water-intake chart is displayed on screen and saved to
`water_intake_chart.txt`.

## Questions My Project Answers

1. How much water did I drink each day?
2. How much exercise did I complete?
3. How many hours did I sleep?
4. What was my mood on a selected date?
5. What patterns appear in my wellness summary?

## Main Features

- Add one validated daily wellness entry
- Prevent duplicate entries for the same date
- Reject dates in the future
- Save and load records using `wellness_data.csv`
- Include 10 varied demonstration records for meaningful analysis
- View every valid saved entry
- Search for an entry by date
- Sort entries by water intake in either direction
- Filter entries using a start date and an end date
- Calculate average water, exercise and sleep values
- Display and save a text-based water intake chart
- Pause after each result so the output can be read
- Close safely if the user presses Ctrl+C or sends an end-of-file signal

## Programming Techniques

The project demonstrates the following programming techniques:

- Functions to divide the program into clear tasks
- Lists to hold multiple wellness records
- Dictionaries to represent individual records
- `if`, `elif` and `else` selection statements
- `while` and `for` loops
- CSV file input and output
- Input validation and exception handling
- A linear search algorithm
- A manually implemented bubble sort algorithm
- Calculations and a simple text-based data visualisation

## Searching and Sorting Algorithms

### Linear Search

The date search checks each entry in order until all matching dates have been
found. This is a linear search with a worst-case time complexity of O(n).

### Bubble Sort

The water-intake sorting feature compares neighbouring entries and swaps them
when they are in the wrong order. The algorithm repeats until no swaps are
needed. It can sort from lowest to highest or highest to lowest and has a
worst-case time complexity of O(n²).

## Error Handling and Validation

The program checks for:

- Empty mood input and mood text longer than 40 characters
- Invalid calendar dates and incorrect date formats
- Dates later than the current day
- Non-numeric input where a whole number is required
- Water values outside 0–30 glasses
- Exercise values outside 0–300 minutes
- Sleep values outside 0–24 hours
- Duplicate dates
- Missing CSV headings
- Missing or damaged values in CSV rows
- Missing files, permission problems and other file errors
- Invalid menu and sorting choices
- An end date that occurs before the start date

Invalid CSV rows are skipped with a warning so that other valid records can
still be used. A structurally invalid CSV file is not overwritten automatically.

## Data File

The CSV file uses these column headings:

```text
date,mood,water,exercise,sleep
```

Example record:

```text
2026-06-09,energetic,12,60,9
```

The submitted dataset contains 10 fictional demonstration records with varied
mood, water, exercise and sleep values. All dates are in the past. This makes
the sorting, filtering, averages and chart features easy to demonstrate.

## Chart Output

When the user chooses **Show summary**, the program displays the water-intake
chart and writes the same chart to `water_intake_chart.txt`. File permission
and operating-system errors are handled without crashing the program.

## Libraries Used

The program uses only Python standard-library modules:

- `csv` for reading and writing CSV data
- `os` for creating a reliable path to the data file
- `datetime` for validating real calendar dates

No external packages are required.

## Installation

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Keep `main.py` and `wellness_data.csv` in the same project folder.
4. Open the project folder in a terminal or code editor.

## Running the Program

On macOS or Linux, run:

```bash
python3 main.py
```

On Windows, run:

```bash
python main.py
```

## Menu Guide

1. **Add daily entry** – enter and save a new record.
2. **View all entries** – display every valid record.
3. **Search entry by date** – perform a linear date search.
4. **Sort entries by water intake** – run bubble sort in either direction.
5. **Filter entries by date range** – display records between two dates.
6. **Show summary** – display averages and save the water chart.
7. **Exit** – close the program.

## Submission Files

- `main.py` – the Python program
- `README.txt` – plain-text project documentation required by the brief
- `requirements.txt` – confirms that no external packages are needed
- `wellness_data.csv` – 10 demonstration records
- `water_intake_chart.txt` – example chart output

## GitHub Repository

https://github.com/E26180/daily-wellness-tracker

## Declaration of Own Work

I confirm that this assignment is my own work.

Where I have referred to online sources, I have provided comments detailing
the reference and included a link to the source.
