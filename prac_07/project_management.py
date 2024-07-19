from prac_07.project import Project
import datetime

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
    user_selection(projects_information)


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
    """Select the file to save"""
    file_name = input("Please enter where you want save")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    print(file_name)
    save_data_to_file(projects_information, file_name)


def save_data_to_file(projects_information, file_name):
    """Save data from the selected file"""
    with open(file_name, "w") as on_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=on_file)
        for line in projects_information:
            print(f"{line.name}\t"
                  f"{line.start_date}\t"
                  f"{line.priority}\t"
                  f"{line.cost_estimate}\t"
                  f"{line.completion_percentage}", file=on_file)


def display_projects(projects_information):
    """Show completed and uncompleted items separately"""
    display_information = sorted(projects_information)
    print("Incomplete projects:")
    incomplete_projects = [line for line in display_information if not line.is_complete()]
    for line in incomplete_projects:
        print(f"\t{line}")
    print("Completed projects:")
    completed_projects = [line for line in display_information if line.is_complete()]
    for line in completed_projects:
        print(f"\t{line}")


def update_project(projects_information):
    """Update input data"""
    project_number = 0
    for line in projects_information:
        print(f"{project_number} {line}")
        project_number += 1
    choice = int(input("Project choice: "))
    print(projects_information[choice])
    new_percentage = int(input("New Percentage: "))
    projects_information[choice].completion_percentage = new_percentage
    new_priority = int(input("New Priority:"))
    projects_information[choice].priority = new_priority


def add_project(projects_information):
    """Add a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    day = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    percent_complete = int(input("Percent complete: "))
    projects_information.append(Project(name, day, priority, cost, percent_complete))
    display_projects(projects_information)


def filter_projects(projects_information):
    """Output the project after the selected date"""
    display_information = sorted(projects_information)
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    display_information.sort()
    for line in display_information:
        project_start_date = datetime.datetime.strptime(line.start_date, "%d/%m/%Y").date()
        if project_start_date >= date:
            print(line)


def user_selection(projects_information):
    user_input = input(f"Would you like to save to {FILENAME}?").upper()
    if user_input == "Y" or user_input == "YES":
        save_data_to_file(projects_information, FILENAME)
    print("Thank you for using custom-built project management software.")



main()
