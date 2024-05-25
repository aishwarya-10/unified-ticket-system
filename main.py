# ==================================================       /     IMPORT LIBRARY    /      =================================================== #
#[Data Transformation]
import numpy as np
import pandas as pd

#[DataBase]
import pymysql

#[Dashboard]
import plotly.graph_objects as go
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_option_menu import option_menu

#[Module]
import pages.home as home, pages.account as account


# ==================================================       /     CUSTOMIZATION    /      =================================================== #
# Streamlit Page Configuration
st.set_page_config(
    page_title = "Unified-Ticketing-System",
    page_icon= "Images/bus-ticket.png",
    layout = "wide",
    initial_sidebar_state= "collapsed"
    )





class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # Top Navbar 
        container = st.container()
        with container:
            col1, col2 = st.columns(2)
            # Column 1: Title
            with col1:
                col1.markdown("# :blue[Unified Ticket System]", unsafe_allow_html=True)

            # Column 2: Navigation Menu
            with col2:
                menu = option_menu(
                    menu_title = None,
                    options=["Home", "Account", "Wallet", "Support", "Log-out"],
                    default_index= 1,
                    icons = ["house", "person-circle", "wallet2", "person-raised-hand", "door-closed"],
                    orientation = "horizontal",
                    styles={
                    "container": {"padding": "10px", "background-color": "#f0f0f0"},
                    "nav-link": { "--hover-color": "#834da0","color": "black","width":"140px",
                                    "text-align":"center","padding":"5px 0",
                                    "border-bottom":"4px solid transparent","transition":"border-bottom 0.5 ease","font-size":"14px", "font-weight": "bold"},
                    "nav-link:hover": {"color":"black"},
                    "nav-link-selected": {"background-color": "#391c59", "width":"140px","border-bottom":"4px solid #834da0","color":"white"}
                    }           
                )

        if menu == "Home":
            home.app()
        
        elif menu == "Account":
            account.app()


    run()






# streamlit run main.py