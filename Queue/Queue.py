class Node:
    def __init__(self, value: int) -> None:
        """
        Initializes a new node with the given value.

        Args:
            value (int): The value of the node.
        """
        self.data: int = value
        self.next: Node | None = None  # Pointer to the next node


class Queue:
    def __init__(self) -> None:
        """
        Initializes an empty queue.
        """
        self.front: Node | None = None  # Pointer to the front node
        self.rear: Node | None = None  # Pointer to the rear node
        self.count: int = 0  # Number of elements in the queue

    def enqueue(self, data: int) -> None:
        """
        Adds an element to the rear of the queue.

        Args:
            data (int): The data to be added to the queue.
        """
        new_node = Node(data)
        if self.front is None:  # If the queue is empty
            self.front = new_node
            self.rear = new_node
        else:  # Append the new node at the rear
            assert self.rear is not None  # Ensure rear is not None
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1

    def dequeue(self) -> None:
        """
        Removes an element from the front of the queue.

        Returns:
            None
        """
        if self.front is None:  # If the queue is empty
            print("Queue is empty:)")
            return
        self.front = self.front.next  # Move the front pointer to the next node
        self.count -= 1

    def size(self) -> None:
        """
        Prints the size (number of elements) in the queue.

        Returns:
            None
        """
        if self.front is None:  # If the queue is empty
            print("Queue is empty:)")
            return
        print(f"\nQueue size: {self.count}")

    def front_item(self) -> None:
        """
        Prints the front item of the queue.

        Returns:
            None
        """
        if self.front is None:  # If the queue is empty
            print("Queue is empty:)")
            return
        print(f"Front item: {self.front.data}")

    def rear_item(self) -> None:
        """
        Prints the rear item of the queue.

        Returns:
            None
        """
        if self.rear is None:  # If the queue is empty
            print("Queue is empty:)")
            return
        print(f"Rear item: {self.rear.data}")

    def travarse(self) -> None:
        """
        Traverses the queue and prints all elements from front to rear.

        Returns:
            None
        """
        if self.front is None:  # If the queue is empty
            print("Queue is empty:)")
            return
        curr = self.front
        while curr:
            print(curr.data, end=" ")  # Print the data of each node
            curr = curr.next
        print()  # For new line after traversal


# Example usage of the Queue class
q = Queue()
q.enqueue(11)  # Enqueue 11
q.enqueue(12)  # Enqueue 12
q.enqueue(13)  # Enqueue 13
q.enqueue(14)  # Enqueue 14


q.travarse()  # Output: 11 12 13 14
q.dequeue()  # Dequeue the front item (11)
q.travarse()  # Output: 12 13 14

q.size()  # Output: Queue size: 3
q.front_item()  # Output: Front item: 12
q.rear_item()  # Output: Rear item: 14
