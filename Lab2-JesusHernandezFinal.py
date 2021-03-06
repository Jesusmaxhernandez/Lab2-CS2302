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
            return True
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
#sorts linked list in descending order using Bubble Sort 
def bubbleSort(llist):
    #If list empty return none
    if llist is None:
        return None
    #Checks if the linked list has been swapped yet
    swapped = True 
    
    while swapped is True:
        swapped = False
        temp = llist
        while temp.next is not None:
            if temp.password < temp.next.password:
                #simple swap function
                swapped = True
                swap = temp.password
                temp.password = temp.next.password
                temp.next.password = swap
            temp = temp.next
    printList(llist)

    return
#sorts linked list in descending order (a-A-1)
def mergeSort(llist):
    if llist == None or llist.next == None:
        return llist
    length = lLength(llist)
    #Gets the middle for the pivot
    pivot = length//2
    temp = llist
    for i in range(pivot - 1):
        temp = temp.next
    
    llist2 = temp.next
    temp.next = None
    
    sList1 = mergeSort(llist) 

    sList2 = mergeSort(llist2)
    #sorts the list
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
  #merges the two lists back into one      
    while sList1 is not None:
        temp.next = sList1
        sList1 = sList1.next
        temp = temp.next 
    
    while sList2 is not None:
        temp.next = sList2
        sList2 = sList2.next
        temp = temp.next 
    
    return mList
#Main
temp = None   
#opens file and inserts passwords in linked list   
with open('test.txt') as f:
    for line in f:
        info = line.split('\t')
        password = info[1]
        temp = Node(password, 1, temp)
        if not inList(temp, password): 
            temp = Node(password, 1, temp)
            
root = temp

#comment out to implement merge sort
#mList = mergeSort(root)

#comment out to implement bubble sort
mList = bubbleSort(root)

#Prints linked list in descending order
printList(mList)

#Prints 20 most common passwords
popular(temp)

