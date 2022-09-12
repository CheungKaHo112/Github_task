#!/usr/bin/env python
# coding: utf-8

# In[50]:


import os
import requests
import re
from bs4 import BeautifulSoup


# In[51]:


def get_page():
    global url

    # Code here - Ask the user to input "Enter url of a medium article: " and collect it in url
    url = input("Enter url of a medium article: ")
    # Code ends here

    # handling possible error
    if not re.match(r'https?://medium.com/',url):
        print('Please enter a valid website, or make sure it is a medium article')
        sys.exit(1)

    # Code here - Call get method in requests object, pass url and collect it in res
    res = requests.get(url)
    # Code ends here

    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

# function to remove all the html tags and replace some with specific strings
def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub('\<(.*?)\>', '', text)
    return text


def collect_text(soup):
    text = f'url: {url}\n\n'
    para_text = soup.find_all('p')
    print(f"paragraphs text = \n {para_text}")
    for para in para_text:
        text += f"{para.text}\n\n"
    return text

# function to save file in the current directory
def save_file(text):
    if not os.path.exists('./scraped_articles'):
        os.mkdir('./scraped_articles')
    name = url.split("/")[-1]
    print(name)
    fname = f'scraped_articles/{name}.txt'

    # Code here - write a file using with (2 lines)
    with open('./scraped_articles/test1.txt', 'w') as file:
        file.write(text)
    # Code ends here

    print(f'File saved in directory {fname}')


# In[52]:


text = clean(collect_text(get_page()))
save_file(text)


# In[ ]:




