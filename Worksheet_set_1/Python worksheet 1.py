#!/usr/bin/env python
# coding: utf-8

# In[9]:


#11. Write a python program to find the factorial of a number.

factorial = 1

# enter number for factor
num = int(input("Enter a number: "))

if num < 0:
   print("Sorry, factorial not possible.")
elif num == 0:
   print("The factorial of 0 is always 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of ",num,"is =",factorial)


# In[11]:


# 12. Write a python program to find whether a number is prime or composite
num = int(input("Enter a number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime")
            break
    else:
        print(num, "is a prime")
elif num == 0 or 1:
    print(num, "is a neither prime nor composite.")
else:
    print(num, "is a composite number")


# In[3]:


# Python program to check if a string is palindrome or not

inputStr=input("Enter a string : ")
n = -1
flag = 0
for i in inputStr:
    if i != inputStr[n]:
        flag = 1
        break
    n = n - 1
if flag == 1:
    print("No, Not a palindrome string ")
else:
    print("Yes, it is palindrome string")


# In[6]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides
 
def getThirdSideRightAngleTrngle(side1, side2):
    s3 = (((side1 * side1) + (side2 * side2))**(1/2));
    return s3;
  
side1 = int(input("Enter a side 1 : "))
side2 = int(input("Enter a side 2 : "))
  
print("The third side of right-angled triangle is ", getThirdSideRightAngleTrngle(side1, side2));


# In[9]:


#15. Write a python program to print the frequency of each of the characters present in a given string

inputStr=input("Enter a string : ")

strDic = {}
 
for keys in inputStr:
    strDic[keys] = strDic.get(keys, 0) + 1
 
print("character : count in entered string is : \n" + str(strDic))


# In[ ]:




