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
        if self.value == key and self.prv is None:      # Head
            return True
            # Þinn kóði hér Tumi ef hnútur er fremstur...
        elif self.value == key and self.nxt is None:    # Last
            self.prv.nxt = self.nxt
            return self
            # Þinn kóði hér Tumi ef hnútur er aftastur
        elif self.value == key and self.nxt:            # Í miðju
            self.prv.nxt = self.nxt #tengjum framhjá
            self.nxt.prv = self.prv #tengjum framhjá

            self.prv = None # slítum frá listnaum
            self.nxt = None # slítum frá listnaum

            return self # skilum honum til baka í Self_Orginizing

        elif self.value != key and self.nxt is None:    # Hnútur ekki til
            return None
        else:                                           # Förum í næsta hnút...
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
        if self.head is None:                       # Listinn tómur
            print('Tómur listi')
            return False
        else:
            n =  self.head.search(key)              # Fáum hnútinn til baka ef hann er til annars None
            
            if n is None:                           # Hnútur ekki til í listanum
                print("Ekki í lista")
            elif n is True:
                print("\n tala er fremst")
            else:
                n.nxt = self.head
                self.head.prv = n
                self.head = n


SO = Self_Orginizing()

SO.insert(5)           # 5
SO.insert(7)           # 5 7
SO.insert(6)           # 5 7 6
SO.insert(9)           # 5 7 6 9
SO.print_all()
SO.search(6)           # 6 5 7 9
SO.print_all()
SO.search(9)           # 6 5 7
SO.print_all()
SO.search(5)
SO.print_all()