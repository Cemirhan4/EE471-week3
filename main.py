from custom_classes import MediaItem

# Create two MediaItem instances
book = MediaItem("1984", "George Orwell")
movie = MediaItem("Inception", "Christopher Nolan")

# Display initial status
print(book)
print(movie)

print()

# Simulate checking out the book
print("Checking out the book...")
print(book.checkout())
print(book)

print()

# Try to check out the book again
print("Trying to check out the book again...")
print(book.checkout())

print()

# Return the book
print("Returning the book...")
book.return_item()
print(book)