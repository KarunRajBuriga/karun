#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium ')


# In[2]:


# importing required from selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pandas as pd


# In[3]:


browser = webdriver.Edge()
browser.get('https://datatables.net/')     #launch the browser in this url
browser.maximize_window()


# In[6]:


action=ActionChains(browser)
Click = browser.find_element_by_xpath('//*[@id="example_length"]/label/select')
action.context_click(Click).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER) .perform()


# In[12]:


#(!No Need to execute)
#Getting all the tables data
e_data= browser.find_elements_by_xpath('//*[@id="example"]/tbody/tr/td')
#iterating to each column and setting display= block if ‘none’ by using extension script
for edata in e_data:
    Display = edata.value_of_css_property('display')
    if display == 'none':
        Browser.execute_script("arguments[0].style.display='block'; ",edata)


# In[13]:


name=browser.find_elements_by_xpath('//tbody/tr/td[1]')
posit=browser.find_elements_by_xpath('//tbody/tr/td[2]')
office=browser.find_elements_by_xpath('//tbody/tr/td[3]')
age=browser.find_elements_by_xpath('//tbody/tr/td[4]')
date=browser.find_elements_by_xpath('//tbody/tr/td[5]')
salary=browser.find_elements_by_xpath('//tbody/tr/td[6]')
data=[]


# In[14]:


i=0
while i<(len(office)):
    temporary_data={'name':name[i+1].text,
                'posit':posit[i+1].text,
                'office':office[i].text,
                'age':age[i].text,
                'date':date[i].text,
                'salary':salary[i].text}
    data.append(temporary_data)
    i+=1
df_data = pd.DataFrame(data) 


# In[15]:


df_data


# In[16]:


browser.close()


# In[17]:


df_data.to_csv('Scrapping data.csv',index=False)


# In[ ]:




