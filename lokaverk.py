# https://www.geeksforgeeks.org/self-organizing-list-move-front-method/?ref=rp
class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None
        self.prv = None
    
    def insert(self,numer):
        if self.nxt: # ef það er til næsti fer ég þangað...
            return self.nxt.insert(numer)
        else:
            n = Node(numer)
            # n.value = numer  # þetta er gert í constructor
            self.nxt = n # nxt á self node bendir á nýjan node sem er aftast
            n.prv = self #  prv á nýja hnútnum bendir á mig sjálfan
            return True
            return self.nxt.insert(numer)

    def print_all(self):
        if self is None:
            print('list is empty')
            return
        else:
            n = self
            print('\n List: ', end="")

            while n != None:
                print(n.value,end="")
                if n.nxt != None:
                    print(' --> ',end="")

                n = n.nxt
        
    def search(self,key):
        if self.value == key and self.nxt is None:
            print('True')
            return True
        elif self.value == key and self.nxt is not None:
            print('True')
            return True
        elif self.value != key and self.nxt is None:
            print('False')
            return False
        else:
            return self.nxt.search(key)

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
    
    def search(self, key):
        if self.head is None:
            print('Það er ekkert í listanum')
            return False
        if self.head.search(key) == False:
            print('Það er ekkert í listanum')
            return False
        
        elif self.head.search(key) == True:
            print('hér á að koma kóði til að færa töluna sme var valin fremst')
        else:
            return self.head.search(key)


SO = Self_Orginizing()

SO.insert(5)           # 5
SO.insert(7)           # 5 7
SO.insert(6)           # 5 7 6
SO.print_all()
SO.search(6)           # 6 5 7
SO.print_all()