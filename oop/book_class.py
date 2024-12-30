class Book:
    """A class representing a book with magic methods for enhanced functionality."""

    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for user-friendly display."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation for recreating the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

