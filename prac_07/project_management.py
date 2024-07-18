from prac_07.project import Project
import datetime

# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))
FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit\n"
        ">>> ")


def main():
    """Control program execution"""
    print("Welcome to Pythonic Project Management")
    projects_information = read_file(FILENAME)
    user_choice = input(MENU).upper()
    while user_choice != "Q":
        if user_choice == "L":
            load_project()
        elif user_choice == "S":
            save_data_to_new_file(projects_information)
        elif user_choice == "D":
            display_projects(projects_information)
        elif user_choice == "F":
            filter_projects(projects_information)
        elif user_choice == "A":
            add_project(projects_information)
        elif user_choice == "U":
            update_project(projects_information)
        else:
            print("Invalid Menu Choice")
        user_choice = input(MENU).upper()
    user_input = input(f"Would you like to save to {file_name}?").upper()
    if user_input == "Y" or user_input == "YES":
        save_data_to_file(projects_information, FILENAME)
    print("Thank you for using custom-built project management software.")


def read_file(file_name):
    """Read data from the selected file"""
    projects_information = []
    with open(file_name, "r") as on_file:
        on_file.readline()
        for line in on_file:
            parts = line.strip().split('\t')
            projects_information.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    print(f"Loaded {len(projects_information)} projects from {file_name}")
    return projects_information


def load_project():
    """Select the file to read"""
    file_name = input("Please enter the file name: ")
    try:
        read_file(file_name)
    except FileNotFoundError:
        print(f"Name Error, system will using the default file: {FILENAME}")
        read_file(FILENAME)


def save_data_to_new_file(projects_information):
    file_name = input("Please enter where you want save")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    print(file_name)
    save_data_to_file(projects_information, file_name)


def save_data_to_file(projects_information, file_name):

    with open(file_name, "w") as on_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=on_file)
        for line in projects_information:
            print(f"{line.name}\t"
                  f"{line.start_date}\t"
                  f"{line.priority}\t"
                  f"{line.cost_estimate}\t"
                  f"{line.completion_percentage}", file=on_file)




main()
