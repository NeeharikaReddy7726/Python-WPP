class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued: {data}")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty, cannot dequeue.")
            return None
        data = self.queue.pop(0)
        print(f"Dequeued: {data}")
        return data

    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Queue:", self.queue)


# Taking input from the user
queue = Queue()
while True:
    action = input("Choose an action (enqueue, dequeue, display, exit): ").strip().lower()
    if action == "enqueue":
        data = input("Enter the data to enqueue: ").strip()
        queue.enqueue(data)
    elif action == "dequeue":
        queue.dequeue()
    elif action == "display":
        queue.display()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please choose 'enqueue', 'dequeue', 'display', or 'exit'.")
