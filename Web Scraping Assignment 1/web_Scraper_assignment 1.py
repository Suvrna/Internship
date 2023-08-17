#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


#importing required libraries for web scrapping
from bs4 import BeautifulSoup
import requests


# In[14]:


#Write a python program to display all the header tags from wikipedia.org and make data frame

import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])

df = pd.DataFrame({'Header tags':titles})

df


# In[11]:


#Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) 
#from https://presidentofindia.nic.in/index.php/former-presidents and make data frame.


import pandas as pd
from bs4 import BeautifulSoup
import requests

page=requests.get('https://presidentofindia.nic.in/index.php/former-presidents')
soup = BeautifulSoup(page.content)

namep=soup.find_all(['h3'])
termO=soup.find_all(['h5'])

#dataframes
df = pd.DataFrame({'Name':namep,'Term ofoffice':termO})

df


# In[34]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
#b) Top 10 ODI Batsmen along with the records of their team andrating.
#c) Top 10 ODI bowlers along with the records of their team andrating.


import pandas as pd
from bs4 import BeautifulSoup
import requests

#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
def teamMatchesPoints():
    teamName=[]
    matches=[]
    points=[]
    data=[]
    index=0
   
    page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
    soup = BeautifulSoup(page.content)

    for i in soup.find_all('span',class_="u-hide-phablet"):
        teamName.append(i.text)

    for d in soup.find_all('td',class_="rankings-block__banner--matches"):
        data.append(d.text)
    
    for d in soup.find_all('td',class_="rankings-block__banner--points"):
        data.append(d.text)
    
    for d in soup.find_all('td',class_="table-body__cell u-center-text"):
        data.append(d.text)

    while index < len(data):
        matches.append(data[index])
        index=index+1
        points.append(data[index])
        index=index+1
    
    print(data,"\n",matches,"\n",points)
    #add data in dataframes
   
    df = pd.DataFrame({'Team':teamName,'Matches':matches,'Points':points})
    df.head(10)
   
    print("// function")
    
#b) Top 10 ODI Batsmen along with the records of their team and rating.
def batsmenMatchesPoints():
    btplayer=[]
    btTeam=[]
    btrating=[]

    page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
    soup = BeautifulSoup(page.content)
  
    # for header data starts

    for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
        btplayer.append(i.text.replace("\n",""))
    
    for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
        btTeam.append(i.text.replace("\n",""))

    for i in soup.find_all('div',class_="rankings-block__banner--rating"):
        btrating.append(i.text)

    #print(btplayer,"\n",btTeam,"\n",btrating)

    # for header data ends

    # for table data starts

    for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
        btplayer.append(i.text.replace("\n",""))
    
    for i in soup.find_all('span',class_="table-body__logo-text"):
        btTeam.append(i.text)

    for i in soup.find_all('td',class_="table-body__cell rating"):
        btrating.append(i.text)
 
    df = pd.DataFrame({'Batting player':btplayer,'Team':btTeam,'Rating':btrating})

    # for table data ends

 #   df.drop_duplicates(subset=['Batting player','Team','Rating'])
    df.head(10)

#c) Top 10 ODI bowlers along with the records of their team and rating.
def bowlerMatchesPoints():
    blplayer=[]
    blTeam=[]
    blrating=[]

    page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
    soup = BeautifulSoup(page.content)

    # for header data starts
    for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
        blplayer.append(i.text.replace("\n",""))

    for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
        blTeam.append(i.text.replace("\n",""))

    for i in soup.find_all('div',class_="rankings-block__banner--rating"):
        blrating.append(i.text)

    #print(blplayer,"\n",blTeam,"\n",blrating)

    # for table data starts

    for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
        blplayer.append(i.text.replace("\n",""))
    
    for i in soup.find_all('span',class_="table-body__logo-text"):
        blTeam.append(i.text)

    for i in soup.find_all('td',class_="table-body__cell rating"):
        blrating.append(i.text)
 
    dfBlPlayer = pd.DataFrame({'Bolwing player':blplayer,'Team':blTeam,'Rating':blrating})
    dfBlPlayer.drop_duplicates(subset=['Bolwing player','Team','Rating'])
    dfBlPlayer.head(10)


