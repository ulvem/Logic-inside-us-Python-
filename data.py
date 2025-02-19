# WRITE YOUR CODE HERE
# data.py file
favourite_books = [
    {"title": "Atomic Habits by James Clear", "year_published": 2018, "is_published_after_2000": True},
    {"title": "Think Like a Tycoon by W.G. Hill", "year_published": 1980, "is_published_after_2000": False}
]

# Displaying book titles using a for loop
for book in favourite_books:
    print(book["title"])

# Extracting authors and displaying them using a for loop
for book in favourite_books:
    # Split the book string to get the author's name
    author = book["title"].split(" by ")[1]
    print(author)

# Check if the first book is newer than 2000 and display the title if True
if favourite_books[0]["is_published_after_2000"]:
    print(favourite_books[0]["title"])

# Check the age of books and display the titles with appropriate text
for book in favourite_books:
    if book["is_published_after_2000"]:
        print(f'{book["title"]} is newer than 2000.')
    else:
        print(f'{book["title"]} is older than 2000.')

# Check the age of books and display the titles with appropriate text using != operator
for book in favourite_books:
    if book["is_published_after_2000"] != False:
        print(f'{book["title"]} is newer than 2000.')
    else:
        print(f'{book["title"]} is older than 2000.')

# Check the age of books and display the titles with appropriate text using inequality operators
for book in favourite_books:
    if book["year_published"] > 2000:
        print(f'{book["title"]} is newer than 2000.')
    else:
        print(f'{book["title"]} is older than 2000.')

# Combine the results using loops and conditionals
for book in favourite_books:
    if book["year_published"] > 2000:
        print(f'{book["title"]} is newer than 2000.')
    else:
        print(f'{book["title"]} is older than 2000.')


