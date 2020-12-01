# https://www.geeksforgeeks.org/self-organizing-list-move-front-method/?ref=rp
class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None
        self.head = None
        self.prv = None
        self.rear = None
    
    def insert(self,numer):
        if self.nxt is None:
            n  = Node(self.value)
            n.value = numer
            n.nxt = None

            if self.head == None:
                self.head = self.rear = n
            else:
                self.rear.nxt = n
                self.rear = n
            
        else:
            return self.nxt.insert(self.value)
    
    def print_all(self):
        if self.head is None:
            print('list is empty')
            return
        else:
            n = Node(self.value)
            print('List: ')

            while n != None:
                print(n.value)
                if n.nxt != None:
                    print('-->')

                n = n.nxt
            print(self.value)
        
    def search(self,key):
        current = self.head

        self.prv = None

        while current != None:
            if current.value == key:
                if self.prv != None:
                    self.prv.nxt = current.nxt
                    current.nxt = self.head
                    self.head = current
                return True
            self.prv = current
            current = current.nxt
        return False

class Self_Orginizing:
    def __init__(self):
        self.head = None

    def print_all(self):
        if self.head is None:
            print('tómur listi')
        else:
            self.head.print_all()
    
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            self.head.insert(value)
    
    def search(self, value):
        if self.head is None:
            print('Það er ekkert í listanum')
            return False
        else:
            return self.head.search(value)

SO = Self_Orginizing()
SO.insert(5)           # 5
SO.insert(7)           # 5 7
SO.insert(6)           # 5 7 6
SO.print_all()
SO.search(6)           # 6 5 7