#calling functions
#print("Top 10 ODI teams in men’s cricket along with the records for matches, points and rating")
#teamMatchesPoints()

#print("Top 10 ODI Batsmen along with the records of their team and rating")
#batsmenMatchesPoints()

print("Top 10 ODI bowlers along with the records of their team and rating")
bowlerMatchesPoints()


# In[52]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

#importing required libraries for web scrapping
import pandas as pd
from bs4 import BeautifulSoup
import requests

teamName=[]
matches=[]
points=[]
data=[]
index=0

page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup = BeautifulSoup(page.content)

for i in soup.find_all('span',class_="u-hide-phablet"):
    teamName.append(i.text)

for d in soup.find_all('td',class_="rankings-block__banner--matches"):
    data.append(d.text)

for d in soup.find_all('td',class_="rankings-block__banner--points"):
    data.append(d.text)
    
for d in soup.find_all('td',class_="table-body__cell u-center-text"):
    data.append(d.text)

while index < len(data):
    matches.append(data[index])
    index=index+1
    points.append(data[index])
    index=index+1

#print(teamName,"\n",matches,"\n",points)

df = pd.DataFrame({'Team':teamName,'Matches':matches,'Points':points})
df.head(10)


# In[51]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#b) Top 10 ODI Batsmen along with the records of their team and rating.

#importing required libraries for web scrapping
import pandas as pd
from bs4 import BeautifulSoup
import requests

btplayer=[]
btTeam=[]
btrating=[]

page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup = BeautifulSoup(page.content)
  
# for header data starts

for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    btplayer.append(i.text.replace("\n",""))
    
for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    btTeam.append(i.text.replace("\n",""))

for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    btrating.append(i.text)

# for header data ends

# for table data starts

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    btplayer.append(i.text.replace("\n",""))
    
for i in soup.find_all('span',class_="table-body__logo-text"):
    btTeam.append(i.text)

for i in soup.find_all('td',class_="table-body__cell rating"):
    btrating.append(i.text)

#print(btplayer,"\n",btTeam,"\n",btrating)

df = pd.DataFrame({'Batting player':btplayer,'Team':btTeam,'Rating':btrating})

# for table data ends

df.drop_duplicates(subset=['Batting player','Team','Rating'])
df.head(10)


# In[54]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#c) Top 10 ODI bowlers along with the records of their team and rating.

blplayer=[]
blTeam=[]
blrating=[]

page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup = BeautifulSoup(page.content)

# for header data starts
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    blplayer.append(i.text.replace("\n",""))

for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    blTeam.append(i.text.replace("\n",""))

for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    blrating.append(i.text)

# for table data starts

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    blplayer.append(i.text.replace("\n",""))
    
for i in soup.find_all('span',class_="table-body__logo-text"):
    blTeam.append(i.text)

for i in soup.find_all('td',class_="table-body__cell rating"):
    blrating.append(i.text)

#print(blplayer,"\n",blTeam,"\n",blrating)
dfBlPlayer= pd.DataFrame({'Bolwing player':blplayer,'Team':blTeam,'Rating':blrating})
dfBlPlayer.drop_duplicates(subset=['Bolwing player','Team','Rating'])
dfBlPlayer.head(10)


# In[55]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

#importing required libraries for web scrapping
import pandas as pd
from bs4 import BeautifulSoup
import requests

teamName=[]
matches=[]
points=[]
data=[]
index=0

page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup = BeautifulSoup(page.content)

for i in soup.find_all('span',class_="u-hide-phablet"):
    teamName.append(i.text)

for d in soup.find_all('td',class_="rankings-block__banner--matches"):
    data.append(d.text)

for d in soup.find_all('td',class_="rankings-block__banner--points"):
    data.append(d.text)
    
