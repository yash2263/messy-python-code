# ORIGINAL messy script (kept unchanged for comparison)
import os,sys,math
l=[]
def f(x):
 t=0
 for i in range(0,len(x)):
     t=t+x[i]
 a=t/len(x)
 return a
def g(x):
  m=x[0]
  for i in x:
   if i>m: m=i
  return m
def h(x):
    m=x[0]
    for i in x:
        if i<m:m=i
    return m
n=int(input("how many students"))
for i in range(n):
  s=input("name")
  mk=int(input("marks"))
  l.append([s,mk])
mm=[]
for i in l: mm.append(i[1])
print("avg",f(mm))
print("max",g(mm))
print("min",h(mm))
for i in l:
  if i[1]>=90: print(i[0],"A")
  elif i[1]>=75: print(i[0],"B")
  elif i[1]>=50: print(i[0],"C")
  else: print(i[0],"F")
