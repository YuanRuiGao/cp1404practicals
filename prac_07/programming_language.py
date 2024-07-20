"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""
import csv


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer = pointer

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        language_pointer = "no"
        if self.pointer:
            language_pointer = ""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year},"
                f"language with {language_pointer} pointer")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def is_pointer(self):
        return self.pointer == "Yes"


def main():
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), parts[4])
        languages.append(language)
    in_file.close()
    run_tests(languages)


def run_tests(languages):
    """Determine whether there is pointer"""
    # ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, True)
    # python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    # visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    #
    # languages = [ruby, python, visual_basic]
    # print(python)

    print("The programming languages with pointer are:")
    for language in languages:
        if language.is_pointer():
            print(language.name)


if __name__ == "__main__":
    main()
