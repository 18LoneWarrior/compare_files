import json
from deepdiff import DeepDiff


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def main():
    file1_path = 'bca.json'
    file2_path = 'bca1.json'

    try:
        data1 = read_json_file(file1_path)
        data2 = read_json_file(file2_path)

        print("Data from file 1:")
        print(data1)

        print("\nData from file 2:")
        print(data2)

        differences = DeepDiff(data1, data2)
        print("\nDifferences between the two data sets:")
        print(differences)

    except FileNotFoundError:
        print("One or both of the files not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data from one or both files.")


if __name__ == "__main__":
    main()
