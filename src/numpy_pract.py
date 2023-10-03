# -*- coding: utf-8 -*-
"""numpy_practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fw55ImnLyIJy5TbK1iUqQADdcNymgTU4
"""

import numpy as np

#creating a list

a = [1,"one",2,"two",3,"three"]
#We can access each element using a square bracket as follows:
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
print("a[5]:", a[5])

# list can easily change into array by numpy
a = np.array([0,1,2,3,4,5])
a

# check type of the element
print(type(a))
a.dtype

#for checking version of numpy library
print(np.__version__)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
print(arr[:2])
print(arr[0:])
print(arr[1:4:])

select = np.array([0, 2, 3, 4])
select
print(select.ndim)
print(select.shape)
print(select.size)

##Numpy Statistical Functions

#creating a list by using numpy array
a = np.array([1, -1, 1, -1])

#calculating mean
mean = a.mean()
mean

# for calculation standard deviation
sd = a.std()
sd



#calculating min values
minn = a.min()
minn
#calculating max values
maxx = a.max()
maxx

#performing addition operation on numpy
u = np.array([2,3,8,4])
v = np.array([4,2,3,4])
a = np.add(u,v)
print("Addition:",a)

s = np.subtract(u,v)
print("Subtraction:",s)

m = np.multiply(u,v)
print("Multiplication:",m)

d = np.divide(u,v)
print("Division:",d)

np.dot(u,v)

#Mathematical Functions

np.pi
# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])
y = np.sin(x)
y

np.linspace(-2, 2, num=5)

x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x,y)

#QUIZ

u = np.array([1, 0])
v = np.array([0, 1])
S = np.subtract(u,v)
S

z = np.array([2, 4])
-2*z

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])

a*b

# Commented out IPython magic to ensure Python compatibility.
# Import the libraries

import time
import sys
import numpy as np

import matplotlib.pyplot as plt
# %matplotlib inline

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

a = np.array([1,0])
b = np.array([0, 1])

Plotvec2(a,b)
print("Dot product:", np.dot(a,b))

a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

