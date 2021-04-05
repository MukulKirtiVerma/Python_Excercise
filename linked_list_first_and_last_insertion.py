# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:05:58 2021

@author: MUKUL
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
new_ll.insert_first(3)
new_ll.insert_first(5)
new_ll.insert_first(8)
new_ll.insert_first(10)
new_ll.insert_last(1)

new_ll.print_ll()
