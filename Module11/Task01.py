class publication:
    def __init__(self, name):
        self.name = name

class magazine(publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


class book(publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")

donald_duck = magazine("Donald Duck", "Aki Hyyppä")
compartment = book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
print()
compartment.print_information()



