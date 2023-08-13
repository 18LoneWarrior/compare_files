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
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    file1_path = "bca.json"  
    file2_path = "bca1.json" 

    json1 = read_json(file1_path)
    json2 = read_json(file2_path)

    differences = diff(json1, json2)

    output_data = {
        "original_data": json1,
        "differences": differences
    }

    output_file_path = "output.json"

    with open(output_file_path, 'w') as output_file:
        json.dump(output_data, output_file, indent=4)

    if differences:
        print(f"Differences saved to {output_file_path}.")
    else:
        print("The JSON files are identical.")
