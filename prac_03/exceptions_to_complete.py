"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
result = 0 # If I don't add this value, the result at the bottom will be marked with a yellow wavy line
            # and prompt that the value is not found. Although this does not affect the code running.
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True # TODO: this line
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
