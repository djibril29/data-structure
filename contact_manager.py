# Contact book
# - doubly linked list: show contacts forward and backward
# - dictionary: find a contact by exact name
# - naive search: find a name that contains a keyword


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return self.name + " - " + self.phone


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, contact):
        new_node = Node(contact)

        # First contact: head and tail are the same node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def show_forward(self):
        if self.head is None:
            print("No contacts to display.")
            return

        current = self.head
        while current is not None:
            print(current.contact)
            current = current.next

    def show_backward(self):
        if self.tail is None:
            print("No contacts to display.")
            return

        current = self.tail
        while current is not None:
            print(current.contact)
            current = current.prev


def contains_keyword(name, keyword):
    """Naive search: try the keyword at every position in the name."""
    name_length = len(name)
    keyword_length = len(keyword)

    if keyword_length == 0 or keyword_length > name_length:
        return False

    start = 0
    while start <= name_length - keyword_length:
        position = 0
        same = True

        while position < keyword_length:
            if name[start + position] != keyword[position]:
                same = False
                break
            position = position + 1

        if same:
            return True

        start = start + 1

    return False


class ContactBook:
    def __init__(self):
        self.contact_list = DoublyLinkedList()
        # Hash table: the key is the name, the value is the contact
        self.by_name = {}

    def add_contact(self, name, phone):
        if name in self.by_name:
            print("A contact with that name already exists.")
            return

        contact = Contact(name, phone)
        self.contact_list.add(contact)
        # Same contact object in the list and in the dictionary
        self.by_name[name] = contact
        print("Contact added.")

    def search_by_keyword(self, keyword):
        current = self.contact_list.head
        found = False

        while current is not None:
            if contains_keyword(current.contact.name, keyword):
                print("Match found: " + str(current.contact))
                found = True
            current = current.next

        if not found:
            print("No match found.")

    def search_by_name(self, name):
        if name in self.by_name:
            print("Contact found: " + str(self.by_name[name]))
        else:
            print("Contact not found.")


def main():
    book = ContactBook()

    while True:
        print()
        print("1. Add Contact")
        print("2. Search by Keyword")
        print("3. Search by Exact Name")
        print("4. View All (Forward)")
        print("5. View All (Backward)")
        print("6. Exit")
        print()

        option = input("Enter option: ")

        if option == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()

            if name == "" or phone == "":
                print("Name and phone cannot be empty.")
            else:
                book.add_contact(name, phone)

        elif option == "2":
            keyword = input("Search keyword: ").strip()

            if keyword == "":
                print("Keyword cannot be empty.")
            else:
                book.search_by_keyword(keyword)

        elif option == "3":
            name = input("Name: ").strip()
            book.search_by_name(name)

        elif option == "4":
            book.contact_list.show_forward()

        elif option == "5":
            book.contact_list.show_backward()

        elif option == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


main()
