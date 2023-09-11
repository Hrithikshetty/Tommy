
bubble sort is [2, 5, 6, 7, 9]
enter the first elem 2
enter the second elem 10
2
* 
* * 
* * * 
* * 
* 
#bubble sort
def bsort(n):
 for i in range(len(n)-1,0,-1):
 for j in range(i):
 if n[j]>n[j+1]:
# temp=n[j]
# n[j]=n[j+1]
# n[j+1]=temp
 (n[j],n[j+1])=(n[j+1],[j])
 
num=[5,7,9,2,6]
bsort(num)
print("bubble sort is ",num)
#gdc
n=int(input("enter the first elem "))
m=int(input("enter the second elem "))
a=0
for i in range(1,m):
 if n%i==0 and m%i==0:
 a=i
print(a)
 
#patten
n=3
for i in range(1,n+1):
 for j in range(1,i+1):
 print("*",end=" ")
 print()
for i in range(n-1,0,-1):
 for j in range(1,i+1):
 print("*",end=" ")
 print()
In [16]:
In [13]:
enter the number 10
fibonacci series is 0 1 1 2 3 5 8 13 21 34 
the array is
the array index 0 is 10
the array index 1 is 5
the array index 2 is 42
the array index 3 is 69
enter the index:2
the index of element is : 42
#fibonacci series
num=int(input("enter the number "))
n1,n2=0,1
print("fibonacci series is",n1,n2,end=' ')
for i in range(2,num):
 n3=n1+n2
 n1=n2
 n2=n3
 print(n3,end=' ')
#create an array of 5 integers and display the array items. Access individual elements 
a=[10,5,42,69]
print("the array is")
for i in range(len(a)):
 print(f"the array index {i} is",a[i])
index=int(input("enter the index:"))
if 0<=index<len(a):
 element=a[index]
 print("the index of element is : ",element)
else:
 print("invalid index")
 
In [12]:
In [16]:
In [21]:
Enter the key to be searcehd100
not found
Enter the key to be searcehd100
not found
[10, 20, 30, 40, 60]
# 4 Write a Python program to demonstrate sequential search.
a=[10,20,30,20,40]
key=int(input("Enter the key to be searcehd"))
found=0
c=[]
for i in range(len(a)):
 if key==a[i]:
 found+=1
 c.append(i)
if found!=0:
 print("the array elements is ",[c[i] for i in range(found)])
else:
 print("not found")
a=[10,20,30,20,40]
key=int(input("Enter the key to be searcehd"))
f=0
for i in range(len(a)):
 if key==a[i]:
 f=1
if f==1:
 print("found")
else:
 print("not found")
a=[10,30,20,40,60]
n=5
for i in range(n-1):
 for j in range(n-i-1):
 if a[j]>a[j+1]:
 (a[j],a[j+1])=(a[j+1],a[j])
 
print(a)
In [29]:
In [ ]:
* 
* * 
* * * 
* * 
* 
for i in range(1,4):
 for j in range(i):
 print("*",end=" ")
 print() 
for i in range(2,0,-1):
 for j in range(i):
 print("*",end=" ")
 print()