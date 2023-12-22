# This is a sample Python script.
import PIL
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import json

from streamlit_lottie import st_lottie




st.set_page_config(page_title="KaiJun Webpage", page_icon=":tada:", layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
st.subheader("Hi, I am KaiJun :basketball:")
st.title("I am a Basketball Player")
st.write(
    "I love playing basketball")
st.write("[Contact Me](https://www.instagram.com/mike.szh/)")
st.write("---") # adds a line across the screen by creating an empty <hr> markdown
left_column, right_column = st.columns(2)
with left_column:
    st.header("What I do")
    st.write("##")  # adds a gap by creating an empty <H2> markdown
    st.write(
            """
            I am a basketball player who:
            - love beating his brother.
            - love challenges.
            - love trying new things.
            - strive to be a better self.

            """
    )

path = "animation.json"
with open(path, "r") as file:
    url = json.load(file)

with right_column:
    st_lottie(url, height=300)

from PIL import Image
size = (480, 343)
firstImage = Image.open('pic 1.jpeg')
firstImage = firstImage.resize(size)

secondImage = Image.open('pic 2.jpeg')
secondImage = secondImage.resize(size)

thirdImage = Image.open('pic 3.jpeg')
thirdImage = thirdImage.resize(size)

fourthImage = Image.open('pic 4.jpeg')
fourthImage = fourthImage.resize(size)


st.write("---")
st.header("My Photos")
st.write("##")
left_column1, right_column1, left_column, right_column = st.columns(4)
with left_column1:
    st.image(firstImage, width=300, use_column_width=True)

with right_column1:
    st.image(secondImage,width=300,use_column_width=True)

with left_column1:
    st.image(thirdImage,width=300,use_column_width=True)

with right_column1:
    st.image(fourthImage,width=300,use_column_width=True)







