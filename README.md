# GunTrack JSON to PDF

This Python script reads data from a JSON file containing information about firearms and their accessories. It creates two tables: one for the firearms and one for the accessories with serial numbers. The tables are displayed side by side on a single page in a PDF document.

## Features

- Loads firearm and accessory data from a JSON file
- Generates two tables: one for firearms and one for accessories with serial numbers
- Formats the tables with left-aligned text and increased cell spacing
- Saves the tables as a PDF document in A4 landscape format

## Requirements

- Python 3.x
- Pandas library
- Matplotlib library

## Installation

1. Make sure you have Python 3.x installed on your system. You can download it from the official Python website: [python.org](https://www.python.org/downloads/)

2. Install the required Python libraries using pip, the package installer for Python. Open a terminal or command prompt and run the following commands:

   ```shell
   pip install pandas
   pip install matplotlib
   ```

   This will install the `pandas` and `matplotlib` libraries.

## Usage

1. Ensure that you have the required Python libraries installed (`pandas` and `matplotlib`).
2. Place the JSON file containing firearm and accessory data in the same directory as the script.
3. Update the `json_file_path` variable in the script to specify the correct filename.
4. Run the script.
5. The script will generate a PDF file named `firearms_and_accessories.pdf` in the same directory.

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).