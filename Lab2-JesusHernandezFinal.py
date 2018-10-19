#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Jesus Maximino Hernandez 88756947
#Data Structures - Diego Aguirre
#Lab 2 - Option B
#Program sorts passwords in linked list then
#prints the top 20 most used passwords
"""
Created on Wed Oct 17 20:57:02 2018

@author: JesusMHernandez
"""

import collections
#creates node
class Node:
    password =""
    count = 1
    next = None
    def __init__(self, password, count, next):
        self.password = password
        self.next = next
    def __in__(self, password, next):
        self.password = password
        self.next = next
        
        Node(password, 1, temp)
        
#function to print linked list
def printList(llist):
    while llist is not None:
        #Prints the number of times the linked list comes out
        #print(llist.count)
        print(llist.password)
        llist = llist.next
#check if password is alread in list
def inList(llist, password):
    tempPass = llist
    while tempPass is not None:
        if(tempPass.password == password):
            tempPass.count += 1
            #print(tempPass.count)
            
        tempPass = tempPass.next  
    return False
#Prints top 20 most popular passwords
def popular(llist):
    temp = llist
    tempList = []
    #gets elements from linked list and puts it into a list
    while llist is not None:
        tempList.append(temp.password)  
        temp = temp.next
        llist = llist.next
        
    #removes \n from list     
    tempList = map(lambda s: s.strip(), tempList)
    
    #print(tempList)
    #puts items in linked list into list
    from collections import Counter
    c = Counter(tempList)
    print()
    print("20 most common passwords are: ") 
    print(c.most_common(20))

    
#finds length of linked list
def lLength(llist):
    count = 0
    while llist is not None:
        count += 1
        llist = llist.next
    return count
#sorts linked list in descending order
def mergeSort(llist):
    if llist == None or llist.next == None:
        return llist
    length = lLength(llist)
    pivot = length//2
    temp = llist
    for i in range(pivot - 1):
        temp = temp.next
    
    llist2 = temp.next
    temp.next = None
    
    sList1 = mergeSort(llist) 

    sList2 = mergeSort(llist2)
    
    if(sList1.password > sList2.password):
        mList = sList1
        sList1 = sList1.next
    else:
        mList = sList2
        sList2 = sList2.next
    temp = mList
    while sList1 is not None and sList2 is not None:        
        if(sList1.password > sList2.password):
            temp.next = sList1
            sList1 = sList1.next
        else:
            temp.next = sList2
            sList2 = sList2.next
        temp = temp.next
        
    while sList1 is not None:
        temp.next = sList1
        sList1 = sList1.next
        temp = temp.next 
        
    while sList2 is not None:
        temp.next = sList2
        sList2 = sList2.next
        temp = temp.next 
    
    return mList

temp = None   
#opens file and inserts passwords in linked list   
with open('10-million-combos.txt') as f:
    for line in f:
        info = line.split('\t')
        password = info[1]
#       temp = Node(password, 1, temp)
        if not inList(temp, password): 
            temp = Node(password, 1, temp)
            
root = temp
mList = mergeSort(root)
#Prints linked list in descending order
#printList(mList)
#Prints 20 most common passwords
popular(mList)