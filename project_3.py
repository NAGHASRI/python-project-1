# -*- coding: utf-8 -*-
"""project 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fBDKFA-D0cS-aYxWiJa46T8xLsq5QWuD
"""

l=[23,1,4,5,6,45,7,8,82]
even=[]
odd=[]
for i in l:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print("even list is",even)
print("odd list is",odd)