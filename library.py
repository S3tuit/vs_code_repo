class Books:
    def __init__(self, isbn, state="Available") -> None:
        self.isbn = isbn
        self.state = state

class Patrons:
    def __init__(self, id) -> None:
        self.id = id

class LibraryCatalog:
    def __init__(self, catalog=[], users=[], record=[]) -> None:
        self.catalog = catalog
        self.users = users
        self.record = record

    def registration(self, id):
        for user in self.users:
            if user.id == id:
                print("User already registered")
                self.record.append("{} tried to register".format(id))
                return
        
        new_user = Patrons(id)
        self.users.append(new_user)
        self.record.append("Registered {}".format(id))
        print("User registered successfully")
                
    def cancellation(self, id):
        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                print("{} was cancellated".format(id))
                self.record.append("Cancelled {}".format(id))
                return
        print("{} is already not a patron".format(id))
        self.record.append("{} tried to cancell".format(id))

    def all_users(self):
        for user in self.users:
            print(str(user.id) + "\n")
    
    def show_record(self):
        print(self.record)

library_catalog = LibraryCatalog()

library_catalog.registration(912353)

library_catalog.cancellation(912353)

library_catalog.cancellation(912358)

library_catalog.registration(712353)

library_catalog.show_record()