import streamlit as st
from streamlit_option_menu import option_menu
from  PIL import Image
import requests
from streamlit_lottie import st_lottie



def load_view():
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # ---- LOAD ASSETS ----
    lottie_cyber = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ndt8zfny.json") 
    
    st.markdown("""
        <p style="text-align: center; font-weight: 700;  font-size: 40px; margin: -5px"> 
            LET'S LEARN
        </p>""", unsafe_allow_html=True)
    st.write("###")

    #------HEADER SECTION------
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("CYBERSTUDIO")
            st.markdown("""
            <p style="font-weight: 700;  font-size: 40px; margin: -5px">
                Apa itu
                <span style="color:#82CAFA;font-weight: 700;  font-size: 40px"> 
                    Keamanan Siber 
                </span>? 
            </p>""", unsafe_allow_html=True)
            st.write("##")
            st.markdown("""
            <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); text-align: justified; font-size: 16px">
                Keamanan siber adalah praktik melindungi sistem penting dan informasi sensitif dari serangan digital. Dikenal juga sebagai keamanan teknologi informasi (TI), langkah-langkah keamanan siber dirancang untuk memerangi ancaman terhadap sistem dan aplikasi jaringan, baik ancaman tersebut berasal dari dalam atau luar organisasi. 
            </p>""", unsafe_allow_html=True)
            st.markdown("""
            <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); text-align: justified; font-size: 16px;">
                Menurut UK National Cyber Security Strategy, keamanan siber mengacu pada perlindungan sistem informasi (perangkat keras, perangkat lunak, dan infrastruktur terkait), data di dalamnya, dan layanan yang mereka berikan, dari akses tidak sah, bahaya, atau penyalahgunaan. Ini termasuk kerusakan yang disebabkan secara sengaja oleh operator sistem, atau secara tidak sengaja, sebagai akibat dari kegagalan mengikuti keamanan prosedur.
            </p>""", unsafe_allow_html=True)
        
        with right_column:
            st_lottie(lottie_cyber, height=400)
    st.write("---")

    

    #------MAIN MENU------
    choose = option_menu("Main Menu", ["Pengantar Cybersecurity", "Serangan, Konsep, dan Teknik", "Prinsip Dasar Keamanan Siber", "Kriptografi"], 
        default_index=0,
        styles={
        "container": {"padding": "5!important", "background-color": "#1010b3"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#000047"},
        "nav-link-selected": {"background-color": "#203ae6"},
    }
    )

    #------MODULE 1------
    if choose == "Pengantar Cybersecurity":
        topic_1 = option_menu(None, ["Model CyberSecurity","Pelaku dan Motif Serangan Siber", "Asal Serangan Siber", "Target Hacker dan Tips"],
        icons=['book', 'book','book','book'],
        menu_icon="list", default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#0704cc"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#010169"},
            "nav-link-selected": {"background-color": "#080000", },
        },
        orientation='horizontal')

        #------SUBMODULE 1A------
        if topic_1=="Model CyberSecurity":
            with st.container ():
                feature_image1 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 1 - ANCAMAN KEAMANAN CYBER_page-0002.jpg")
                st.image(feature_image1)
            
        #------SUBMODULE 1B------
        elif topic_1 =="Pelaku dan Motif Serangan Siber":
            with st.container ():
                feature_image4 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 1 - ANCAMAN KEAMANAN CYBER_page-0003.jpg")
                feature_image5 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 1 - ANCAMAN KEAMANAN CYBER_page-0004.jpg")
                feature_image6 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 1 - ANCAMAN KEAMANAN CYBER_page-0005.jpg")
                st.image(feature_image5)
                st.image(feature_image4)
                st.image(feature_image6)

        #------SUBMODULE 1C------
        elif topic_1 =="Asal Serangan Siber":
            with st.container ():
                feature_image2 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 1 - ANCAMAN KEAMANAN CYBER_page-0006.jpg")
                feature_image3 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 1 - ANCAMAN KEAMANAN CYBER_page-0007.jpg")
                st.image(feature_image2)
                st.image(feature_image3)

        #------SUBMODULE 1D------
        elif topic_1 =="Target Hacker dan Tips":
            with st.container ():
                feature_image7 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 1 - ANCAMAN KEAMANAN CYBER_page-0008.jpg")
                feature_image8 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 1 - ANCAMAN KEAMANAN CYBER_page-0009.jpg")
                st.image(feature_image7)
                st.image(feature_image8)
   
    #------MODULE 2------
    if choose == "Serangan, Konsep, dan Teknik":
        topic_2 = option_menu(None, ["Pengenalan","Malware", "Teknik Menjebol Password"],
        icons=['book', 'book','book'],
        menu_icon="list", default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#0704cc"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#010169"},
            "nav-link-selected": {"background-color": "#080000", },
        },
        orientation='horizontal')
        #------SUBMODULE 2A------
        if topic_2 =="Pengenalan":
            with st.container ():
                feature_image21= Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 2 - SERANGAN, KONSEP, dan TEKNIK_page-0001.jpg")
                st.image(feature_image21)

        #------SUBMODULE 2B------
        elif topic_2 =="Malware":
            with st.container ():
                feature_image22 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 2 - SERANGAN, KONSEP, dan TEKNIK_page-0002.jpg")
                feature_image23 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 2 - SERANGAN, KONSEP, dan TEKNIK_page-0003.jpg")
                st.image(feature_image22)
                st.image(feature_image23)

        #------SUBMODULE 2C------
        elif topic_2 =="Teknik Menjebol Password":  
            with st.container():
                feature_image24 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 2 - SERANGAN, KONSEP, dan TEKNIK_page-0004.jpg")
                feature_image25 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 2 - SERANGAN, KONSEP, dan TEKNIK_page-0005.jpg")
                feature_image27 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 2 - SERANGAN, KONSEP, dan TEKNIK_page-0006.jpg")
                st.image(feature_image24)
                st.image(feature_image25)
                st.image(feature_image27)  

    #------MODULE 3------
    if choose == "Prinsip Dasar Keamanan Siber":
        topic_3 = option_menu(None, ["CIA TRIAD","CIA TRIAD + AAA", "Perlindungan Data", "Cyber Security Safeguard"],
        icons=['book', 'book','book','book'],
        menu_icon="list", default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#0704cc"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#010169"},
            "nav-link-selected": {"background-color": "#080000", },
        },
        orientation='horizontal') 

        #------SUBMODULE 3A------
        if topic_3=="CIA TRIAD":
            with st.container ():
                st.markdown(""" 
                    <style> 
                    .font {font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
                    </style> """, unsafe_allow_html=True)
                st.markdown('<p class="font">Triad CIA</p>', unsafe_allow_html=True)
                
                
                col1, col2 = st.columns(2)
                with col1:              
                    st.markdown("""
                        <p class="font">
                            Tiga prinsip utama:  kerahasiaan (confidentiality), integritas (integrity), dan ketersediaan (availability)
                        </p>""", unsafe_allow_html=True)    
                with col2:              
                    
                    st.markdown("""
                        <p class="font">
                            CIA Triad adalah model keamanan yang telah dikembangkan untuk membantu orang berpikir tentang bagian-bagian dari keamanan TI. Tujuannya adalah untuk memiliki keseimbangan ketiga aspek tersebut.
                        </p>""", unsafe_allow_html=True)  
            
            with st.container (): 
                feature_image31 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 3 - Prinsip Dasar Keamanan Siber_page-0001.jpg")
                st.image(feature_image31)     

        #------SUBMODULE 3B------
        elif topic_3 == "CIA TRIAD + AAA":
            with st.container ():
                feature_image32 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 3 - Prinsip Dasar Keamanan Siber_page-0002.jpg")
                st.image(feature_image32)

        #------SUBMODULE 3C------
        elif topic_3 =="Perlindungan Data":
            with st.container ():
                feature_image33 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 3 - Prinsip Dasar Keamanan Siber_page-0003.jpg")
                feature_image34 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 3 - Prinsip Dasar Keamanan Siber_page-0004.jpg")
                st.image(feature_image33)
                st.image(feature_image34)

        #------SUBMODULE 3D------
        elif topic_3 =="Cyber Security Safeguard":  
            with st.container():
                feature_image35 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 3 - Prinsip Dasar Keamanan Siber_page-0005.jpg")
                feature_image36 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 3 - Prinsip Dasar Keamanan Siber_page-0006.jpg")
                st.image(feature_image35)
                st.image(feature_image36)  


    #------MODULE 4------
    if choose == "Kriptografi":
        topic_4 = option_menu(None, ["Pengenalan Kriptografi","Enkripsi vs Dekripsi", "Teknik Kriptografi Sederhana", "Enkripsi Modern", "Hashing"],
        icons=['book', 'book','book', 'book','book'],
        menu_icon="list", default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#0704cc"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#010169"},
            "nav-link-selected": {"background-color": "#080000", },
        },
        orientation='horizontal')

        #------SUBMODULE 4A------
        if topic_4 =="Pengenalan Kriptografi":
            with st.container ():
                feature_image41 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0002.jpg")
                st.image(feature_image41)

        #------SUBMODULE 4B------
        elif topic_4 =="Enkripsi vs Dekripsi":
            with st.container ():
                feature_image42 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0003.jpg")
                st.image(feature_image42)

        #------SUBMODULE 4C------
        elif topic_4 =="Teknik Kriptografi Sederhana":
            with st.container ():
                feature_image43 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0004.jpg")
                feature_image44 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0005.jpg")
                feature_image45 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0006.jpg")
                feature_image46 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0007.jpg")
                st.image(feature_image43)
                st.image(feature_image44)
                st.image(feature_image45)
                st.image(feature_image46)

        #------SUBMODULE 4D------
        elif topic_4 =="Enkripsi Modern":
            with st.container ():
                feature_image47 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0008.jpg")
                feature_image48 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0009.jpg")
                st.image(feature_image47)
                st.image(feature_image48)

        #------SUBMODULE 4E------
        elif topic_4 =="Hashing":
            with st.container ():
                feature_image49 = Image.open(r"C:\Users\PAVILION\Documents\Streamlit\1_audrey\project_WIT\images\MODUL 4 - Kriptografi_page-0010.jpg")
                st.image(feature_image49)
