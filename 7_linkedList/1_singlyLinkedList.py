class node:
    def __init__(self, value = None):
        self.value = value,
        self.next = None
        

class single:
    def __init__(self):
        self.head = None,
        self.tail = None
    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next
    def insertSll(self, value, location):
        newNode = node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail = newNode
                self.tail.next = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traversing(self):
        if self.head is None:
            print('list doesn;t exist')
        else:
            nd = self.head
            while nd is not None:
                print(nd.value)
                nd = nd.next

    def searching(self, nodeValue):
        if self.head is None:
            print('Linked list doesnt exist')
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return 'There is no such value'
    
    def deletion(self, location):
        if self.head is None:
            print('Linked list doesnot exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.tail
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    def deleteAll(self):
        if self.head is None:
            print('There is no sll')
        else:
            self.head = None
            self.tail = None
singleLinkedList = single()
singleLinkedList.insertSll(1, 1)
node1 = node(1)
node2 = node(2)

singleLinkedList.head = node1
singleLinkedList.head.next = node2
singleLinkedList.tail = node2
 
print([node.value for node in singleLinkedList])
singleLinkedList.traversing()
print(singleLinkedList.searching(33))
