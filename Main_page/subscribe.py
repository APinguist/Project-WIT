import streamlit as st


def load_view():    
        # ---- CONTACT ----
    with st.container():

        st.markdown("<h1 style='text-align: center; color: light green;'>Subscribe</h1>", unsafe_allow_html=True)     
        st.write("##")
        st.write("##")

        # Form Submit
        contact_form = """
        <form action="https://formsubmit.co/audrey.carissa01@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <div style="text-align:center" "font-weight: bold">
                <button type="submit">Send</button>
            </div>
        </form>
        """
        
        st.markdown(contact_form, unsafe_allow_html=True)   
        st.write("##")
        st.markdown(
        """
            Fitur ini menggunakan [FormSubmit](https://formsubmit.co/) sehingga Anda akan diminta untuk memverifikasi email Anda
            untuk menggunakannya
        """,  unsafe_allow_html=True)


            