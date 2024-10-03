from utils.fileManager import load_books, save_books

# Add a new book
def add_book(title, author, description):
    books = load_books()
    book = {'title': title, 'author': author, 'description': description}
    books.append(book)
    save_books(books)
    print(f"Book '{title}' by {author} added.")


# Remove a book by title
def remove_book(title):
    books = load_books()
    books = [book for book in books if book['title'].lower() != title.lower()]
    save_books(books)
    print(f"Book '{title}' removed.")


# Search for a book by title
def search_by_title(title):
    books = load_books()
    found_books = [book for book in books if title.lower() in book['title'].lower()]
    if found_books:
        for book in found_books:
            print(f"Found: {book['title']} by {book['author']}\nDescription: {book['description']}")
    else:
        print(f"No books found with title containing '{title}'.")


# Search for a book by author
def search_by_author(author):
    books = load_books()
    found_books = [book for book in books if author.lower() in book['author'].lower()]
    if found_books:
        for book in found_books:
            print(f"Found: {book['title']} by {book['author']}\nDescription: {book['description']}")
    else:
        print(f"No books found by author '{author}'.")


# Display all books
def display_books():
    books = load_books()
    if books:
        for book in books:
            print(f"{book['title']} by {book['author']}\nDescription: {book['description']}\n")
    else:
        print("No books in inventory.")
