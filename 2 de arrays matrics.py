# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:48:26 2020

@author: HASSAN ENTERPRISES
"""

        
#=========================================================================
row=int(input("enter the number of rows:"))
column=int(input("enter the number of columns:"))
mat=[]
for i in range(row):
    mat.append([0]*column)
#print(mat)    
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j],end='')
    print()
#=========================================================================
row=int(input("enter the number of rows:"))
column=int(input("enter the number of columns:"))
mat=[]
for i in range(row):
    mat.append([0]*column)
print("enter the elements:")    
#print(mat)
for i in range(len(mat)):
    for j in range(len(mat[0])):
            mat[i][j]=input()   
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j],end='')
    print()
#==========================================================================
23+19+31//3    
abs(54-57)     
54-57
#============================================================================


  


