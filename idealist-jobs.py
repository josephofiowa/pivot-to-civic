
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from math import ceil
import pandas as pd


# In[2]:


driver = webdriver.Chrome()
driver.get("https://www.idealist.org/en/?functions=COMMUNICATIONS&functions=DATABASE_ADMINISTRATION&functions=GRAPHIC_DESIGN&functions=TECHNOLOGY_IT&type=JOB")
sleep(1)
html = driver.page_source
driver.close()


# In[3]:


soup = BeautifulSoup(html, "lxml")


# In[4]:


results = int(soup.find("p", attrs={"class":"text-center search-results-count"}).text.split(" ")[0])
pages = ceil(results/20)


# In[5]:


title = []
link = []
for n in range(1,pages+1):
    driver = webdriver.Chrome()
    driver.get("https://www.idealist.org/en/?functions=COMMUNICATIONS&functions=DATABASE_ADMINISTRATION&functions=GRAPHIC_DESIGN&functions=TECHNOLOGY_IT&page="+str(n)+"&type=JOB")
    sleep(1)
    html = driver.page_source
    for post in soup.find_all("a", attrs={"data-qa-id":"search-result-link"}, href=True):
        title.append(post.text)
        link.append("https://www.idealist.org/" + post['href'])
    driver.close()


# In[6]:


jobs = pd.DataFrame({'title': title,
     'link': link,
    })


# In[7]:


jobs.to_csv("jobs.csv")

