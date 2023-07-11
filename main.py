import argparse

print("Welcome to Apple 2 IDE\n\n")
parser = argparse.ArgumentParser(description="Python file editor")

parser.add_argument("--file-path", type=str, help="Path of the file to edit")
args = parser.parse_args()


if args.file_path == None:
    file_path = input("Please enter the path of the file you want to edit: ")
else:
    file_path = args.file_path

while True:
    with open(file_path, "r") as file:
        print(file.read())

    line_number_input = input("Enter the line number to write: ")

    try:
        line_number = int(line_number_input)
        new_content = input("Enter the new content: ")

        if line_number >= 1:
            with open(file_path, "r") as file:
                lines = file.readlines()

            if line_number <= len(lines):
                lines[line_number - 1] = new_content + '\n'
            else:
                lines.extend(['\n'] * (line_number - len(lines) - 1))
                lines.append(new_content + '\n')

            with open(file_path, "w") as file:
                file.writelines(lines)
        else:
            print("Line number should be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid line number.")
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error occurred while reading/writing the file.")
