# ---------------------------------------> CIRCULAR LINKED LIST <--------------------------  

# 1. Define a class Node to describe a node of a circular linked list.
class Node:
    def __init__ (self, item=None, next=None):
        self.item = item
        self.next = next

# 2. Define a class CLL to implement Circular Linked List with init_() method to create and initialise last reference variable.
class CLL:
    def __init__(self, last=None):
        self.last = last

    # 3. Define a method is_empty() to check if the linked list is empty in CLL class.
    def is_empty(self):
        return self.last is None

    # 4. In class CLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    # 5. In class CLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    # 6. In class CLL, define a method search() to find the node with specified element value.
    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while True:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.last.next:
                break
        return None

    # 7. In class CLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n

    # 8. In class CLL, define a method to print all the elements of the list.
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while True:
                print(temp.item, end=' ')
                temp = temp.next
                if temp == self.last.next:
                    break
            print()

    # 9. In class CLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    # 10. In class CLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    # 11. In class CLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self, data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp != self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                            break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    # FOR ITERATION
    def __iter__(self):
        if self.last is None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)

# 12. In class CLL, implement iterator for CLL to access all the elements of the list in a sequence.
class CLLIterator:
    def __init__(self, start):
        self.current = start
        self.first = start
        self.started = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.first and self.started:
            raise StopIteration
        self.started = True
        data = self.current.item
        self.current = self.current.next
        return data

# DRIVER CODE
mylist = CLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(10), 50)

for x in mylist:
    print(x, end=" ")
print()

# OR
mylist.print_list()
