from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [
    ProgrammingLanguage("Python", "Dynamic", True, 1991),
    ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
    ProgrammingLanguage("Visual Basic", "Static", False, 1991)
]
print("The dynamically typed languages are:")

dynamically_typed_languages = [language.name for language in languages if language.typing == "Dynamic"]
for name in dynamically_typed_languages:
    print(name)
