import streamlit as st
import pandas as pd
from deepface import DeepFace
import sqlite3
import os
import shutil
import cv2

def app():
    testeimg = None
    temp = "tempimg"
    if os.path.exists(temp):
        shutil.rmtree(temp)

    col1, col2 = st.columns(spec=[1,0.3], border=True)
    with col1:
        uploadimg = st.file_uploader('', ["jpg", "jpeg", "png"])
        if uploadimg is not None:
            if os.path.exists(temp):
                shutil.rmtree(temp)
            os.makedirs(temp, exist_ok=True)
            
            testeimg = os.path.join(temp, uploadimg.name)
            with open(testeimg, "wb") as f:
                f.write(uploadimg.getvalue())
    with col2:
        # Função para ler a imagem como bytes
        def load_image_as_bytes(image_path):
            with open(image_path, "rb") as file:
                return file.read()

        # Caminho da imagem na pasta raiz
        image_path = "teste.jpg"  # Substitua pelo nome do seu arquivo

        # Carregar a imagem como bytes
        image_bytes = load_image_as_bytes(image_path)
        st.write("caso não tenha imagem faça o download")
        # Criar o botão de download
        st.download_button(
            label="Baixar Imagem Teste",
            data=image_bytes,
            mime="image/jpg"  # Tipo MIME da imagem (ajuste conforme necessário)
        )

    models = [ 
        "VGG-Face",
        "Facenet",
        "Facenet512",
        "OpenFace",
        "DeepFace",
        "DeepID",
        "ArcFace",
        "Dlib",
        "SFace",
        "GhostFaceNet",
        "Buffalo_L",
    ]

    backends = [  
        "opencv",
        "ssd",
        "dlib",
        "mtcnn",
        "fasion",
        "retinaface",
        "mediapipe",
        "yolov8",
        'yolov11n',
        "yolov11s",
        "yolov11m",
        "fastmtcnn",
        "yunet",
        "centerface",
    ]

    results = None  # Inicializar a variável results

    if testeimg is not None:
        results = DeepFace.verify(
            img1_path=testeimg,
            img2_path="teste2.jpg",
            model_name=models[3], 
            enforce_detection=False,
            detector_backend=backends[0],
            distance_metric="cosine"
        )
    else:
        st.write("Por favor, carregue uma imagem para comparação.")
    
    col3, col4 = st.columns(spec=[1,1])

    with col3:
        if results is not None:
            st.write(results)
    with col4:
        if testeimg is not None:
            st.image(testeimg, width=300)
            if results and results["verified"]:
                st.write("Bem vindo")
            else:
                st.write("Não é a mesma pessoa. Por favor, faça o cadastro.")
                if st.button("Cadastrar"):
                    # Definir o parâmetro de consulta 'page' como 'cadastro'
                    
        # st.query_params(page=cadastro.app())
                    pass