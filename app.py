import streamlit as st 
import utils as utl
from Main_page import about_us,tools,contact_us, subscribe, learn, blog
import matplotlib
matplotlib.use('Agg')


st.set_page_config(
    page_title="CyberStudio",
    page_icon="💻",
    layout = 'wide')

st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

head_message_temp ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
    <h4 style="color:white;text-align:center;">{}</h1>
    <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
    <h6>Author:{}</h6> 
    <h6>Post Date: {}</h6> 
    </div>
    """
full_message_temp ="""
    <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
    <p style="text-align:justify;color:black;padding:10px">{}</p>
    </div>
    """


def main():
    route = utl.get_current_route()
    if route == "about us":
        about_us.load_view() 
    elif route == "tools":
        tools.load_view()
    elif route == "let\'s learn":
        learn.load_view()    
    elif route == "blog":
        blog.load_view()
    elif route == "contact us":
        contact_us.load_view() 
    elif route == "subscribe":
        subscribe.load_view()
    elif route == None:
        about_us.load_view()
    

if __name__ == '__main__':
    main()

