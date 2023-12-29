class Node:
    def __init__(self,v=None):
        self.v=v
        self.next=None
    
    def isEmpty(self):
        return False if self.v!=None else True
    
    def append(self, v):
        if self.isEmpty():
            self.v=v
            return
        elif self.next==None:
            self.next=Node(v)
        else:
            self.next.append(v)
    
    def printer(self):
        while self is not None:
            print(self.v, end=' -> ')
            self=self.next
    
    def delete(self,v):
        if self.isEmpty():
            return
        elif self.v==v:
            self.v=self.next.v
            self.next=self.next.next
        else:
            self.next.delete(v)
        return
    
    def insert_f(self,v):
        if self.isEmpty():
            self.v=v
        else:
            node=Node(v)
            node.v, self.v=self.v, node.v
            self.next,node.next=node,self.next
    
    def insert_l(self,v):
        if self.isEmpty():
            self.v=v
        else:
            while self.next is not None:
                self=self.next
            self.next=Node(v)
    
    def insert_ith(self,i,v):
        if self.isEmpty():
            return
        for _ in range(i-1):
            self=self.next
        node=Node(v)
        self.next, node.next=node, self.next
    
    def delete_ith(self,i):
        if self.isEmpty():
            return
        for _ in range(i-1):
            self=self.next
        self.next=self.next.next


n=Node()
# print(n.isEmpty())
n.append(1)
n.append(2)
n.append(3)
n.append(4)
n.append(5)
n.append(6)
n.append(7)
print(n.printer())
n.delete(3)
n.delete(6)
print(n.printer())
n.insert_f(0)
print(n.printer())
n.insert_f(-1)
print(n.printer())
n.delete(-1)
print(n.printer())
n.insert_l(8)
print(n.printer())
n.insert_ith(3,99)
print(n.printer())
n.delete_ith(4)
print(n.printer())