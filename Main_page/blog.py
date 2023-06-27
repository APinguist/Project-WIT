import streamlit as st
from streamlit_text_rating.st_text_rater import st_text_rater
from  PIL import Image #membuka image dari laptop
import base64 #untuk membuka pdf di web 




def load_view():

    def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf">
        </iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
        

    st.markdown("""
        <p style="text-align: center; font-weight: 700;  font-size: 40px; margin: -5px"> 
            BLOG
        </p>""", unsafe_allow_html=True)
    st.write("###")

    #------POST 1------
    feature_image1 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\Bruteforce.png")
    with st.container():
        image_col, text_col = st.columns((1,3))
        with image_col:
            st.image(feature_image1,caption='Image by Pixabay')
        with text_col:
            st.markdown(""" 
            <style> .font {font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
            st.markdown("""
            <p class="font">
                Apa itu Two Factor Authentication?
            </p>""", unsafe_allow_html=True)    
            st.markdown("""
                Belakangan ini kerap kita dengar mengenai adanya kebocoran data atau hacking beberapa akun baik media sosial hingga akun e-commerce. Hal ini terjadi karena kurang kuatnya system keamanan yang diterapkan ...
                """)

    with st.container():
        col1, col2,col3= st.columns(3)
        with col1:  
            if st.button('Read PDF Tutorial',key='10'):            
                show_pdf('post1.pdf')
        with col2:
            st.button('Close PDF Tutorial',key='11')                   
        with col3:
            with open("post1.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(label="Download PDF Tutorial", 
                            key='12',
                            data=PDFbyte,
                            file_name="Apa-itu-Two-Factor-Authentication?.pdf",
                            mime='application/octet-stream')

        for text in ["Is this tutorial helpful?"]:
            response = st_text_rater(text=text, key='1', )
    st.write('---')

    #------POST 2------
    feature_image2 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\ransomeware.jpg")
    with st.container():
        image_col, text_col = st.columns((1,3))
        with image_col:
            st.image(feature_image2,caption='Image by Pixabay')

        with text_col:
            st.markdown(""" <style> .font {
                    font-size:22px ; font-family: 'Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Ransomeware dan Cara Pencegahannya</p>', unsafe_allow_html=True)    
            st.markdown(""" 
                Ransomware adalah berasal dari nama kelas malware yang terdiri dari dua kata “ranson” yang berarti tebusan dan “malware.” Badan Siber dan Sandi Negara menjelaskan tujuan ransomware adalah menuntut pembayaran ...
                """)

    with st.container():               
        col1, col2,col3 = st.columns(3)
        with col1: 
            if st.button('Read PDF Tutorial',key='7'): 
                show_pdf('post2.pdf')
        with col2:
            st.button('Close PDF Tutorial',key='8')                   
        with col3:
            with open("post2.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(label="Download PDF Tutorial",
                            key='9',
                            data=PDFbyte,
                            file_name="Ransomeware-dan-Cara-Pencegahannya.pdf",
                            mime='application/octet-stream')

        for text in ["Is this tutorial helpful?"]:
            response = st_text_rater(text=text, key='2')

    st.write('---')


    #------POST 3------
    feature_image3 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\2FA.jpg")
    with st.container():
        image_col, text_col = st.columns((1,3))
        with image_col:
            st.image(feature_image3,caption='Image by Pixabay')

        with text_col:
            st.markdown('<p class="font">Manajemen Password</p>', unsafe_allow_html=True)    
            st.markdown("""
                Dengan semakin meningkatnya penggunaan teknologi informasi, maka semakin meningkat pula jumlah user account dan password yang harus kita ingat dan kelola. Password merupakan metode yang nyaman dan mudah untuk melakukan autentikasi user saat masuk ke sistem komputer. Sistem hanya mengharuskan ...
                """)

    with st.container():                       
        col1, col2,col3 = st.columns(3)
        with col1:
            if st.button('Read PDF Tutorial',key='4'): 
                show_pdf('post3.pdf')
        with col2:
            st.button('Close PDF Tutorial',key='5')                   
        with col3:
            with open("post3.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(label="Download PDF Tutorial",
                            key='6',
                            data=PDFbyte,
                            file_name="Manajemen-Password.pdf",
                            mime='application/octet-stream')
        for text in ["Is this tutorial helpful?"]:
            response = st_text_rater(text=text, key='3')
