#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st


# In[6]:


#to find largest of 3 numbers
def largest_number(a,b,c):
    return max(a,b,c)


# In[ ]:


st.title('Largest Number Finder')
num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')
num3 = st.number_input('Enter the third number:')


if st.button('Find Largest Number'):
    largest_num = largest_number(num1, num2, num3)
    st.success(f'The largest number is: {largest_num}')

