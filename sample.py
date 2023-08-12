import json
""" 
JSON is a file that is mainly used to store and transfer data mostly between a server and a web application. 
It is popularly used for representing structured data. Python provides a module called json which comes with Python standard built-in utility.
**load()** method can read a file that contains a JSON object.
"""
from jsondiff import diff

"""
Compares two JSON files (http://json.org) and generates a new JSON file with the result. 
Allows exclusion of some keys from the comparison, or in other way to include only some keys.
"""

# READS THE JSON FILES
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# COMPARES THE CONTENT OF JSON FILES
def compare_files(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)
    differences = diff(data1, data2)
    return differences

# WRITE THE COMPARED DATA TO A EXTERNAL JSON FILE
def write_files(file_path, data):
    with open(file_path, 'w')as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    # PATH FOR INPUT AND OUTPUT FILES
    file1 = "bca.json"
    file2 = "bca1.json"
    output = "output.json"

    differences = compare_files(file1, file2)
    write_files(output, differences)
    print(f"Data has been saved to '{output}'.")
