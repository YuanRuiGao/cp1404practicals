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
    project_information = read_file()


def read_file():
    projects_information = []
    with open(FILENAME, "r") as on_file:
        on_file.readline()
        for line in on_file:
            parts = line.strip().split('\t')
            projects_information.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    return projects_information
