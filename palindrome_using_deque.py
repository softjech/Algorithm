class Deque:

    def __init__(self):
        self.items =[]
    
    def add_f(self,item):
        self.items.insert(0, item)

    def add_r(self,item):
        self.items.append(item)

    def remove_f(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def remove_r(self):
        if self.items:
            return self.items.pop()
        return None

    def peek_f(self):
        if self.items:
            return self.items[0]
        return None

    def peek_r(self):
        if self.items:
            return self.items[-1]
        return None

    def is_empty(self):
        return self.items ==[]
    
    def size(self):
        return len(self.items)


def check_palindrome(inp_str):
    my_deque = Deque()
    for c in inp_str:
        my_deque.add_r(c)
    
    while my_deque.size()>=2:
        front=my_deque.remove_f()
        rear=my_deque.remove_r()
        
        if front != rear :
            return False
    return True

#--------------------------- Normal Approach-----------------------------
x="oranges"
y=True
for i in range(len(x)//2):
    print(x[i],x[-i-1],i,len(x)//2)
    if(x[i].lower()==x[-i-1].lower()):
        continue
    else:
        y=False
        break
if y:
    print("Pallindrome")

else:
    print("Not a Pallindrome")
