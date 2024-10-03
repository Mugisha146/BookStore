import json

BOOK_FILE = 'books.json'

# Load books from file
def load_books():
    try:
        with open(BOOK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save books to file
def save_books(books):
    with open(BOOK_FILE, 'w') as file:
        json.dump(books, file, indent=4)
