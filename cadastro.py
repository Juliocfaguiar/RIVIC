import streamlit as st
import os

def app():
    st.header("**Cadastro**",divider="green")


    col1, col2 = st.columns(spec=[1,1])
    with col1:
        st.text_input('Nome Completo')
        st.text_input("e-mail")
        col01, col02 = st.columns(spec=[1,1])
        with col01:
            st.text_input('CPF')
            st.text_input("Telefone")
        with col02:
            st.text_input('RG')
            st.text_input('Data de Nascimento')
            
    with col2:
        tempimg_path = "tempimg"
        cl = False
        ps = False
        if os.path.exists(tempimg_path):
            files = os.listdir(tempimg_path)
            col03,col04,col05 = st.columns(spec=[1,1,1])
            with col03:
                pass
            with col04:
                st.image(os.path.join(tempimg_path, files[0]), width=300)
                
                ps = st.checkbox("Prestador de serviço")
                cl = st.checkbox("Colaborador")
            with col05:
                pass
    
    col3,col4 = st.columns(spec=[1,1])
    with col3:
        if ps == True:
            col06, col07 = st.columns(spec=[1,1])
            with col06:
                st.text_input("Nome da Empresa")
                st.text_input("CNPJ da Empresa")
            with col07:
                st.text_input("Telefone da Empresa")
                st.text_input("Cargo")
    
        if cl == True:
            col08, col09 = st.columns(spec=[1,1])
            with col08:
                OPTIONS = ["TD","CSTI","ADM","DIRETORIA","OUTRO"]
                st.selectbox(options=OPTIONS, label="Setor")
            with col09:
                st.text_input("Número do R.A")

        
# Compare this snippet from main.py:)












    pass
