from custom_classes import MediaItem, Book, DVD

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