class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        return

    def is_empty(self):
        return True if self.value == None else False

    def append(self, v):
        if self.is_empty():
            self.value = v
        elif self.next == None:
            self.next = Node(v)
        else:
            self.next.append(v)
        return

    def append_r(self, v):
        if self.is_empty():
            self.value = v
            return
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = Node(v)
        return

    def insert(self, v):
        if self.is_empty():
            self.value = v
            return
        new_node = Node(v)
        self.value, new_node.value = new_node.value, self.value
        self.next, new_node.next = new_node, self.next
        return

    def delete(self, v):
        if self.is_empty():
            return
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return
        # 1 2 3 4 5, 2


n = Node()
print(n.is_empty())

"""
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
"""
