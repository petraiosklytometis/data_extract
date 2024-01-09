import os
import pandas as pd

# Path to the directory containing JSON files
directory_path = "./"

# List all files in the directory with the .json extension
json_files = [file for file in os.listdir(directory_path) if file.endswith(".json")]

for json_file in json_files:
    # Construct the full path of the JSON file
    json_file_path = os.path.join(directory_path, json_file)

    # Read the JSON file into a DataFrame
    df = pd.read_json(json_file_path)

    # Path for the XLSX file
    xlsx_file_path = os.path.join("../extracted/dataset/", f"{os.path.splitext(json_file)[0]}.xlsx")

    # Save the DataFrame in XLSX format
    df.to_excel(xlsx_file_path, index=False)

    print(f"XLSX file for {json_file} saved at: {xlsx_file_path}")
