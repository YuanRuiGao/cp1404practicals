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
    length_of_class_name = 0
    length_of_lord_name = 0
    length_of_student_number = 0
    for x in data:
        if len(x[0]) > length_of_class_name:
            length_of_class_name = len(x[0])
        if len(x[1]) > length_of_lord_name:
            length_of_lord_name = len(x[1])
        if len(str(x[2])) > length_of_student_number:
            length_of_student_number = len(str(x[2]))

    for y in range(len(data)):
        print(f"{data[y][0]:<{length_of_class_name}} is taught by {data[y][1]:<{length_of_lord_name}} and has "
              f"{data[y][2]:>{length_of_student_number}} students")


main()
