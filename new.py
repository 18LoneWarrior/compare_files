import json
from difflib import ndiff


def compare_json_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    comparison_data = []

    for line1, line2 in zip(lines1, lines2):
        diff = list(ndiff([line1], [line2]))
        if any(d.startswith('- ') or d.startswith('+ ') for d in diff):
            comparison_data.append({
                "file1_line": line1.strip(),
                "file2_line": line2.strip(),
                "diff": diff
            })

    return comparison_data


def write_comparison_to_file(comparison_data):
    with open("comparison_result.txt", 'w') as output_file:
        for entry in comparison_data:
            output_file.write("File 1:\n{}\n".format(entry["file1_line"]))
            output_file.write("File 2:\n{}\n".format(entry["file2_line"]))
            output_file.write("Differences:\n")
            output_file.write('\n'.join(entry["diff"]))
            output_file.write("\n\n" + "="*50 + "\n\n")


if __name__ == "__main__":
    file1_path = "bca.json"
    file2_path = "bca1.json"

    comparison_data = compare_json_files(file1_path, file2_path)
    write_comparison_to_file(comparison_data)

    print("Comparison data written to 'comparison_result.txt'")
