import copy


class Node:
    """
    Class to represent a node in a stack.

    Attributes:
        data (int or str): The value stored in the node.
        next (Node): Pointer to the next node in the stack.
    """

    def __init__(self, value: int | str) -> None:
        self.data = value
        self.next = None


class Stack:
    """
    Class to represent a stack using linked list.

    Attributes:
        top (Node): Pointer to the top node of the stack.
        n (int): Number of elements in the stack.
        auth (bool): A flag used for queue operations.
    """

    def __init__(self) -> None:
        self.top = None
        self.n = 0
        self.auth = True

    def isempty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise.
        """
        return self.top is None

    def push(self, value: int | str) -> None:
        """
        Push a new value onto the stack.

        Args:
            value (int or str): The value to be added to the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n += 1

    def traverse(self) -> None:
        """
        Traverse and print all elements in the stack from top to bottom.
        """
        if self.isempty():
            print("Stack is empty:)")
        else:
            temp = self.top
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
        print("\n")

    def peek(self) -> None:
        """
        Peek at the top element of the stack without removing it.
        """
        if self.isempty():
            print("Stack is empty:)")
        else:
            print(self.top.data)

    def pop(self) -> int | str:
        """
        Pop and return the top element of the stack.

        Returns:
            int or str: The value of the popped element.
        """
        if self.isempty():
            print("Stack is empty:)")
            return None
        pop_value = self.top.data
        self.top = self.top.next
        self.n -= 1
        return pop_value

    def reverse_str(self, word: str) -> None:
        """
        Reverse a string using stack.

        Args:
            word (str): The string to be reversed.
        """
        for char in word:
            self.push(char)
        reversed_word = ""
        increment_count = 0

        while increment_count != len(word):
            increment_count += 1
            reversed_word += self.pop()

        print(reversed_word)

    def size(self) -> int:
        """
        Return the size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return self.n

    def u_r_ope(self, input_str: str, ur_str: str) -> None:
        """
        Perform undo/redo operations using two stacks.

        Args:
            input_str (str): The initial string before undo/redo operations.
            ur_str (str): The string representing undo ('u') and redo ('r') operations.
        """
        undo = Stack()
        redo = Stack()

        temp_data = ""

        for char in input_str:
            undo.push(char)
        for char in ur_str:
            if char == "u":
                redo.push(undo.pop())
            else:
                undo.push(redo.pop())

        while undo.top is not None:
            temp_data += undo.pop()
        undo.reverse_str(temp_data)

    def math_para_check(self, math_str: str) -> None:
        """
        Check if the parentheses in a mathematical expression are balanced.

        Args:
            math_str (str): The mathematical expression to be checked.
        """
        l = Stack()
        r = Stack()

        for item in math_str:
            if item in "[({":
                l.push(item)
            if item in "]})":
                r.push(item)

        if l.size() == r.size():
            print("Equation is balanced")
        else:
            print("Equation is not balanced")

    def queue(self, oper: str, value: int = None) -> None:
        """
        Implement queue using two stacks.

        Args:
            oper (str): Operation to perform ('enqueue', 'dequeue', or 'traverse').
            value (int, optional): The value to enqueue into the queue. Defaults to None.
        """
        if self.auth:
            global s1, s2
            s1 = Stack()
            s2 = Stack()
            self.auth = False

        def dequeue() -> None:
            """
            Perform dequeue operation.
            """
            if s1.isempty() and s2.isempty():
                return print("Queue is empty:)")
            else:
                if s2.isempty():
                    while s1.top:
                        s2.push(s1.top.data)
                        s1.top = s1.top.next
                    s2.pop()
                else:
                    s2.pop()

        def traverse() -> None:
            """
            Traverse the elements in the queue.
            """
            while s1.top:
                s2.push(s1.top.data)
                s1.top = s1.top.next

        if oper == "enqueue":
            s1.push(value)

        elif oper == "dequeue":
            dequeue()
        else:
            if s1.isempty() and s2.isempty():
                return print("Queue is empty:)")
            if s2.isempty():
                traverse()
                s_2 = copy.copy(s2)
                result = ""
                while s_2.top:
                    result += str(s_2.top.data) + "->"
                    s_2.top = s_2.top.next
                print(result[:-2])
                return
            s_1 = copy.copy(s1)
            s_2 = copy.copy(s2)
            result = ""
            while s_1.top:
                while s_2.top:
                    result += str(s_2.top.data) + "->"
                    s_2.top = s_2.top.next
                temp = []
                while s_1.top:
                    temp.append(str(s_1.top.data))
                    s_1.top = s_1.top.next
                temp = temp[::-1]

                if temp:
                    for item in temp:
                        result += item + "->"

            print(result[:-2])


# Example of each method with output:

s = Stack()

# 1. Push operation
print("1. Push Operation:")
s.push(10)
s.push(20)
s.push(30)
s.traverse()  # Output: 30 20 10

# 2. Pop operation
print("2. Pop Operation:")
s.pop()  # Output: 30
s.traverse()  # Output: 20 10

# 3. Peek operation
print("3. Peek Operation:")
s.peek()  # Output: 20

# 4. Size operation
print("4. Size Operation:")
print(s.size())  # Output: 2

# 5. Reverse string operation
print("5. Reverse String Operation:")
s.reverse_str("Hello")  # Output: olleH

# 6. Undo/Redo operation
print("6. Undo/Redo Operation:")
s.u_r_ope("Hello", "uu")  # Output: ollH

# 7. Parenthesis check operation
print("7. Parenthesis Check Operation:")
s.math_para_check("[{(a+b)+(c+d)}]")  # Output: Equation is balanced

# 8. Queue operations (using two stacks)
print("8. Queue Operations:")
s.queue("enqueue", 1)
s.queue("enqueue", 2)
s.queue("enqueue", 3)
s.queue("travarse")  # Output: 1->2->3
s.queue("dequeue")
s.queue("travarse")  # Output: 2->3
