# N1 -> N2 -> N3 -> N4 -> N5
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def Insert(self, data):
        self.length +=1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def InsertAtPos(self, pos, data):
        if pos > self.length - 1:
            print("Please Select appropriate Position")
        else:
            prev = None
            current = self.head
            for _ in range(pos):
                prev = current
                current = current.next
            new_node = Node(data)
            prev.next = new_node
            new_node.next = current
    def Print(self):
        current = self.head
        while current is not None:
            if current.next is not None:
                print(current.data, end=' -> ')
            else:
                print(current.data)
            current = current.next
    def Search(self, value):
        current = self.head
        self.count = 0
        self.isSearchFound = False
        while current is not None:
            self.count +=1
            if current.data == value:
                self.isSearchFound = True
                print("The value exists in " + str(self.count) + " Node")
                break
            current = current.next
        if not self.isSearchFound:
            print("The value is not in the List.")
    def Delete(self, data):
        previous = None
        current = self.head
        while current is not None:
            if current.data == data:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.length -=1
                return
            previous = current
            current = current.next
        print("Value not Found")
    def Length(self):
        return self.length

linked_list = LinkedList()
linked_list.Insert(1)
linked_list.Insert(2)
linked_list.Insert(3)
linked_list.Insert(4)
linked_list.Insert(5)
linked_list.Insert(6)
linked_list.Print()
print("Length of List: " + str(linked_list.Length()))
linked_list.Search(4)
linked_list.Delete(2)
linked_list.Print()
linked_list.InsertAtPos(2, 16)
linked_list.Print()