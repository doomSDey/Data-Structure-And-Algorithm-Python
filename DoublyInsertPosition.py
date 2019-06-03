# insert at any position in doubly linked list

class Node:
    def __init__(self, data = None):
        self.prev = None
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head.data is None:
            print("\nLinked List Is Empty!")
        else:
            ptr = self.head

            while ptr is not None:
                print(f"{ptr.data} -> ", end="")
                ptr = ptr.next

    def insertPosition(self):
        position = int(input("\nEnter Position : "))
        data = int(input("Enter Data : "))
        ptr = Node(data)

        if position is 0:
            if self.head.data is None:
                self.head.data = data
            else:
                ptr.next = self.head
                self.head.prev = ptr
                self.head = ptr
            print("\nNode Inserted!")
        else:
            flag = 0
            temp = self.head

            while temp is not None:
                if position == flag+1:
                    if temp.next is None:
                        temp.next = ptr
                        ptr.prev = temp
                    else:
                        again = temp.next
                        again.prev = ptr
                        temp.next = ptr
                        ptr.prev = temp
                        ptr.next = again
                    print("\nNode Inserted!")
                    break
                else:
                    temp = temp.next
                    flag += 1


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n1. Display\n2. Insert Position\n3. Exit\nChoice : "))
        
        if choice is 1:
            linkedList.display()
        elif choice is 2:
            linkedList.insertPosition()
        elif choice is 3:
            break
        else:
            print("\nInvalid Input!")