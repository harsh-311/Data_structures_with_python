
# Queue Data Structure in Python

## What is a Queue?

A **Queue** is a linear data structure that follows the **First In First Out (FIFO)** principle. The first element added to the queue will be the first one to be removed. It is commonly used in scenarios where we need to manage items in an order, such as task scheduling, handling requests in a server, or printing tasks.

## Why Use a Queue?

Queues are essential when you need to maintain an order of tasks or elements and ensure that the first one to arrive is the first to be processed. This makes queues ideal for managing resources, task scheduling, and buffering in various applications.

## Queue Operations

This Python code provides a linked-list implementation of a queue with the following operations:

### 1. **Enqueue**
   Adds an item to the end of the queue.

   ```python
   q.enqueue(value)
   ```

### 2. **Dequeue**
   Removes an item from the front of the queue.

   ```python
   q.dequeue()
   ```

### 3. **Size**
   Displays the number of elements in the queue.

   ```python
   q.size()
   ```

### 4. **Front/Rear Item**
   Retrieves the data at the front or rear of the queue.

   ```python
   q.front_item()
   q.rear_item()
   ```

### 5. **Traverse**
   Displays all elements in the queue.

   ```python
   q.travarse()
   ```

---

## Example Usage

```python
q = Queue()
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)

q.travarse()    # Output: 11 12 13 14
q.dequeue()     # Removes 11
q.travarse()    # Output: 12 13 14
q.size()        # Output: 3
q.front_item()  # Output: 12
q.rear_item()   # Output: 14
```

## License

This project is licensed under the MIT License.
