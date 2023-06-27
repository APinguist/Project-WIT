import streamlit as st
from streamlit_option_menu import option_menu #untuk membuat menu
import hashlib #enkripsi menggunakan hash md5
import requests # mengirim request http
from streamlit_lottie import st_lottie  #untuk menggunakan animasi lottie


    
def load_view():
    

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # ---- LOAD ASSETS ----
    lottie_time = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_etaum4bz.json") 
    lottie_data = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_x17ybolp.json") 

    #----- def Caesar-Cypther ------
    alphabets = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{ }|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ" #untuk library nya

    def encrypt_caesar(num, text):
        results = ' '
        for k in text:
            try:
                i = (alphabets.index(k) + num) % 26
                results += alphabets[i]
            except ValueError:
                results+= k
        return results.lower()
    
    def decrypt_caesar(num, text):
        results = ''
        for k in text:
            try:
                i = (alphabets.index(k) - num) % 26
                results +=alphabets[i]
            except ValueError:
                results += k
        return results.lower()

    st.markdown("""
        <p style="text-align: center; font-weight: 700;  font-size: 40px; margin: -5px"> 
            TOOLS
        </p>""", unsafe_allow_html=True)
    st.write("###")


    #------MENU------ 

    selected = option_menu("Main Menu", ["Enkripsi", "Dekripsi"], 
        icons=['lock fill', 'unlock fill'],
        styles={
        "container": {"padding": "5!important", "background-color": "#1010b3"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#000047"},
        "nav-link-selected": {"background-color": "#203ae6"},
    }
    )
    
    
    # ----- Enkripsi--------
    if selected == "Enkripsi":
        st.markdown("""
        <p style="text-align: center; font-weight: 700;  font-size: 30px; margin: -5px"> 
            Enkripsi
        </p>""", unsafe_allow_html=True)
         
         # ------ Enkripsi Menu ------       
        if selected == "Enkripsi":
            # ------ Enkripsi Penjelasan 1 ------  
            with st.container():
                st.write("---")
                st.markdown("""
                <p style="text-align: center; font-weight: 400;  font-size: 20px; margin: -5px"> 
                    Apa     Itu 
                    <span style="color:#82CAFA; font-weight: 700"> 
                        Enkripsi
                    </span> 
                    ? 
                </p>""", unsafe_allow_html=True)
                st.write("###")
                st.markdown("""
                <p style="text-align: center; margin: -5px"> 
                    Enkripsi (Encryption) adalah metode di mana informasi diubah menjadi kode rahasia yang menyembunyikan arti sebenarnya dari informasi tersebut. 
                </p>""", unsafe_allow_html=True)
                st.markdown("""
                <p style="text-align: center; margin: -5px"> 
                    Ilmu mengenkripsi informasi disebut 
                    <span style="color:#82CAFA; font-weight: 700"> 
                        kriptografi
                    </span> (ketahui lebih lanjut tentang kriptografi di Let's Learn).
                </p>""", unsafe_allow_html=True)

            # ------ Enkripsi Penjelasan 2 ------  
            with st.container():
                st.write("---")
                left_column, right_column = st.columns([1,3])
                with left_column:
                    st_lottie(lottie_time, height=350 )
                    
                with right_column:
                    st.write("###")
                    st.write("###")
                    st.write("###")
                    
                    st.markdown("""
                    <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                        Agar efektif, cipher menyertakan variabel sebagai bagian dari algoritma. Variabel, yang disebut kunci, adalah apa yang membuat keluaran cipher menjadi unik. Ketika pesan terenkripsi dicegat oleh entitas yang tidak berwenang, penyusup harus menebak sandi mana yang digunakan pengirim untuk mengenkripsi pesan, serta kunci apa yang digunakan sebagai variabel. Waktu dan kesulitan menebak informasi inilah yang membuat enkripsi menjadi alat keamanan yang berharga.
                    </p>""", unsafe_allow_html=True)
                    st.markdown("""
                    <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                        Enkripsi digunakan oleh militer dan pemerintah sejak dulu. Di zaman modern, enkripsi digunakan untuk melindungi data yang disimpan di komputer dan perangkat penyimpanan, serta data dalam perjalanan melalui jaringan.
                    </p>""", unsafe_allow_html=True)

            st.write("##")
             # ------ Enkripsi Menu ------ 
            option2 = st.selectbox('Tipe', ('Caesar-Cypther', 'MD5'))
            
        
        # ------ Enkripsi Caesar-Cypther ------
        if option2 == "Caesar-Cypther":
            with st.container():
                st.markdown("""
                <p style="text-align: center; font-weight: 400;  font-size: 20px; margin: -5px"> 
                    Apa Itu 
                    <span style="color:#82CAFA; font-weight: 700"> 
                        Enkripsi Caesar-Cypther
                    </span> 
                    ? 
                </p>""", unsafe_allow_html=True)

            # ------ CC Penjelasan 1 ------ 
            with st.container():
                st.write("###")
                a1, a2, a3 = st.columns([0.5,3, 0.5])
                with a1:
                    st.empty()
                with a2:
                    st.markdown("""
                    <p style="text-align: center; margin: -5px"> 
                        Enkripsi Caesar-Cypther
                        adalah metode enkripsi dengan menggantikan bit, karakter, atau blok karakter dengan pengganti. 
                    </p>""", unsafe_allow_html=True)
                    st.markdown("""
                    <p style="text-align: center; margin: -5px"> 
                        Nama lainnya adalah substitution ciphers. Ini ditemukan oleh Julius Caesar. Beliau menggunakannya dengan pergeseran tiga (A menjadi D saat mengenkripsi, dan D menjadi A saat mendekripsi) untuk melindungi pesan penting militer.
                    </p>""", unsafe_allow_html=True)
                with a3:
                    st.empty()

            st.write("---")
            num_cc = st.number_input("Masukkan perputaran/pergeseran :\t", min_value=1, step=1, key="input_enum_cc")

             # ------ CC Penjelasan 2 ------  
            with st.container():
                st.write("---")
                x1, x2, x3 = st.columns([0.5,3, 0.5])
                with x1:
                    st.empty()
                with x2:
                    st.markdown("""
                    <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                        Caesar cipher menggeser semua huruf dalam sepotong teks dengan sejumlah tempat tertentu. Kunci untuk cipher ini adalah huruf yang mewakili jumlah tempat untuk shift. Jadi, misalnya, kunci D berarti "menggeser 3 tempat" dan kunci M berarti "menggeser 12 tempat". Perhatikan bahwa kunci A berarti "jangan bergeser" dan kunci Z bisa berarti "menggeser 25 tempat" atau "menggeser satu tempat ke belakang". Misalnya, kata “caesar” dengan shift P (menggeser 16 tempat) menjadi “rpthpg”.
                    </p>""", unsafe_allow_html=True)
                with x3:
                    st.empty()
                st.write("---")

            text_cc = st.text_input("Masukkan text : \t", key="input_eteks_cc")
            ciphertext=encrypt_caesar(num_cc, text_cc)
            st.text_area("Hasil Encode :", ciphertext)
            

        # ------ Enkripsi MD5 ------
        elif  option2 == "MD5":
            with st.container():
                st.markdown("""
                <p style="text-align: center; font-weight: 400;  font-size: 20px; margin: -5px"> 
                    Apa Itu 
                    <span style="color:#82CAFA; font-weight: 700"> 
                        Enkripsi MD5
                    </span> 
                    ? 
                </p>""", unsafe_allow_html=True)

            # ------ MD5 Penjelasan 1 ------ 
            with st.container():
                st.write("###")
                a1, a2, a3 = st.columns([0.5,3, 0.5])
                with a1:
                    st.empty()
                with a2:
                    st.markdown("""
                    <p style="text-align: center; margin: -5px"> 
                        MD5 (message-digest algorithm) adalah protokol kriptografi yang digunakan untuk mengautentikasi pesan serta verifikasi konten dan tanda tangan digital.  
                    </p>""", unsafe_allow_html=True)
                    st.write("###")
                    st.markdown("""
                    <p style="text-align: center; margin: -5px"> 
                        MD5 didasarkan pada fungsi hash yang memverifikasi bahwa file yang Anda kirim cocok dengan file yang diterima oleh orang yang Anda kirimi. Sebelumnya, MD5 digunakan untuk enkripsi data, tetapi sekarang digunakan terutama untuk otentikasi.
                    </p>""", unsafe_allow_html=True)
                with a3:
                    st.empty()

            st.write("---")
            text_md5=st.text_input("Masukkan text : \t", key="md5")

            # ------ MD5 Penjelasan 2 ------  
            with st.container():
                st.write("---")
                x1, x2, x3 = st.columns([0.5,3, 0.5])
                with x1:
                    st.empty()
                with x2:
                    st.markdown("""
                    <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                        Algoritma hashing MD5 menggunakan rumus matematika yang kompleks untuk membuat hash.Langkah-langkah algoritma MD5 sangat rumit — Anda tidak dapat membalikkan proses ini dan menghasilkan file asli dari hash. 
                    </p>""", unsafe_allow_html=True)
                    st.markdown("""
                    <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                        Tetapi input yang sama akan selalu menghasilkan output yang sama, juga dikenal sebagai MD5 sum, hash, atau checksum. Itulah yang membuat mereka sangat berguna untuk validasi data. Contoh hash MD5 terlihat seperti ini: 0cc175b9c0f1b6a831c399e269772661. Itu hash untuk huruf "a"
                    </p>""", unsafe_allow_html=True)
                with x3:
                    st.empty()
                st.write("---")

            result_md5 = hashlib.md5(text_md5.encode()) #enkripsi menggunakan hash md5
            a_dec = result_md5.hexdigest()
            st.text_area("Hasil Encode :", a_dec)

            # ------ MD5 Penjelasan 3 ------  
            with st.container():
                st.write("---")
                x1, x2, x3 = st.columns([0.5,3, 0.5])
                with x1:
                    st.empty()
                with x2:
                    st.markdown("""
                    <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                        Sebuah hash MD5 adalah 16 byte. Setiap hash MD5 terlihat seperti 32 angka dan huruf, tetapi setiap digit dalam heksadesimal dan mewakili empat bit. Karena satu karakter mewakili delapan bit (untuk membentuk satu byte), jumlah bit total dari hash MD5 adalah 128 bit. Dua karakter heksadesimal membentuk satu byte, jadi 32 karakter heksadesimal sama dengan 16 byte.
                        Maka, Panjang MD5 akan selalu sama: hash 128-bit.
                    </p>""", unsafe_allow_html=True)
                with x3:
                    st.empty()
                st.write("---")
                

    # ----- Dekripsi--------
    elif selected == "Dekripsi":
        st.markdown("""
        <p style="text-align: center; font-weight: 700;  font-size: 30px; margin: -5px"> 
            Dekripsi
        </p>""", unsafe_allow_html=True)

        # ------ Dekripsi Penjelasan 1 ------ 
        with st.container():
                st.write("---")
                st.markdown("""
                <p style="text-align: center; font-weight: 400;  font-size: 20px; margin: -5px"> 
                    Apa     Itu 
                    <span style="color:#82CAFA; font-weight: 700"> 
                        Dekripsi
                    </span> 
                    ? 
                </p>""", unsafe_allow_html=True)
                st.markdown("""
                <p style="text-align: center; margin: -5px"> 
                    Dekripsi (Decryption) adalah proses mengubah data yang telah di-enkripsi kembali ke bentuk yang tidak terenkripsi/ke bentuk aslinya. 
                </p>""", unsafe_allow_html=True)
                st.markdown("""
                <p style="text-align: center; margin: -5px"> 
                    Ilmu mendekripsi informasi disebut 
                    <span style="color:#82CAFA; font-weight: 700"> 
                        kriptografi
                    </span> (ketahui lebih lanjut tentang kriptografi di Let's Learn).
                </p>""", unsafe_allow_html=True)
        
        # ------ Dekripsi Penjelasan 2 ------  
        with st.container():
            st.write("---")
            left_column, right_column = st.columns([2,3])
            with left_column:
                st.write("###")
                st_lottie(lottie_data, height=350)
                    
            with right_column:
                st.write("###")
                st.write("###")
                st.write("###")
                st.write("###")

                st.markdown("""
                <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                    Dalam dekripsi, sistem mengekstrak dan mengubah data yang kacau dan mengubahnya menjadi teks dan gambar yang mudah dimengerti tidak hanya oleh pembaca tetapi juga oleh sistem.
                </p>""", unsafe_allow_html=True)
                st.markdown("""
                <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                    Dekripsi dapat dilakukan secara manual atau otomatis. Ini juga dapat dilakukan dengan satu set kunci atau kata sandi.
                </p>""", unsafe_allow_html=True)

         # ------ Dekripsi Menu ------ 
        option_dec = st.selectbox('Tipe', ('Caesar-Cypther', ''))

        # ------ Dekripsi Caesar-Cypther ------
        if option_dec == "Caesar-Cypther":
            with st.container():
                st.markdown("""
                <p style="text-align: center; font-weight: 400;  font-size: 20px; margin: -5px"> 
                    Apa Itu 
                    <span style="color:#82CAFA; font-weight: 700"> 
                        Dekripsi Caesar-Cypther
                    </span> 
                    ? 
                </p>""", unsafe_allow_html=True)


            # ------ CC Penjelasan 1 ------ 
            with st.container():
                st.write("###")
                a1, a2, a3 = st.columns([0.5,3, 0.5])
                with a1:
                    st.empty()
                with a2:
                    st.markdown("""
                    <p style="text-align: center; margin: -5px"> 
                        Dekripsi Caesar-Cypther
                        adalah metode dekripsi dengan mencoba menemukan kunci yang tepat dan mendekripsi data. 
                    </p>""", unsafe_allow_html=True)
                with a3:
                    st.empty()

            st.write("---")
            num_c = st.number_input("Masukkan perputaran/pergeseran  :\t", min_value=1, step=1, key="input_dnum_cc")
             
            # ------ CC Penjelasan 2 ------  
            with st.container():
                st.write("---")
                x1, x2, x3 = st.columns([0.5,3, 0.5])
                with x1:
                    st.empty()
                with x2:
                    st.markdown("""
                    <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                        Masalah cipher ini adalah keamanannya yang sangat buruk. Untuk memecahkannya, Anda dapat menerapkan setiap perubahan pada sandi Caesar, dan melihat apakah ada yang masuk akal. 
                    </p>""", unsafe_allow_html=True)
                    st.markdown("""
                    <p style="font-weight: 200; src: url(arvo-v20-latin-regular.woff2); ">
                        Cara lain untuk memecahkannya adalah dengan melihat frekuensi huruf. Data yang diennkripsi dengan pergeseran 16 maka hanya bisa didekripsikan dengan pergeseran 16.
                    </p>""", unsafe_allow_html=True)
                with x3:
                    st.empty()
                st.write("---")
            
            text_c = st.text_input("Masukkan text : \t", key="input_dteks_cc")
            ciphertext_dec=decrypt_caesar(num_c, text_c)
            st.text_area("Hasil Decode :",  ciphertext_dec)

