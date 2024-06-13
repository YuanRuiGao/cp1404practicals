"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """ Control program operation"""
    data = load_data()
    display_information(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    load_detail = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        load_detail.append(parts)
    input_file.close()
    return load_detail


def display_information(data):
    """Control elements are nested in sentences for output"""
    for i in range(len(data)):
        print(f"{data[i][0]:<6} is taught by {data[i][1]:<12} and has {data[i][2]:>3} students")


main()
