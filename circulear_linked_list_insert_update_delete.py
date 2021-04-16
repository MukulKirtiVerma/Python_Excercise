# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:14:11 2021

@author: Mukul Kirti Verma
"""



class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        
class ll:
    def __init__(self):
        self.head=None
    def insert_first(self,data):
        if(self.head==None):
            
            new_node=Node(data)
            new_node.next=new_node
            self.head=new_node
            
            return
        new_node=Node(data)
        new_node.next=self.head
        current=self.head
        while current.next!=self.head:
            current=current.next
        current.next=new_node
        self.head=new_node
        self.print_ll()
        
    def insert_last(self,data):
        new_node=Node(data)
        current=self.head
        while current.next!=self.head:
            current=current.next
        current.next=new_node
        new_node.next=self.head
        self.print_ll()
        
        
        
    def insert_mid(self,d,data):
       new_node=Node(data)
       current=self.head
       while current.data!=d:
           current=current.next
       new_node.next=current.next
       current.next=new_node
       self.print_ll()
            
    def delete_first(self):
        if(self.head==None):
            print("No node to delete")
            return
        if(self.head.next==self.head):
            self.head=None
            
            return
        self.head=self.head.next
        current=self.head
        while current.next.next!=self.head:
            current=current.next
        current.next.next=None
        current.next=self.head
        self.print_ll()
    def delete_last(self):
        if(self.head==None):
            print("no node to delete")
            return
        if(self.head.next==self.head):
            self.head=None
            self.print_ll()
            return
        current=self.head
        while current.next.next!=self.head:
            current= current.next
            
        current.next.next=None
        current.next=self.head
        self.print_ll()
    def update(self,d,data):
        if(self.head==None):
            print("linked list is empty ")
            return
        current=self.head
        while current.next!=self.head and current.data!=d:
            current=current.next
        if(current.data==d):
            current.data=data
        self.print_ll()
    def print_ll(self):
        
        if(self.head==None):
            print("no node to print")
            return
        if(self.head.next==self.head):
            print("|",self.head.data,"|->")
            return
        current=self.head
 
        while current.next!=self.head:
            print("|",current.data,"|->",end="")
            current=current.next
        print("|",current.data,"|->",end="")
            
            
            
        
        
new_ll=ll()
new_ll.insert_first(1)
new_ll.insert_first(2)
new_ll.insert_first(3)
new_ll.insert_first(4)
new_ll.insert_first(5)
new_ll.insert_last(9)
new_ll.insert_mid(4,11)
new_ll.delete_first()
new_ll.delete_last()
new_ll.update(11,22)
new_ll.print_ll()
new_ll.insert_last(3)
new_ll.insert_mid(1,5)
