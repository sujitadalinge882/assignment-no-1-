#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#You will have a number of elements and in the next n lines element of a list.You have to create a list from the given.
#strings.You have to sort the list based on 2nd last character of a string.

#For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be 
#['great', 'abc', 'hello','hiyo]

#Input Format:

#At first-line it will have an integer (number of elements inside a list). In the second line, it will have a string.

#Output Format:

#A single line containing a sorted list.
                                                                                              
                                                                                              
                                                                                              
def Question1(l):
    l1=[]
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j][-2]<l[j+1][-2]:
                pass
            else:
                l1=l[j]
                l[j]=l[j+1]
                l[j+1]=l1
            return l
        n=int(input())
        s=input()
        t=s.split()
        m=t[:n]
        print(m)
        Question1(m)
def Question1(lst):
        lst.sort(key=lambda x: (x[-2]))
        return lst
n=int(input())
s=input()
t=s.split()
m=t[:n]
print(m)
Question1(m)
                                                                                        


# In[8]:


#Your task is to complete the validate_triangle and validate_rectangle functions for the classes.Hint for validating 
#is given in the
#comments of the code. Also you will have to print the following after validation in respective functions:-

#1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)

#2.Valid Triangle:If the triangle sum property of sides is valid.

#3.Valid Rectangle:If 2 side pairs are same and they are input in correct order like l,b,l,b

#4.Invalid Rectangle: If Not Valid rectangle as stated above.

#Input Format:

#The side length of triangle followed by for rectangle in the next line in order.

#Output Format:

#since object are created in order, so first validate info about triangle will come and than rectangle.

#Sample Input 0:

#3 4 5

#2 4 2 4

#Sample Output 0:

#Valid Triangle

#Valid Rectangle


class Triangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_triangle(self,l):
        if len(l)==3 and (l[0]+l[1])>l[0]:
            return "Valid Triangle"         
        else:
            return "Invalid Triangle"
class Rectangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_rectangle(self,l):
        if len(l)==4 and  (l[0]==l[2]) and (l[1]==l[3]):
            return "Valid Rectangle"         
        else:
            return "Invalid Rectangle"
    s=list(map(int,input().split()))
    t=list(map(int,input().split()))
    A=Triangle(s) 
    print(A.validate_triangle(s))
    B=Rectangle(t)
    print(B.validate_rectangle(t))


# In[ ]:




