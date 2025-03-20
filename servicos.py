import streamlit as st
from deepface import DeepFace
import sqlite3


def app():

    pass

# 1. Entregas
# Transporte de Documentos : Entrega de contratos, relatórios ou correspondências importantes.
# Distribuição de Materiais : Transporte de equipamentos, amostras ou produtos entre unidades.
# Logística de Pequenas Encomendas : Serviços rápidos de entrega, como malotes ou pacotes.
# Coleta de Amostras : Retirada de materiais ou itens para análise em laboratórios externos.

# 2. Reforma e Construção
# Pequenas Reparos : Consertos simples, como troca de lâmpadas, ajustes em portas ou reparos hidráulicos.
# Obras Estruturais : Ampliações, reformas ou adaptações de espaços físicos.
# Instalação de Equipamentos : Montagem de estruturas para máquinas, laboratórios ou escritórios.
# Pintura e Acabamento : Renovação estética de paredes, pisos ou áreas comuns.

# 3. Limpeza
# Limpeza Geral : Serviços de rotina para manter as instalações higienizadas.
# Limpeza Pesada : Lavagem de vidros, carpetes, ou áreas críticas (ex.: salas limpas).
# Desinfecção : Higienização especial para prevenir contaminações (ex.: após obras ou eventos).
# Descarte de Resíduos : Coleta e destinação adequada de lixo ou materiais recicláveis.

# 4. Manutenção
# Manutenção Elétrica : Reparos em instalações elétricas, painéis ou sistemas de energia.
# Manutenção Hidráulica : Conserto de vazamentos, encanamentos ou sistemas de drenagem.
# Manutenção de Ar Condicionado : Instalação, limpeza ou reparo de sistemas de climatização.
# Manutenção de Elevadores : Inspeção e reparo de elevadores ou plataformas de acessibilidade.

# 5. Eventos e Recepção
# Montagem de Estruturas : Instalação de stands, palcos ou mobiliário para eventos.
# Decoração Temporária : Preparação de espaços para conferências, workshops ou reuniões.
# Buffet e Alimentação : Fornecimento de refeições ou coffee breaks durante eventos.
# Recepção Temporária : Contratação de recepcionistas para atender visitantes durante atividades específicas.

# 6. Serviços Especializados
# Controle de Pragas : Dedetização ou controle de insetos e roedores nas instalações.
# Jardinagem e Paisagismo : Cuidados com áreas verdes, plantas ou jardins.
# Segurança Temporária : Contratação de vigilantes para eventos ou períodos específicos.
# Inspeção Técnica : Avaliação de condições de segurança, estrutura ou conformidade regulatória.

# 7. Outros Serviços
# Transporte de Pessoas : Serviços de motorista ou transporte para visitantes/executivos.
# Serviços de Cópia e Impressão : Impressão de materiais para eventos ou uso interno.
# Assistência Técnica : Reparo de equipamentos eletrônicos ou eletrodomésticos.
# Reciclagem e Sustentabilidade : Coleta de resíduos recicláveis ou implementação de práticas sustentáveis.






# import streamlit as st

# # Lista de tipos de serviços
# servicos = [
#     "Entregador",
#     "Reforma e Construção",
#     "Limpeza",
#     "Manutenção",
#     "Eventos e Recepção",
#     "Controle de Pragas",
#     "Jardinagem",
#     "Outro"
# ]

# # Interface do Streamlit
# st.title("Cadastro de Prestadores de Serviço Externos")

# nome_prestador = st.text_input("Nome do Prestador")
# tipo_servico = st.selectbox("Tipo de Serviço", servicos)
# data_servico = st.date_input("Data do Serviço")
# observacoes = st.text_area("Observações", placeholder="Descreva detalhes adicionais...")

# if st.button("Registrar"):
#     st.success(f"Prestador {nome_prestador} registrado para: {tipo_servico}")
#     st.write(f"Data do Serviço: {data_servico}")
#     if observacoes:
#         st.write(f"Observações: {observacoes}")








# import sqlite3

# # Função para inicializar o banco de dados
# def init_db():
#     conn = sqlite3.connect('prestadores.db')
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS prestadores (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT NOT NULL,
#             servico TEXT NOT NULL,
#             data TEXT NOT NULL,
#             observacoes TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Função para adicionar um novo prestador
# def add_prestador(nome, servico, data, observacoes):
#     conn = sqlite3.connect('prestadores.db')
#     c = conn.cursor()
#     c.execute('INSERT INTO prestadores (nome, servico, data, observacoes) VALUES (?, ?, ?, ?)', 
#               (nome, servico, data, observacoes))
#     conn.commit()
#     conn.close()

# # Inicializa o banco de dados
# init_db()

# # Interface do Streamlit
# st.title("Cadastro de Prestadores de Serviço Externos")

# nome_prestador = st.text_input("Nome do Prestador")
# tipo_servico = st.selectbox("Tipo de Serviço", servicos)
# data_servico = st.date_input("Data do Serviço")
# observacoes = st.text_area("Observações", placeholder="Descreva detalhes adicionais...")

# if st.button("Registrar"):
#     add_prestador(nome_prestador, tipo_servico, str(data_servico), observacoes)
#     st.success(f"Prestador {nome_prestador} registrado com sucesso!")





































