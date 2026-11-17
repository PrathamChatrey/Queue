queue = []

# Push operation (Enqueue)
def push():
    n = int(input("Enter element: "))
    queue.append(n)
    print(n, "inserted into queue")

# Pop operation (Dequeue)
def pop():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        x = queue.pop(0)
        print("Deleted element:", x)

# Display operation
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements:", queue)

# Main program
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Program ended")
        break
    else:
        print("Invalid choice")
