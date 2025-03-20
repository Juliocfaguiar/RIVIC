import streamlit as st
from streamlit_option_menu import option_menu
import home, cadastro, visitante ,servicos, colaborador, adm
import pandas as pd
from deepface import DeepFace
import sqlite3

st.set_page_config(page_title="Integrador_v_RIVIC",layout="wide",page_icon="👾")

# config()

# from os_sys.progress import spinner

# spinner = Spinner('Loading ')
# while state != 'FINISHED':
#     # Do some work
#     spinner.next()


# There are 5 predefined spinners:

# Spinner
# PieSpinner
# MoonSpinner
# LineSpinner
# PixelSpinner


class Multiapp:
    
    def __int__(self):
        self.apps = []
    def add_app(self,title,function):
        self.app.append({
            "title"     : title,
            "function"  : function
        })

    def run() :

        app = option_menu(None, 
                          ['Home','Cadastro','Visitante',"Prestador de Serviços",'colaborador','adm'],
                          
            icons=['house-fill','database','person-circle','person-circle','person-circle','pc-display-horizontal'
                #    'question-diamond-fill','display','display','bi-buildings-fill'
                   ], 
            menu_icon="cast", default_index=0, orientation="horizontal")
    
        
        if app == "Home":
            home.app()
        if app == "Cadastro":
            cadastro.app()  
        if app == "Visitantes":
            visitante.app()    
        if app == "Prestador de Serviços":
            servicos.app()
        if app == "colaborador":
            colaborador.app()         
        if app == 'adm':
            adm.app()   
             
    run()
