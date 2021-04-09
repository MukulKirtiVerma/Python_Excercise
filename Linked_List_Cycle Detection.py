# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:46:45 2021

@author: Mukul Kirti Verma
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:09:50 2021

@author: Mukul Kirti Verma
"""

class ll:
    def __init__(self):
        self.head=None
    def insert_first(self,data):
        if(self.head==None):
            new_node=Node(data)
            self.head=new_node
        else:
            new_node=Node(data)
            new_node.link=self.head
            self.head=new_node
    def insert_last(self,data):
        current=self.head
        new_node=Node(data)
        while current.link:
            current=current.link
        current.link=new_node
    def insert_mid(self,x,data):
        new_node=Node(data)
        current=self.head
        while current.data!=x and current:
        
            current=current.link
        new_node.link=current.link
        current.link=new_node
        
    def delete_first(self):
        current=self.head
        self.head=self.head.link
        current.link=None
        self.print_ll()
    def delete_last(self):
        current=self.head
        while current.link.link:
            current=current.link
        current.link=None
        self.print_ll()
    def delete_middle(self,m):
        if self.head.data==m:
            self.head=self.head.link
            return
        current=self.head
        while(current.link.data!=m):
            current=current.link
        temp=current.link
        current.link=temp.link
        temp.link=None
    def update(self,k,data1):
        current=self.head
        while(current and current.data!=k):
            current=current.link
        if current==None:
            print("No node to Update with that data")
            return
        current.data=data1
    def create_cycle(self,pos):
        current=self.head
        temp=self.head
        count=1
     
        while temp.link:
               if(count<pos):
                     current=current.link
               temp=temp.link
               count+=1
        temp.link=current
    def cycle_det(self):
        slow=self.head
        fast=self.head.link
        while slow!=fast and fast!=None:
            slow=slow.link
            fast=fast.link
            if(fast==None):
                print("no cycle")
                break
            fast=fast.link
        
        if(fast==None):
            print("no cycle")
        if(slow==fast):
            print("cycle")

    
        
    def print_ll(self):
        current=self.head
   
        while current:
            
            print("| ",current.data,"|",end="->")
            current=current.link
        
    
class Node:
    def __init__(self,data):
       
        self.data=data
        self.link=None
new_ll=ll()
new_ll.insert_first(1)
new_ll.insert_first(2)
new_ll.insert_first(3)
new_ll.insert_first(4)
new_ll.insert_last(5)



new_ll.create_cycle(3)
new_ll.cycle_det()
new_ll.print_ll()
new_ll.insert_mid(3,7)
new_ll.delete_first()
new_ll.delete_last()
new_ll.delete_middle(4)
new_ll.update(7,5)
