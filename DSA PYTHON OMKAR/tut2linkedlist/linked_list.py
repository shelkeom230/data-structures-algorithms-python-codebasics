class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next 
    
class LinkedList:
    def __init__(self):
        self.head=None 
    
       
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node 

    def print(self):
        itr=self.head 

        ll=""
        while itr:
            ll+=str(itr.data)+" --> "
            itr=itr.next 
        print(ll)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return 

        itr=self.head 
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None) 
    
    def insert_values(self,data_list):
        self.head=None 
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        count=0
        itr=self.head 
        while itr:
            count+=1
            itr=itr.next 
        return count  

    def remove_at(self,idx):
        if idx<0 or idx>=self.length():
            raise Exception('invalid idx')

        if idx==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head 
        while itr:
            if count==idx-1:
                itr.next=itr.next.next 
                break 
            itr=itr.next 
            count+=1
    
    def insert_at(self,index,data):
        if index<0 or index>self.length():
            raise Exception('invalid index')
        
        if index==0:
            self.insert_at_beginning(data)
            return 
        
        count=0
        itr=self.head 
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node 
            itr=itr.next 
            count+=1
    
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            node=Node(data_to_insert,None)
            self.head=node 
            return 
            
        itr=self.head 
        while itr:
            if itr.data==data_after:
                node=Node(data_to_insert,itr.next)
                itr.next=node 
                break 
            itr=itr.next 
    
    def remove_by_value(self,data):
        # remove first node that contains data 
        if self.head is None:
            print('empty list , cannot remove')
            return 
        if self.head.data==data:
            self.head=self.head.next 
            return 
        
        prev_node=self.head 
        curr_node=self.head.next 

        while curr_node:
            if curr_node==data:
                prev_node.next=curr_node.next 
                curr_node.next=None 
            prev_node=curr_node
            curr_node=curr_node.next 

if __name__=="__main__":
    ll=LinkedList()
    ll.insert_values(['omkar','devesh','kalash','priyansh'])
    # ll.print()
    ll.remove_at(2)
    ll.insert_at(0,'dhaval')
    ll.insert_at(2,'aarash')
    ll.insert_after_value('omkar','abhinav')
    ll.remove_by_value('omkar')
    ll.print()
    print(ll.length())