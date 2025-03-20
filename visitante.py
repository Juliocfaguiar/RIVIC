import streamlit as st
from deepface import DeepFace



def app():

    pass

# 1. Eventos Institucionais
# Palestras e Conferências : Apresentações sobre temas relevantes, como inovação tecnológica, sustentabilidade ou tendências de mercado.
# Workshops e Treinamentos : Atividades práticas para capacitar participantes em áreas específicas.
# Seminários Técnicos : Discussões técnicas ou científicas voltadas para especialistas ou profissionais do setor.
# Feiras e Exposições : Mostras de produtos, serviços ou tecnologias desenvolvidas pela empresa.

# 2. Visitas Técnicas
# Visitas Guiadas : Apresentação das instalações, laboratórios ou centros de pesquisa da empresa.
# Demonstrações Tecnológicas : Exibição de projetos, protótipos ou soluções inovadoras desenvolvidas pelo IPT.
# Intercâmbio de Conhecimento : Troca de experiências entre especialistas da empresa e visitantes externos.

# 3. Parcerias e Colaborações
# Reuniões de Negócios : Encontros para discutir parcerias, contratos ou projetos conjuntos.
# Networking : Oportunidades para conectar-se com outros profissionais, empresas ou instituições.
# Assinatura de Acordos : Formalização de colaborações estratégicas, convênios ou memorandos de entendimento.

# 4. Educação e Capacitação
# Programas de Estágio : Recebimento de estudantes para conhecerem o ambiente de trabalho e oportunidades de estágio.
# Visitas Escolares : Recebimento de alunos e professores para apresentar aplicações práticas dos conhecimentos acadêmicos.
# Cursos de Extensão : Oficinas ou cursos voltados para o público externo.

# 5. Comunicação e Relacionamento
# Eventos de Relacionamento : Recepção de stakeholders, investidores ou parceiros para fortalecer vínculos.
# Apresentação de Resultados : Divulgação de avanços, relatórios ou conquistas da empresa.
# Comemorações Especiais : Celebração de datas importantes, como aniversário da empresa ou marcos históricos.

# 6. Consultoria e Serviços
# Atendimento a Clientes : Recepção de clientes ou parceiros interessados em serviços oferecidos pelo IPT.
# Apoio Técnico : Discussão de demandas específicas relacionadas a consultoria, certificação ou desenvolvimento de projetos.
# Diagnósticos e Avaliações : Realização de análises técnicas ou auditorias solicitadas por terceiros.

# 7. Projetos e Pesquisas
# Colaboração em Pesquisa : Integração de visitantes em projetos de pesquisa conjunta.
# Validação de Tecnologias : Testes ou validações de produtos ou processos desenvolvidos por terceiros.
# Desenvolvimento de Protótipos : Trabalho conjunto na criação ou aprimoramento de protótipos.

# 8. Marketing e Divulgação
# Lançamento de Produtos/Serviços : Apresentação de novidades desenvolvidas pelo IPT.
# Tour de Imprensa : Recepção de jornalistas ou influenciadores para divulgar iniciativas da empresa.
# Campanhas de Sustentabilidade : Promoção de práticas e projetos alinhados aos Objetivos de Desenvolvimento Sustentável (ODS).

# 9. Outras Finalidades
# Entrevistas e Processos Seletivos : Recepção de candidatos para entrevistas de emprego ou programas de trainee.
# Auditorias e Inspeções : Recebimento de órgãos reguladores ou entidades certificadoras.
# Participação em Comitês ou Conselhos : Convite para integrar grupos de discussão ou tomada de decisões.









# finalidades = [
#     "Evento",
#     "Palestra",
#     "Visita Técnica",
#     "Reunião de Negócios",
#     "Treinamento",
#     "Parceria",
#     "Outro"
# ]

# st.title("Cadastro de Visitantes")
# nome = st.text_input("Nome do Visitante")
# finalidade = st.selectbox("Finalidade da Visita", finalidades)

# if st.button("Registrar"):
#     st.success(f"Visitante {nome} registrado para: {finalidade}")