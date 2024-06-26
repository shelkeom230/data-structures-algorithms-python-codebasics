class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None 
    
    def append(self,data):
        if self.head is None:
            new_node=Node(data)
            new_node.prev=None 
            self.head=new_node

        # 1 element in list
        else: 
            new_node=Node(data)
            curr=self.head 
            while curr.next:
                curr=curr.next 
            curr.next=new_node
            new_node.prev=curr
            new_node.next=None
            

    def prepend(self,data):
        if self.head is None:
            new_node=Node(data)
            new_node.prev=None 
            self.head=new_node
        else:
            node=Node(data)
            self.head.prev=node 
            node.next=self.head 
            self.head=node  
            node.prev=None  
    
    def add_after_node(self,key,data):
        cur=self.head 
        while cur:
            if cur.next is None and cur.data==key:
                self.append(data)
                return 
            elif cur.data==key:
                new_node=Node(data)
                nxt=cur.next 
                cur.next=new_node
                new_node.next=nxt
                new_node.prev=cur
                nxt.prev=new_node
            cur=cur.next 

    def add_before_data(self,key,data):
        cur=self.head 

        while cur:
            if cur.prev is None and cur.data==key:
                 self.prepend(data)
                 return 
            elif cur.data==key:
                new_node=Node(data)
                prev=cur.prev 
                prev.next=new_node
                cur.prev=new_node
                new_node.next=cur 
                new_node.prev=prev
            cur=cur.next

    def delete(self,key):
        cur=self.head 
        while cur:
            if cur==self.head and cur.data==key:
                # case 1 
                if not cur.next:
                    cur=None 
                    self.head=None 
                    return
                
                # case 2 
                else:
                    nxt=cur.next 
                    # detach cur from list 
                    cur.next=None 
                    nxt.prev=None 
                    cur=None
                    self.head=nxt 
                    return
                
                #case 3 
            elif cur.data==key:
                if cur.next:
                    nxt=cur.next 
                    prev=cur.prev
                    prev.next=nxt 
                    nxt.prev=prev 
                    cur.next=None 
                    cur.prev=None
                    cur=None 
                    return 

                # case 4 
                else:
                    prev=cur.prev 
                    prev.next=None 
                    cur.prev=None 
                    cur=None 
                    return 

        cur=cur.next 
    

    def reverse(self):
        tmp=None 
        cur=self.head 
        while cur:
            tmp=cur.prev 
            cur.prev=cur.next 
            cur.next=tmp 
            cur=cur.prev 
        if tmp:
            self.head=tmp.prev 

    def remove_duplicates(self):
        cur=self.head 
        seen=dict()

        while cur:
            if cur.data not in seen:
                seen[cur.data]=1 
                cur=cur.next 
            else:
                nxt=cur.next 
                self.delete_node(cur)
                cur=nxt 
    

    def delete_node(self,node):
        cur=self.head 
        while cur:
            if cur==self.head and cur==node:
                # case 1 
                if not cur.next:
                    cur=None 
                    self.head=None 
                    return
                
                # case 2 
                else:
                    nxt=cur.next 
                    # detach cur from list 
                    cur.next=None 
                    nxt.prev=None 
                    cur=None
                    self.head=nxt 
                    return
                
                #case 3 
            elif cur==node:
                if cur.next:
                    nxt=cur.next 
                    prev=cur.prev
                    prev.next=nxt 
                    nxt.prev=prev 
                    cur.next=None 
                    cur.prev=None
                    cur=None 
                    return 

                # case 4 
                else:
                    prev=cur.prev 
                    prev.next=None 
                    cur.prev=None 
                    cur=None 
                    return 

        cur=cur.next 
         
    def print(self):
         cur=self.head 
         while cur:
             print(cur.data,end=' ')
             cur=cur.next


dllist=DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(4)
dllist.append(5)
dllist.append(5)

dllist.remove_duplicates()
dllist.print() 



