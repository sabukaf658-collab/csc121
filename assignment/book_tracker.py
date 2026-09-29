def dashboard():
    print("=" * 40)
    print("📚  YOUR LIBRARY")
    print("=" * 40 + "\n")


def estimate_reading_time(pages):
    return round(pages / 40, 1)


def add_book(library):
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours = estimate_reading_time(pages)
    book = {"title": title, "author": author, "pages": pages, "hours": hours}
    library.append(book)
    print("\nBook added:")
    print(f"\n '{title}' by {author} -- approx. {hours} hours to read")


def view_books(library):
    if len(library) == 0:
        print("Your library is empty. Add a book first!")
    else:
        for i in range(len(library)):
            book = library[i]
            print(f"{i + 1}. '{book['title']}' - {book['author']} "
                  f"({book['pages']} pages - approx. "
                  f"({book['hours']} hours to read)")


def show_menu():
    print("What would you like to do?\n")
    print("  1) View books")
    print("  2) Add a book\n")
    print("  q) Quit\n")
    choice = input("> ")
    return choice.strip().lower()


def main():
    library = []
    dashboard()
    while True:
        choice = show_menu()
        if choice == "1":
            view_books(library)
        elif choice == "2":
            add_book(library)
        elif choice == "q" or choice == "quit" or choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Sorry, that option isn't available.")

        print()

if __name__ == "__main__":
    main()