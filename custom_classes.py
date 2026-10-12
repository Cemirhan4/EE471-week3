class MediaItem:
    """
    Represents a generic item in a library collection.

    This is the base class for all media types. It provides
    core checkout and return functionality shared by all items.
    """

    def __init__(self, title, author, is_available=True):
        """
        Initialize a MediaItem.

        Args:
            title (str): The title of the media item.
            author (str): The author or creator of the item.
            is_available (bool): Whether the item is available for checkout. Defaults to True.
        """
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        """
        Check out the item if it is currently available.

        Returns:
            str: 'Successful checkout' if available, 'Already out' if not.
        """
        if self.is_available:
            self.is_available = False
            return "Successful checkout"
        else:
            return "Already out"

    def return_item(self):
        """Mark the item as available again after being returned."""
        self.is_available = True

    def __str__(self):
        """Return a human-readable string representation of the item."""
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"


class Book(MediaItem):
    """
    Represents a book in the library.

    Extends MediaItem with a page count attribute and
    includes page count in its string representation.
    """

    def __init__(self, title, author, page_count, is_available=True):
        """
        Initialize a Book.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): Total number of pages.
            is_available (bool): Availability status. Defaults to True.
        """
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation that includes the page count."""
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}] - {self.page_count} pages"


class DVD(MediaItem):
    """
    Represents a DVD in the library.

    Extends MediaItem with a duration attribute. DVDs are fragile,
    so a care reminder is printed on every successful checkout.
    """

    def __init__(self, title, author, duration, is_available=True):
        """
        Initialize a DVD.

        Args:
            title (str): The title of the DVD.
            author (str): The director or creator.
            duration (int): Duration of the DVD in minutes.
            is_available (bool): Availability status. Defaults to True.
        """
        super().__init__(title, author, is_available)
        self.duration = duration

    def checkout(self):
        """
        Check out the DVD, reminding the borrower to handle it with care.

        Uses super().checkout() to preserve the base checkout logic,
        then adds a fragility warning if the checkout succeeds.

        Returns:
            str: 'Successful checkout' if available, 'Already out' if not.
        """
        result = super().checkout()
        # DVDs can be scratched easily — warn the user only on success
        if result == "Successful checkout":
            print("Handle with care: Do not scratch the disc.")
        return result


class LibraryCollection:
    """
    A container for managing a collection of MediaItems.

    Supports adding items and querying which titles are currently available.
    """

    def __init__(self):
        """Initialize the collection with an empty list."""
        self.items = []

    def add_item(self, item):
        """
        Add a MediaItem (or any subclass) to the collection.

        Args:
            item (MediaItem): The item to add.
        """
        self.items.append(item)

    def list_available(self):
        """
        Return the titles of all currently available items.

        Returns:
            list[str]: A list of available item titles.
        """
        return [item.title for item in self.items if item.is_available]