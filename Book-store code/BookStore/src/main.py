from components.bookManager import add_book, remove_book, search_by_title, search_by_author, display_books

# Main menu
def main():
    while True:
        print("\nBook Store Inventory")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search by title")
        print("4. Search by author")
        print("5. Display all books")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            description = input("Enter book description: ")
            add_book(title, author, description)
        elif choice == '2':
            title = input("Enter book title to remove: ")
            remove_book(title)
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_by_title(title)
        elif choice == '4':
            author = input("Enter author name to search: ")
            search_by_author(author)
        elif choice == '5':
            display_books()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
