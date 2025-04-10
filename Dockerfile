# Usa uma imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala o Flask
RUN pip install flask

# Expõe a porta que o app usará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
