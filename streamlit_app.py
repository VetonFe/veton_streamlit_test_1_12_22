import streamlit as st

def convert_list(user_text):
    '''
    This function takes a text input from the user
    it seperates the text in words, it returns
    a list containing those words
    '''
    text_list=user_text.split()
    return text_list

def convert_upper(text_list):
    '''
    This function takes the return list of convert_list
    function as input and converts all the words in upper case,
    it returns a new list containing those words
    '''
    new_text_list=[]
    for item in text_list:
        new_item=item.upper()
        new_text_list.append(new_item)
    return new_text_list

def count(text_list):
    '''
    This function takes the return list of convert_list
    function as input, it returns the number of elements in it
    '''
    return len(text_list)

user_text=st.text_input('Enter input: ')
text_list=convert_list(user_text)

if st.button('Return List'):
    st.write(convert_list(user_text))

if st.button('Upper'):
    st.write(convert_upper(text_list))

if st.button('Print Count'):
    st.write(count(text_list))