import copy


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Linklist:
    def __init__(self) -> None:
        self.n = 0
        self.head = None

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def insert_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while True:
            if curr.next == None:
                curr.next = new_node
                break
            curr = curr.next
        self.n += 1

    def insert_middle(self, after, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr:
            if curr.value == after:
                break
            curr = curr.next
        else:
            print("Item not found:)")
            return
        temp = curr.next
        curr.next = new_node
        new_node.next = temp
        self.n = self.n + 1

    def sort_list(self, input):
        """inc for increase or dec for decrease"""
        if not self.head or not self.head.next:
            return  # List is already sorted if it's empty or has only one element

        swapped = True
        if input == "dec":
            while swapped:
                swapped = False
                curr = self.head
                while curr.next:
                    if curr.value > curr.next.value:
                        # Swap the values of the two nodes
                        curr.value, curr.next.value = curr.next.value, curr.value
                        swapped = True
                    curr = curr.next
        else:
            while swapped:
                swapped = False
                curr = self.head
                while curr.next:
                    if curr.value < curr.next.value:
                        # Swap the values of the two nodes
                        curr.value, curr.next.value = curr.next.value, curr.value
                        swapped = True
                    curr = curr.next

    def __str__(self):
        curr = self.head
        values = ""
        if curr == None:
            return "List is empty"
        while curr:
            values += f"{curr.value}->"
            curr = curr.next
        return values[:-2]

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            print("Link-list is empty:)")
            return

        self.head = self.head.next
        self.n -= 1

    def delete_tail(self):
        curr = self.head

        if self.head == None:
            print("Link-list is empty:)")
        for i in range(len(self) - 2):
            curr = curr.next
        curr.next = None
        self.n -= 1

    def remove(self, value):
        if self.head == None:
            print("Link-list is empty:)")
            return

        if self.head.value == value:
            print("You mean delete head:)")
            self.delete_head()
            return

        curr = self.head
        temp = None
        while curr:
            if curr.value == value:
                break
            temp = curr
            curr = curr.next
        else:
            print("Item not found:)")
            return

        temp.next = curr.next
        self.n -= 1

    def search_by_value(self, value):
        if self.head == None:
            print("Link-list is empty:)")
            return
        if self.head.value == value:
            print(f"The given value found on index {1}")
            return

        curr = self.head.next
        for i in range(2, len(self) + 1):
            if curr.value == value:
                print(f"The given value found on index {i}")
                break
            curr = curr.next
        else:
            print("Value is not found:)")

    def search_by_index(self, index):
        if self.head == None:
            print("Link-list is empty:)")
            return
        if index == 1:
            print(f"The value on index {index} is {self.head.value}")
            return

        curr = self.head.next
        for i in range(2, len(self) + 1):
            if i == index:
                print(f"The value on index {i} is {curr.value}")
                break
            curr = curr.next
        else:
            print("The given index is out of bound")

    def max_value(self):
        if not self.head:
            print("Link-list is empty:)")
            return

        curr = self.head
        max_value = 0

        while curr:
            if max_value < curr.value:
                max_value = curr.value

            curr = curr.next

        print(max_value)

    def min_value(self):
        if not self.head:
            print("Link-list is empty:)")
            return

        curr = self.head
        min_value = self.head.value
        while curr:

            if min_value > curr.value:
                min_value = curr.value
            curr = curr.next
        print(min_value)

    def pos_sum(self, input):
        """Odd or Evern"""
        if not self.head:
            print("Link-list is empty:)")
            return
        if input.lower() == "odd":
            sum = 0
            curr = self.head
            for i in range(0, len(self), 2):
                print(curr.value)
                sum = sum + curr.value
                for i in range(2):
                    curr = curr.next

        if input.lower() == "even":
            sum = 0
            curr = self.head.next
            for i in range(0, len(self) // 2):
                print(curr.value)
                sum = sum + curr.value
                for i in range(2):
                    if curr.next:
                        curr = curr.next
            print(sum)

    def reverse_list(self):
        if not self.head:
            print("Link-list is empty:)")
            return
        prev_node = None
        curr_node = self.head

        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node

    def convert_str(self):
        curr = self.head
        main_str = ""
        while curr:
            if curr.value.isalpha():
                main_str += curr.value
            else:
                main_str += " "
            if curr:
                curr = curr.next
        print(main_str)

    def remove_duplicates(self):
        if not self.head:
            print("Link-list is empty:)")
            return
        curr_1 = self.head
        length_list = len(self)
        while curr_1:
            curr = curr_1
            value = curr_1.value
            for _ in range(length_list):
                prev = curr
                if curr:
                    curr = curr.next
                    if curr:
                        if value == curr.value:
                            prev.next = curr.next
            length_list -= 1
            if curr_1:
                curr_1 = curr_1.next

    def __len__(self):
        return self.n


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
L.convert_str()
print(L)