for d in soup.find_all('td',class_="table-body__cell u-center-text"):
    data.append(d.text)

while index < len(data):
    matches.append(data[index])
    index=index+1
    points.append(data[index])
    index=index+1

#print(teamName,"\n",matches,"\n",points)

df = pd.DataFrame({'Team':teamName,'Matches':matches,'Points':points})
df.head(10)


# In[56]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#B. Top 10 women’s ODI Batting players along with the records of their team and rating.

#importing required libraries for web scrapping
import pandas as pd
from bs4 import BeautifulSoup
import requests

btplayer=[]
btTeam=[]
btrating=[]

page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup = BeautifulSoup(page.content)
  
# for header data starts

for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    btplayer.append(i.text.replace("\n",""))
    
for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    btTeam.append(i.text.replace("\n",""))

for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    btrating.append(i.text)

# for header data ends

# for table data starts

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    btplayer.append(i.text.replace("\n",""))
    
for i in soup.find_all('span',class_="table-body__logo-text"):
    btTeam.append(i.text)

for i in soup.find_all('td',class_="table-body__cell rating"):
    btrating.append(i.text)

#print(btplayer,"\n",btTeam,"\n",btrating)

df = pd.DataFrame({'Batting player':btplayer,'Team':btTeam,'Rating':btrating})

# for table data ends

df.drop_duplicates(subset=['Batting player','Team','Rating'])
df.head(10)


# In[58]:


#Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

blplayer=[]
blTeam=[]
blrating=[]

page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup = BeautifulSoup(page.content)

# for header data starts
for i in soup.find_all('div',class_="rankings-block__banner--name-large"):
    blplayer.append(i.text.replace("\n",""))

for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    blTeam.append(i.text.replace("\n",""))

for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    blrating.append(i.text)

# for table data starts

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    blplayer.append(i.text.replace("\n",""))
    
for i in soup.find_all('span',class_="table-body__logo-text"):
    blTeam.append(i.text)

for i in soup.find_all('td',class_="table-body__cell rating"):
    blrating.append(i.text)

#print(blplayer,"\n",blTeam,"\n",blrating)
dfBlPlayer= pd.DataFrame({'All-Rounder':blplayer,'Team':blTeam,'Rating':blrating})
dfBlPlayer.drop_duplicates(subset=['All-Rounder','Team','Rating'])
dfBlPlayer.head(10)


# In[75]:


#Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
#i) Headline ii) Time iii) News Link

#importing required libraries for web scrapping
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

headData=[]
timeData=[]
linkData=[]

page=requests.get('https://www.cnbc.com/world/?region=world')
soup = BeautifulSoup(page.content)

# for data starts
for i in soup.find_all('a',attrs={'href': re.compile("https://")},class_="LatestNews-headline"):
    headData.append(i.text)
    linkData.append(i.get('href')) 

for i in soup.find_all('time',class_="LatestNews-timestamp"):
    timeData.append(i.text)

#print(headData,"\n",timeData, "\n", linkData)
dfHeadNews= pd.DataFrame({'Headline':headData,'Time':timeData,'News Link':linkData})
dfHeadNews


# In[92]:


#Write a python program to scrape the details of most downloaded articles 
#from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame-
#i) Paper Title ii) Authors iii) Published Date iv) Paper URL

#importing required libraries for web scrapping
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

tData=[]
authData=[]
timeData=[]
linkData=[]

page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
soup = BeautifulSoup(page.content)

# for data starts
for i in soup.find_all('a',attrs={'href': re.compile("https://")},class_="sc-5smygv-0 fIXTHm"):
    tData.append(i.text)
    linkData.append(i.get('href')) 

for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    authData.append(i.text) 

for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    timeData.append(i.text) 
    
#print(tData,"\n",linkData,"\n",authData,"\n",timeData)

dfdownArticle= pd.DataFrame({'Paper Title':tData,'Authors':authData,'Published Date':timeData,'Paper URL':linkData})
dfdownArticle


# In[ ]:




