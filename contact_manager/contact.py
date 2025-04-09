class Contact:
    # TODO: Create the __init__ method with:
    # name (string), phone (string), email (string)
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    # TODO: Create the __str__ method to return something like:
    # "Jane Doe | Phone: 123-456-7890 | Email: jane@example.com"
    def __str__(self):
        return f"{self.name} | Phone: {self.phone} | Email: {self.email}"
