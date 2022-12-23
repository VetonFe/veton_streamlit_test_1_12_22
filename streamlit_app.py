import streamlit as st

# Ky funksion merr si input nje fjali nga useri
# dhe e bon ndarjen e fjalise ne fjale,
# bon return nje liste me fjalet e fituara

def convert_list(user_text):
    text_list=user_text.split()
    return text_list

# Ky funksion merr si input listen return te funksionit
# convert_list dhe i shendrron fjalet ne upper case,
# bon return nje liste me ato fjale

def convert_upper(text_list):
    new_text_list=[]
    for item in text_list:
        new_item=item.upper()
        new_text_list.append(new_item)
    return new_text_list

# Ky funksion merr si input listen return te funksionit
# convert_list dhe e bon return numrin e elementeve ne te

def count(text_list):
    return len(text_list)

# Ne user_text ruhet fjalia e userit

user_text=st.text_input('Enter input: ')
# Ne text_list ruhet returni i funksionit convert_list
text_list=convert_list(user_text)

if st.button('Return List'):
    st.write(convert_list(user_text))

if st.button('Upper'):
    st.write(convert_upper(text_list))

if st.button('Print Count'):
    st.write(count(text_list))