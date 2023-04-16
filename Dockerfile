# Usar a imagem base do Python
FROM python:3.8

# Copiar o arquivo app.py para o contêiner
COPY main.py /main.py
COPY test.py /test.py

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt /requirements.txt

# Instalar as dependências
RUN pip install -r /requirements.txt

# Definir o comando para executar a aplicação
CMD ["python", "/main.py"]