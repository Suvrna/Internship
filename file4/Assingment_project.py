#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
#Sample Text- 'Python Exercises, PHP exercises.'
#Expected Output: Python:Exercises::PHP:exercises:

import re
inputData=input("Enter text :")
print(re.sub("[ ,.]", ":", inputData))


# In[4]:


#Question 2-  Write a Python program to find all words starting with 'a' or 'e' in a given string.

#import re
inputData=input("Enter text :")

aewords = re.findall("[ae]\w+", inputData)
print(aewords)


# In[14]:


#Question 3- Create a function in python to find all words that are at least 4 characters long in a string. 
#The use of the re.compile() method is mandatory.

import re

def findlst4CharLongWords(str1):
    regPattern = re.compile(r"\b\w{4,}\b")
    outputText=regPattern.findall(inputData)
    return outputText

inputData=input("Enter text :")
print(findlst4CharLongWords(inputData))        


# In[13]:


#Question 4- Create a function in python to find all three, four, and five character words in a string. 
#The use of the re.compile() method is mandatory.

import re

def find345CharInWords(str1):
    regPattern = re.compile(r"\b\w{3,5}\b")
    outputText=regPattern.findall(inputData)
    return outputText

inputData=input("Enter text :")
print(find345CharInWords(inputData))


# In[53]:


#Question 5- Create a function in Python to remove the parenthesis in a list of strings. 
#The use of the re.compile() method is mandatory.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output:
#example.com
#hr@fliprobo.com
#github.com
#Hello Data Science World
#Data Scientist

import re

str1=""
s=""
items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for item in items:
    str1= re.sub(r" ?\([^)]+\)", "", item)
#    print(str1)
    s=s+"\n"+str1       

print(s)


# In[ ]:


import re

outputText=""
mystring=["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

regPattern = re.compile(r" ?\([^)]+\)")
outputText=regPattern.findall(str(mystring))
    
print(outputText)


# In[ ]:


#Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
#Note- Store given sample text in the text file and then to remove the parenthesis area from the text.

import re

storeText = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

for text in storeText:
    print(re.sub(r" ?\([^)]+\)", "", text))


# In[57]:


#Question 7- Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”
#Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

import re

inputData=input("Enter text :")

#inputData = "ImportanceOfRegularExpressionsInPython"

print(re.findall('[A-Z][^A-Z]*', inputData))


# In[ ]:


#Question 8- Create a function in python to insert spaces between words starting with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

import re
def word_number_space(str1):
  return re.sub(r"(\w)([0-9])", r"\1 \2 ", str1)

inputData=input("Enter text :")

print(word_number_space(inputData))


# In[ ]:


#Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

import re

def Capitalword_number_space(str1):
  return re.sub(r"(\W)([0-9])", r"\1 \2 ", str1)

inputData=input("Enter text :")
print(Capitalword_number_space(inputData))


