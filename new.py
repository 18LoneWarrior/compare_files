import json
from difflib import ndiff


def compare_json_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    comparison_data = []

    for line_number, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
        diff = list(ndiff([line1], [line2]))
        if any(d.startswith('- ') or d.startswith('+ ') for d in diff):
            comparison_data.append({
                "line_number": line_number,
                "file1_line": line1.strip(),
                "file2_line": line2.strip(),
                "diff": diff
            })

    return comparison_data


if __name__ == "__main__":
    file1_path = "bca.json"
    file2_path = "bca1.json"

    comparison_data = compare_json_files(file1_path, file2_path)

    with open("comparison_result.json", 'w') as output_file:
        json.dump(comparison_data, output_file, indent=4)

    print("Comparison data written to 'comparison_result.json'")
