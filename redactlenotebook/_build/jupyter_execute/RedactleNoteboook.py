#!/usr/bin/env python
# coding: utf-8

# # Setup

# In[1]:


#!pip install wikipedia ipywidgets


# In[ ]:





# In[2]:


import wikipedia
import ipywidgets
import re
import textwrap
import urllib


# In[3]:


name = urllib.request.urlopen('https://randomincategory.toolforge.org/?category=All%20Wikipedia%20level-5%20vital%20articles&server=en.wikipedia.org&cmnamespace=&cmtype=&returntype=subject').read(500).decode().split('title>')[1].split(' - Wikipedia')[0]
content = wikipedia.page(name).content


# In[4]:


def print_redacted(new_string,count_to_word_dict):
  string_to_print = ''
  delims=['\n',r'===',r'==',r'.',r',',r'(',r')',r'[',r']',r'<',r'>',r'"',r':',r';',r'-',r'/',r'–',r'=',r'%']
  for word in re.split(r'([ |\n|=|.|,|(|)|[|]|<|>|"|:|;|-|/|–|%])',new_string):
    if type(word)==str:
      if word in delims:
        string_to_print += word
      elif word in count_to_word_dict.keys():
        if len(count_to_word_dict[word])>0:
          string_to_print += count_to_word_dict[word][0]+' '
      else:
        pass
  print(string_to_print)


word_to_count_dict = {}
count_to_word_dict = {}
count_the_word_dict = {}
new_string =''
count = 9897098660698
delims=['\n',r'.',r',',r'(',r')',r'[',r']',r'<',r'>',r'"',r':',r';',r'-',r'/',r'–',r'=',r'%',r'',r' ']
words = [x for x in re.split(r'([ |\n|=|.|,|(|)|[|]|<|>|"|:|;|-|/|–|%])',name+' \n\n '+content)]
for word in words:
  if type(word)==str:
    word = word.lower()
    if word in delims:
      if word not in ['',' ']:
        new_string += word
    elif word not in word_to_count_dict.keys():
      word_to_count_dict[word]=str(count)
      count_to_word_dict[str(count)]=['-'*len(word),word]
      new_string += str(count)+' '
      count += 1
      count_the_word_dict[word]=1
    else:
      new_string += word_to_count_dict[word]+' '
      count_the_word_dict[word]+=1

new_string = textwrap.fill(new_string,break_long_words=False,width=200,replace_whitespace=False,
                           drop_whitespace=False, break_on_hyphens=False)
tried = []
name_list = re.split(r'[ |\n|===|==|.|,|(|)|[|]|<|>|"|:|;|-|/|–|=|%|]{1,3}',name)
name_list = [x.lower() for x in name_list]

starting_guesses = ['a','an','is','the','of']
for eachguess in starting_guesses:
  try:
    tried.append(eachguess)
    count = word_to_count_dict[eachguess]
    count_to_word_dict[count]=count_to_word_dict[count][1:]
  except:
    pass


# In[5]:


guess = ipywidgets.Text(value='the')


# # The Game

# In[6]:


#@title Default title text
thisguess = guess.value.lower()
if thisguess in tried:
  print('already tried, here is what you tried already:',textwrap.fill(', '.join(tried)))
  print_redacted(new_string,count_to_word_dict)
elif thisguess not in word_to_count_dict.keys():
  print('Nope')
  print_redacted(new_string,count_to_word_dict)
  tried.append(thisguess)
else:
  tried.append(thisguess)
  if thisguess in name_list:
    name_list.remove(thisguess)
  if len(name_list)>0:
    count = word_to_count_dict[thisguess]
    count_to_word_dict[count]=count_to_word_dict[count][1:]
    print(f"{thisguess} appears {count_the_word_dict[thisguess]} times")
  else:
    print('Hooray! \n')
    for k,v in count_to_word_dict.items():
      if len(v)>1:
        count_to_word_dict[k]=v[1:]
  print_redacted(new_string,count_to_word_dict)

guess


# # Answers/Give up?

# In[7]:


#Give up? Uncomment(remove the # from) the line below and run 
#print(name)


# In[8]:


#print(tried)

