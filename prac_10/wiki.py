import wikipedia
from wikipedia import DisambiguationError, PageError

user_input = input('Enter page title: ')
while user_input != "":
    try:
        page = wikipedia.page(title=user_input)
        print(page.title)
        print(wikipedia.summary(user_input))
        print(page.url)
    except DisambiguationError as error:
        print('We need a more specific title. Try one of the following, or a new search:')
        print(error.options)
    except PageError:
        print(f'Page id "{user_input}" does not match any pages. Try another id!')
    user_input = input('Enter page title: ')
print('Thank you.')
