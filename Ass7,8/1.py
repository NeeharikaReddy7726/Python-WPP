class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print(f"Node with data {key} not found.")
            return

        if not prev:
            self.head = current.next
        else:
            prev.next = current.next

        print(f"Node with data {key} deleted.")

# Taking input from the user
linked_list = LinkedList()
while True:
    action = input("Choose an action (insert, delete, display, exit): ").strip().lower()
    if action == "insert":
        data = input("Enter the data to insert: ").strip()
        linked_list.insert(data)
    elif action == "delete":
        data = input("Enter the data to delete: ").strip()
        linked_list.delete(data)
    elif action == "display":
        linked_list.display()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please choose 'insert', 'delete', 'display', or 'exit'.")
