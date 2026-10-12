from custom_classes import MediaItem, Book, DVD, LibraryCollection

# --- Part 2: Basic MediaItem ---
book = MediaItem("1984", "George Orwell")
movie = MediaItem("Inception", "Christopher Nolan")

print(book)
print(movie)
print()

print("Checking out the book...")
print(book.checkout())
print(book)
print()

print("Trying to check out the book again...")
print(book.checkout())
print()

print("Returning the book...")
book.return_item()
print(book)
print()

# --- Part 3: Book and DVD subclasses ---
novel = Book("To Kill a Mockingbird", "Harper Lee", page_count=281)
dvd = DVD("The Matrix", "Wachowski Sisters", duration=136)

print(novel)
print(dvd)
print()

print("Checking out the DVD...")
print(dvd.checkout())
print(dvd)
print()

print("Trying to check out the DVD again...")
print(dvd.checkout())
print()

# --- Part 4: LibraryCollection ---
library = LibraryCollection()

library.add_item(Book("The Hobbit", "J.R.R. Tolkien", page_count=310))
library.add_item(DVD("Interstellar", "Christopher Nolan", duration=169))
library.add_item(MediaItem("Python Crash Course", "Eric Matthes"))

print("=== Library Collection ===")
for item in library.items:
    print(item)
print()

# Check out 2 items
print("Checking out 'The Hobbit'...")
print(library.items[0].checkout())

print("Checking out 'Interstellar'...")
print(library.items[1].checkout())
print()

# List available
print("Currently available titles:")
print(library.list_available())