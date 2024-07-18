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
    print("Welcome to Pythonic Project Management")
    project_information = read_file(None)
    user_choice = input(MENU).upper()
    while user_choice != "Q":
        if user_choice == "L":
            load_project()
        elif user_choice == "S":
            save_data_to_file(projects)
        elif user_choice == "D":
            display_projects(projects)
        elif user_choice == "F":
            filter_projects(projects)
        elif user_choice == "A":
            add_project(projects)
        elif user_choice == "U":
            update_project(projects)
        else:
            print("Invalid Menu Choice")
        user_choice = input(MENU).upper()


def read_file(file_name):
    if file_name is None:
        file_name = FILENAME
    projects_information = []
    with open(file_name, "r") as on_file:
        on_file.readline()
        for line in on_file:
            parts = line.strip().split('\t')
            projects_information.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    print(f"Loaded {len(projects_information)} projects from {file_name}")
    return projects_information


def load_project():
    file_name = input("Please enter the file name: ")
    try:
        read_file(file_name)
    except FileNotFoundError:
        print(f"Name Error, system will using the default file: {FILENAME}")
        read_file(FILENAME)


main()
