# https://www.geeksforgeeks.org/self-organizing-list-move-front-method/?ref=rp
class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None
        self.head = None
        self.prv = None
        # self.rear = None sé ekki tilgang með þessum
    
    def insert(self,numer):
        if self.nxt: # ef það er til næsti fer ég þangað...
            return self.nxt.insert(numer)
        else:
            n = Node(numer)
            # n.value = numer  # þetta er gert í constructor
            self.nxt = n # nxt á self node bendir á nýjan node sem er aftast
            n.prv = self #  prv á nýja hnútnum bendir á mig sjálfan
            return True

            """  sé ekki tilgang með þessu eða hvað ??????
            if self.head == None:
                self.head = self.rear = n
            else:
                self.rear.nxt = n
                self.rear = n
            """
        
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
            #print(self.value)
        
    """def search(self,key):
        tmp = self.value
        mein_value = key

        #skoða hvort það er eitthvað í litanum eða hvort það er bara eins tala
        if not tmp or not tmp.nxt:
            return print('ekkert til að færa')
        

        while tmp and tmp.nxt:
            mein_value = tmp
            tmp = tmp.nxt
        
        # benda næst seinasta sem none
        mein_value.nxt = None

        # setja valda node sem firsta
        tmp.nxt = self.value
        self.value = tmp"""

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
        tmp = self.head
        mein_value = key

        #skoða hvort það er eitthvað í litanum eða hvort það er bara eins tala
        if not tmp or not tmp.nxt:
            return print('ekkert til að færa')
        

        while tmp and tmp.nxt:
            mein_value = tmp
            tmp = tmp.nxt
        
        # benda næst seinasta sem none
        mein_value.nxt = None

        # setja valda node sem firsta
        tmp.nxt = self.head
        self.head = tmp

SO = Self_Orginizing()

SO.insert(5)           # 5
SO.insert(7)           # 5 7
SO.insert(6)           # 5 7 6
SO.print_all()
SO.search(7)           # 6 5 7
SO.print_all()