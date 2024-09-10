
# Stack Data Structure

## What is a Stack?

A **stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. This means that the last element added to the stack will be the first one to be removed. Think of it as a stack of plates: the plate you add last is the one you remove first.

## Why Use a Stack?

Stacks are useful in situations where you need to store data in a temporary "buffer" and process it in reverse order. Common applications of stacks include:
- **Undo/Redo functionality** in text editors.
- **Function call management** in recursion and program execution.
- **Expression evaluation** (such as infix to postfix conversion).
- **Balancing parentheses** in mathematical expressions.

Stacks are also simple to implement and are often used when we need controlled access to the elements.

## Common Operations on a Stack

The most common operations performed on a stack include:
- **Push**: Add an element to the top of the stack.
- **Pop**: Remove the element from the top of the stack.
- **Peek/Top**: Return the topmost element without removing it.
- **IsEmpty**: Check if the stack is empty.
- **Size**: Return the number of elements in the stack.

### Example of Operations in the Code:

```python
def push(self, value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node
    self.n += 1

def pop(self):
    if self.isempty():
        print("Stack is empty:)")
        return
    pop_value = self.top.data
    self.top = self.top.next
    self.n -= 1
    return pop_value
```

## Additional Features in the Provided Code

1. **Undo/Redo Operations**:
    The `u_r_ope` method demonstrates the use of stacks to perform undo and redo operations. This is commonly used in text editors where you want to go back and forth between states.

    ```python
    def u_r_ope(self, input_str, ur_str):
        undo = Stack()
        redo = Stack()
        # Handles undo/redo based on input
    ```

2. **Mathematical Parentheses Checker**:
    The `math_para_check` function checks if parentheses in a mathematical expression are balanced using two stacks.

    ```python
    def math_para_check(self, math_str):
        # Check if parentheses in the given expression are balanced
    ```

3. **String Reversal**:
    The `reverse_str` function demonstrates how stacks can be used to reverse a string by pushing all characters onto a stack and then popping them off in reverse order.

    ```python
    def reverse_str(self, word):
        for char in word:
            self.push(char)
    ```

4. **Queue Using Stacks**:
    A queue has been implemented using two stacks in the `queue` function. The `enqueue` operation adds elements to one stack, while `dequeue` is managed using two stacks to maintain the FIFO (First In, First Out) order.

    ```python
    def queue(self, oper, value=None):
        # Manage enqueue, dequeue and traversal of elements in a queue-like structure using stacks.
    ```

## Key Elements of a Stack

- **Node**: Each element in the stack is represented as a node containing the value and a reference to the next element.
- **Top**: A reference to the most recent (last added) element in the stack.
- **Next**: A pointer that links the current node to the next node in the stack.

## Conclusion

Stacks are a fundamental data structure used in a variety of real-world applications. They provide a simple but powerful way to manage data in a controlled order. The provided code demonstrates how to implement a stack and use it for various operations such as reversing strings, checking parentheses, and managing undo/redo functionality. Additionally, the code showcases how to simulate a queue using stacks.
