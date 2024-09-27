# ------------------> DOUBLY LINKED LIST <----------------------
# 1. Define a class Node to describe a node of a doubly linked list.
class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

# 2. Define a class DLL to implement Doubly Linked List with __init__() method to create and initialise start reference variable.
class DLL:
    def __init__(self, start=None):
        self.start = start

# 3. Define a method is_empty() to check if the linked list is empty in DLL class.
    def is_empty(self):
        return self.start is None

# 4. In class DLL, a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

# 5. In class DLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, data):
        temp = self.start
        if self.start is not None:
            while temp.next is not None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp is None:
            self.start = n
        else:
            temp.next = n

# 6. In class DLL, define a method search() to find the node with specified element value.
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

# 7. In class DLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

# 8. In class DLL, define a method to print all the elements of the list.
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

# 9. In class DLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

# 10. In class DLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

# 11. In class DLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self, data):
        if self.start is None:
            return
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

# FOR ITERATING 
    def __iter__(self):
        return DLLIterator(self.start)

# 12. In class DLL, implement iterator for DLL to access all the elements of the list in a sequence.
class DLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

# DRIVER CODE
mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10), 15)

for x in mylist:
    print(x, end=' ')
print()
