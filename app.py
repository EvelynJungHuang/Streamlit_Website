from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Evelyn's Webpage", page_icon="♥" ,layout="wide")
#icon can be found on https://www.webfx.com/tools/emoji-cheat-sheet/

def load_lottieurl(url):
   r = requests.get(url)
   if r.status_code !=200:
      return None
   return r.json()

#use local CSS

def local_CSS(file_name):
    with open(file_name) as f:
       st.markdown((f'<style>{f.read()}</style>'),unsafe_allow_html=True)

local_CSS("/Users/evelynhuang/github/Streamlit_Website/style/style.css")

#----Load assets---
lottie_animation=load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_seowcwyx.json")
img_earthqulke=Image.open("/Users/evelynhuang/github/Streamlit_Website/images/921_earthquake_v2.JPG")
img_assessment=Image.open("/Users/evelynhuang/github/Streamlit_Website/images/assessment.png")
img_therapy=Image.open("/Users/evelynhuang/github/Streamlit_Website/images/therapy.png")
img_analysis=Image.open("/Users/evelynhuang/github/Streamlit_Website/images/analysis.png")

#---Header section
with st.container():
    text_column,animation_column = st.columns((2,1))
    with text_column:
        st.subheader("Hi, I am Evelyn :wave:")
        st.title("A Clinical Psychologist from Taiwan")
        st.subheader("I am  passionate about experiencing new things and discovering interesting psychological perspectives in everyday life ")
    with animation_column:
       st_lottie(lottie_animation,width=350,key="animation")
#---Background section
with st.container():
    st.write("---")
    st.subheader("Education Background and Work Experience")
    left_columm, right_column = st.columns(2)
    with left_columm:
       st.write("🎓**Education Background:**")
       st.write("National Taiwan University")
       st.write("Master of Science, Major in Clinical Psychology")
    with right_column:
       st.write("💼 **Work Experience:**")
       st.write("Clinical psychologist in China Medical University Hsinchu Hospital (2023.02-)")
       st.write("Research Assistant at Taiwan Academy of Psychiatry and the Law (2021.11-2023.01) ")

#---My Research
with st.container():
    st.write("---")
    st.header("My Research:")
    image_columm, text_column = st.columns((1,2))
    with image_columm:
       st.image(img_earthqulke)
    with text_column:
       st.subheader("""
       Trajectories of PTSD Symptoms, Social Acknowledgment, Disaster Experience Disclosure, and Posttraumatic Growth: A 20-year Follow-up Study of the 921 Chi-Chi Earthquake
       """)
       st.write("The detailed information about this study is still being arranged.")
#---My Expertise
with st.container():
   st.write("---")
   st.header("My Expertise:")
   st.write("##")
   left_column, middle_column,right_columm  = st.columns(3)
   with left_column:
       st.image(img_assessment,width=200)
       st.subheader("Psychological Assessment")
   with middle_column:
       st.image(img_therapy,width=200)
       st.subheader("Psychological Therapy")
   with right_columm:
       st.image(img_analysis,width=200)
       st.subheader("Mental Health Related Data Analysis")
#---contact-----
with st.container():
   st.write("---")
   st.header("Get In Touch With Me!")
   st.write("##")

   #Documentation: https://formsubmit.co/
   contact_form = """
    <form action="https://formsubmit.co/evelyn.develop@email.com" method="POST">
        <input type="hidden" name="_captha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="message" placeholder= "your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
   """
   left_columm, right_column=st.columns(2)
   with left_columm:
      st.markdown(contact_form,unsafe_allow_html=True)
   with right_column:
      st.empty()