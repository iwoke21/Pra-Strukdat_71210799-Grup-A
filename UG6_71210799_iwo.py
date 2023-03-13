class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def addElementHead(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.current = self.head

    def addElementTail(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.current = self.tail

    def maju(self, step):
        for i in range(step):
            if self.current.next is None:
                break
            self.current = self.current.next
        print(self.current.data)

    def mundur(self, step):
        for i in range(step):
            if self.current.prev is None:
                break
            self.current = self.current.prev
        print(self.current.data)


linkedlist = LinkedList()
linkedlist.addElementHead("Jogja") #Jogja
linkedlist.addElementHead("Jakarta") #Jakarta - Jogja
linkedlist.addElementTail("Bali") #Jakarta - Jogja - Bali
linkedlist.addElementTail("Bandung") #Jakarta - Jogja - Bali - Bandung
linkedlist.maju(2) #output: Bali
linkedlist.mundur(1) #output: Jogja
linkedlist.maju(5) #output: Bali
linkedlist.mundur(3) #output: Bandung
