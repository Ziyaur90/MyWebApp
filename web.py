import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2=st.columns(2)


with col1:
    st.image("images/MyPic.jpg")

with col2:
    st.title("Ziyaur Rahman")
    content = """ My name is Ziyaur Rahman. 
    I have total 9 years of experience as a Software Quality Assurance Engineer. 
    Currently I am working for Wipro Technology. This is my first application. Which I have developed using Python. 
    My hobby is to learn Python as it more demanding language 
    in software industry now a days """
    st.info(content)

content2 = """Hello Everyone, Thank you for visiting my website. Hope you learnt Well"""

st.write(content2)

col3, col_empty, col4 = st.columns([1.5, .5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[SourceCode]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.title(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[SourceCode]({row['url']})")


