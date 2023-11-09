class Node:
    def __init__(self, v=None):
        self.v=v
        self.next=None
        return
    
    def is_empty(self):
        return True if self.v==None else False

    def append(self, v):
        if self.is_empty():
            self.v=v
        elif self.next==None:
            self.next=Node(v)
        else:
            self.next.append(v)
        return
        
    def insert(self,v):
        if self.is_empty():
            self.v=v
        new_node=Node(v)
        self.v, new_node.v=new_node.v, self.v
        self.next, new_node.next=new_node, self.next
        return
        
    def delete(self,v):
        if self.is_empty():
            return
        if self.v==v:
            self.v=None
            if self.next!=None:
                self.v=self.next.v
                self.next=self.next.next
            return
        else:
            if self.next!=None:
                self.next.delete(v)
                if self.next.v==None:
                    self.next=None
        
    def printer(self):
        while(self!=None):
            print(self.v)
            self=self.next
        # return

# 1 2 3 4 5
n=Node(1)
n.append(2)
n.append(3)
n.insert(0)
n.insert(-1)
n.delete(3)
n.printer()
