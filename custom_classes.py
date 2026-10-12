class MediaItem:
    """Base class representing a generic item in a library."""

    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        """Check out the item if available."""
        if self.is_available:
            self.is_available = False
            return "Successful checkout"
        else:
            return "Already out"

    def return_item(self):
        """Return the item to the library."""
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"