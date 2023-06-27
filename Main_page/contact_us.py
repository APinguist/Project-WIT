import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_view():    
    
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # ---- LOAD ASSETS ----
    lottie_contact_us = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_budjbe8f.json") 

        # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.markdown("<h1 style='text-align: center; color: white;'>Get In Touch With Us!</h1>", unsafe_allow_html=True)
        st.write("##")        
        st.write("##")
        
        # Form Submit
        contact_form = """
        <form action="https://formsubmit.co/audrey.carissa01@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>

        </form>
        """

        left_column, right_column = st.columns([3, 2])
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_contact_us, height=300, speed=0.8)
            
        st.markdown(
        """
            Fitur ini menggunakan [FormSubmit](https://formsubmit.co/) sehingga Anda akan diminta untuk memverifikasi email Anda
            untuk menggunakannya
        """,  unsafe_allow_html=True)


            