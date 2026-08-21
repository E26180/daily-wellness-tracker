# Daily Wellness Tracker

A menu-driven Python application for recording and reviewing daily wellness habits. The project stores entries in CSV format and demonstrates practical input validation, file handling, searching, sorting and text-based data visualisation.

## Features

- Add a validated daily entry for mood, water intake, exercise and sleep
- Prevent duplicate entries and reject future dates
- Save and load records from `wellness_data.csv`
- View, search and filter entries by date
- Sort entries by water intake in ascending or descending order
- Calculate average water, exercise and sleep values
- Display and save a text-based water-intake chart
- Handle missing files, malformed rows, permission errors and interrupted input

## Programming concepts

- Functions and modular program structure
- Lists and dictionaries
- CSV file input and output
- Input validation and exception handling
- Linear search with O(n) worst-case time complexity
- Manually implemented bubble sort with O(n²) worst-case time complexity
- Date filtering, summary calculations and simple text visualisation

## Data format

The CSV file uses the following headings:

```text
date,mood,water,exercise,sleep
```

Example:

```text
2026-06-09,energetic,12,60,9
```

The included dataset contains fictional demonstration records so the search, sorting, filtering, averages and chart features can be explored immediately.

## Requirements

- Python 3
- No third-party packages; the project uses only `csv`, `os` and `datetime` from the Python standard library

## Run locally

Clone or download the repository, then run:

```bash
python3 main.py
```

On Windows, use:

```bash
python main.py
```

## Repository contents

- `main.py` — application source code
- `wellness_data.csv` — fictional demonstration records
- `water_intake_chart.txt` — example generated chart
- `requirements.txt` — confirms that no external packages are required

## Learning outcomes

This project strengthened my understanding of structured programming, persistent data, defensive input handling, basic algorithm analysis and clear user-facing console output.
