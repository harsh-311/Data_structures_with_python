
## What is a Linked List?

A **Linked List** is a data structure used to store a collection of elements. Each element in the list is stored in a separate object, called a **node**, and these nodes are linked together by pointers. Unlike arrays, linked lists do not require contiguous memory allocation, allowing for more efficient memory management.

In a singly linked list, each node points to the next node in the sequence, and the last node points to `None`, indicating the end of the list.

### Types of Linked Lists:

1. **Singly Linked List**: Each node points to the next node, and the last node points to `None`.
2. **Doubly Linked List**: Each node points to both the next node and the previous node.
3. **Circular Linked List**: The last node points back to the first node, creating a circular loop.

## What is a Node?

A **Node** is the building block of a linked list. It contains two main components:
- `value`: The data or value that the node holds.
- `next`: A pointer to the next node in the list (or `None` if it is the last node).

### Interaction Between Node and Linked List

- In a linked list, nodes are connected through the `next` pointers. The linked list class (`Linklist`) maintains a reference to the first node, called the **head**. From this head node, we can traverse the entire list by following the `next` pointers.
- Inserting or deleting nodes involves manipulating these `next` pointers to connect or disconnect nodes as needed.
# Linked List Implementation in Python

This repository contains a Python implementation of a singly linked list data structure. The implementation includes various operations such as insertion, deletion, searching, sorting, and more.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Class Structure](#class-structure)
- [Methods](#methods)
- [Example](#example)

## Features

This linked list implementation provides the following features:

- Insertion at the head, tail, and middle of the list
- Deletion from the head, tail, and by value
- Searching by value and index
- Sorting in ascending or descending order
- Reversing the list
- Finding maximum and minimum values
- Summing values at odd or even positions
- Converting list elements to a string
- Removing duplicate elements

## Usage

To use this linked list implementation, simply copy the `Linklist` and `Node` classes into your Python project. You can then create a new linked list and perform operations on it as shown in the [Example](#example) section.

## Class Structure

The implementation consists of two classes:

1. `Node`: Represents a single node in the linked list.
2. `Linklist`: Represents the linked list and contains all the methods for manipulating the list.

### Node Class

```python
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
```

### Linklist Class

```python
class Linklist:
    def __init__(self) -> None:
        self.n = 0
        self.head = None
    
    # Methods are listed in the next section
```

## Methods

The `Linklist` class provides the following methods:

- `insert_head(value)`: Insert a new node at the beginning of the list
- `insert_tail(value)`: Insert a new node at the end of the list
- `insert_middle(after, value)`: Insert a new node after a specified value
- `sort_list(input)`: Sort the list in ascending or descending order
- `clear()`: Remove all nodes from the list
- `delete_head()`: Remove the first node of the list
- `delete_tail()`: Remove the last node of the list
- `remove(value)`: Remove a node with a specific value
- `search_by_value(value)`: Find a node by its value
- `search_by_index(index)`: Find a node by its index
- `max_value()`: Find the maximum value in the list
- `min_value()`: Find the minimum value in the list
- `pos_sum(input)`: Sum values at odd or even positions
- `reverse_list()`: Reverse the order of nodes in the list
- `convert_str()`: Convert list elements to a string
- `remove_duplicates()`: Remove duplicate nodes from the list
- `__len__()`: Return the length of the list
- `__str__()`: Return a string representation of the list

## Example

Here's an example of how to use the linked list:

```python
L = Linklist()
L.insert_head("a")
L.insert_head("b")
L.insert_head("*")
L.insert_tail("d")
L.insert_head("|")
L.insert_head("v")
L.insert_head("%")
L.insert_head("e")
L.insert_head("l")
L.insert_head("p")
L.insert_head("p")

print(L)  # Output: p->l->e->%->v->|->*->b->a->d

L.convert_str()  # Output: ple v    bad

L.remove_duplicates()
print(L)  # Output: p->l->e->%->v->|->*->b->a->d

L.sort_list("inc")
print(L)  # Output: %->*->|->a->b->d->e->l->p->v

L.reverse_list()
print(L)  # Output: v->p->l->e->d->b->a->|->*->%
```

Feel free to explore and use this linked list implementation in your projects!