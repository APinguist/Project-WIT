import requests # mengirim request http
import streamlit as st
from streamlit_lottie import st_lottie  #untuk menggunakan animasi lottie

def load_view():

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    # ---- LOAD ASSETS ----
    lottie_cyber = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_w0acmrm6.json") 
    lottie_learn = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_sns5vheb.json")
 
    #------HEADER SECTION------
    with st.container():
    
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("CYBERSTUDIO")
            original_sub0 = """
            <p style="font-weight: 700;  font-size: 40px; margin: -5px"> 
                Mengenal 
                <span style="color:#82CAFA;font-weight: 700;  font-size: 40px"> 
                    Dunia Siber 
                </span> 
                Bersama 
                <span style="color:#82CAFA;font-weight: 700;  font-size: 40px"> 
                    CyberStudio 
                </span> 
            </p>"""
            original_sub1 = """
            <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); text-align: justified; font-size: 14px">
                Setiap orang rentan terhadap serangan siber. Oleh karena itu, mempelajari keamanan siber menjadi penting untuk mengidentifikasi berbagai ancaman, kerentanan, dan serangan siber. 
                <span style="color:#82CAFA; font-weight: 700"> 
                    CyberStudio
                </span> 
                akan membantu Anda mengenal apa itu dunia keamanan siber dan dampaknya terhadap dunia modern. 
            </p>"""
            original_sub2 = """
            <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); text-align: justified; font-size: 14px;">
                Ayo berlangganan dan aktifkan notifikasi, agar Anda tidak ketinggalan konten apa pun! 🚀
            </p>"""
            st.markdown(original_sub0, unsafe_allow_html=True)
            st.write("##")
            st.markdown(original_sub1, unsafe_allow_html=True)
            st.markdown(original_sub2, unsafe_allow_html=True)
            
        with right_column:
            st_lottie(lottie_cyber, height=400)
    st.write("---")


    #------APA YANG CYBERSTUDIO LAKUKAN------
    with st.container():
        # --- Header ---
        st.markdown("""
        <p style="text-align: center; font-weight: 700;  font-size: 30px; margin: -5px"> 
            Apa Yang 
            <span style="color:#82CAFA; font-weight: 700"> 
                CyberStudio
            </span> 
            Lakukan? 
        </p>""", unsafe_allow_html=True)
        # --- penjelasan ---
        left_column, right_column = st.columns([2, 2])
        with left_column:
            st_lottie(lottie_learn, height=400)
        with right_column:
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("""
                CyberStudio adalah platform terbuka bagi masyarakat umum yang ingin :
                - Mengenal tentang keamanan siber (cybersecurity)
                - Menambah wawasan tentang keamanan siber (cybersecurity)
            """)
            st.markdown("""
            Kamu bisa membantu kami dengan berdonasi melalui link di bawah ini 
            <div style="margin-top: 0.75em;">
                <a href="https://www.buymeacoffee.com/" target="_blank">
                <img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="31" width="154">
                </a>
            </div>
            """,
            unsafe_allow_html=True)

    #------CONTACT------
    with st.container():
        st.write("---")
        st.header("Get In Touch With Us!")
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
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
