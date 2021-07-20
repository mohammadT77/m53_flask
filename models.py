class User:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str

    def __init__(self, id: int, fname: str, lname: str, username: str = None, email: str = None) -> None:
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.username = username
        self.email = email

    def __str__(self):
        return f"<User #{self.id}: {self.first_name} {self.last_name}"

    def json(self):
        return vars(self)