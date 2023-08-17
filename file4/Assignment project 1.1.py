#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 10


# In[8]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re
def stringMatch(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'String match!'
        else:
                return('String Not matched!')

inputData=input("Enter text :")
print(stringmatch(inputData))


# In[10]:


#Question 12- Write a Python program where a string will start with a specific number. 

import re

def matchWithNm(string):
    text = re.compile(r"^6")
    if text.match(string):
        return 'String start with 6 !'
    else:
        return('String Not starting with 6!')

inputData=input("Enter text :")
print(matchWithNm(inputData))


# In[20]:


#Question 13- Write a Python program to remove leading zeros from an IP address

import re
ip = "123.08.04.101"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[28]:


#Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
#Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
#Expected Output- August 15th 1947
#Note- Store given sample text in the text file and then extract the date string asked format.

import re
    
def findMonthDate(string):
        
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)
        
    if match == None: 
        print ("Not a valid date")
        return
    
    print ("Given Data: %s" % (match.group()))
    print ("Month: %s" % (match.group(1)))
    print ("Day: %s" % (match.group(2)))
    
        
# Driver Code
findMonthDate("Jun 24")
print("")
findMonthDate("I was born on June 24")


# In[26]:


#Question 15- Write a Python program to search some literals strings in a string.   
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'

import re

inputData = [ 'fox', 'dog', 'horse' ]

subData = 'The quick brown fox jumps over the lazy dog.'

for text in inputData:
    
    if re.search(text,  subData):
        print('Found "%s" " ->' % (text),)
    else:
        print('No matching for "%s" " ->' % (text),)
        


# In[17]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox'

import re

inputData=input("Enter text :")
#inputData = 'The quick brown fox jumps over the lazy dog.'

subData=input("Enter sub text :")
#subData = 'fox'

match = re.search(subData, inputData)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % (match.re.pattern, match.string, s, e))


# In[16]:


#Question 17- Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'
#Pattern : 'exercises'.

import re

inputData=input("Enter text :")

subData=input("Enter sub text :")

for match in re.findall(subData, inputData):
    print('Found "%s"' % match)


# In[24]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

import re

inputData=input("Enter text :")

subData=input("Enter sub text :")

for match in re.finditer(subData, inputData):
    s = match.start()
    e = match.end()
    print('"%s" at %d:%d' % (inputData[s:e], s, e))


# In[29]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

import re

def DDMMYYYY_date_format(dte):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dte)

inputDate=input("Enter date :")    

print("Entered date in YYY-MM-DD Format: ",inputDate)

print("New date in DD-MM-YYYY Format: ",DDMMYYYY_date_format(inputDate))


# In[35]:


#Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. 
#The use of the re.compile() method is mandatory.

def is_decimal(num):
    import re
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)

inputNum=input("Enter numbers :")

print(str(is_decimal("12.34")))
print(str(is_decimal("1.234")))


# In[38]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string.

import re

inputData=input("Enter text :")

for m in re.finditer("\d+", inputData):
    print(m.group(0))
print("Position:", m.start())


# In[42]:


#Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
#Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
#Expected Output: 950

import re

inputData=input("Enter text :")

occ = re.findall("\d+", inputData)

numList = map(int, occ)

print(max(numList))


# In[45]:


#Question 23- Create a function in python to insert spaces between words starting with capital letters.
#Sample Text: “RegularExpressionIsAnImportantTopicInPython"
#Expected Output: Regular Expression Is An Important Topic In Python

import re

def addSpaceInWords(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

inputData=input("Enter text :")
print(addSpaceInWords(inputData))


# In[2]:


#Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

import re

def isTextUpper(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a text!'
        else:
                return('No upper case matched!')

inputData=input("Enter text :")
print(isTextUpper(inputData))       
            


# In[6]:


#Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
#Sample Text: "Hello hello world world"
#Expected Output: Hello hello world

def removeDuplicateWord(inputText):
    wrd = inputText.split()
    tmpWrd = []
    for w in wrd:
        if w not in tmpWrd:
            tmpWrd.append(w)
    return ' '.join(tmpWrd)



inputData = "Hello hello world world"
print("Original String:")
print(inputData)
print("\nAfter removing duplicate words from the said string:")
print(removeDuplicateWord("Hello hello world world"))


# In[7]:


#Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

import re
def isAlphaNum(tempText):
   if(re.match("^[a-zA-Z0-9]*$", tempText) != None):
     return True
   return False


inputData=input("Enter text :")
print(isAlphaNum(inputData))   


if(isAlphaNum(inputData) == True):
   print("Entered string is a alphanumeric string")
else:
   print("Entered string is not a alphanumeric string")
 


# In[20]:


#Question 27-Write a python program using RegEx to extract the hashtags.
#Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
#Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

import re

def removeHashtag(text):
    regex = "#(\w+)"
    hashtag=""
    hashtag_list = re.findall(regex, text)
    for hashChar in hashtag_list:
        hashtag = hashtag + " "+ hashChar
    print(hashtag)
    
inputData=input("Enter text :")
print(removeHashtag(inputData)) 


# In[24]:


#Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
#The use of the re.compile() method is mandatory.
#Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 
#4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#Expected Output:  following example creates ArrayList a capacity elements. 
#4 elements added ArrayList ArrayList trimmed accordingly.

import re

def find24CharInWords(text):
    regPattern = re.compile(r"\b\w{2,4}\b")
    outputText=regPattern.sub('', text)
    #outputText=regPattern.findall(inputData)
    return outputText

inputData=input("Enter text :")
print(find24CharInWords(inputData))


# In[ ]:




