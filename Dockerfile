# Usar a imagem oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . /app

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Criar os diretórios necessários
RUN mkdir -p ~/conversor-de-xml-para-json/xmls/done ~/conversor-de-xml-para-json/xmls-jsons

# Definir o comando padrão para rodar o script
CMD ["python", "/app/convert_xml_to_json.py"]
