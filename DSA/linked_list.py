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
