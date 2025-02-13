# 📝 XML to JSON Converter

&#x20;

Este é um script Python que converte arquivos XML em JSON de forma automatizada. Ele processa os arquivos XML de uma pasta específica, salva os arquivos JSON gerados em outra pasta e move os XMLs convertidos para uma subpasta de arquivos finalizados.

---

## 🚀 Como usar

### 1️⃣ Clonar o repositório

```bash
  git clone https://github.com/leonardo-27-dev/convert-xml-to-json-py
  cd convert-xml-to-json-py
```

### 2️⃣ Instalar dependências

Antes de rodar o script, instale as dependências necessárias:

```bash
  pip install -r requirements.txt
```

### 3️⃣ Executar o script

Para converter os arquivos XML:

```bash
  python convert_xml_to_json.py
```

### 4️⃣ Usar com Docker

Você também pode usar o Docker para rodar o projeto:

1. Construa a imagem Docker:

    ```bash
    docker-compose build
    ```

2. Inicie o contêiner:

    ```bash
    docker-compose up
    ```

---

## 📁 Estrutura do projeto

```
📦 seu-repositorio
 ┣ 📂 xmls              # Pasta onde você coloca os arquivos XML a serem convertidos
 ┃ ┗ 📂 done            # Após a conversão, os XMLs serão movidos para esta pasta
 ┣ 📂 xmls-jsons        # Aqui serão salvos os arquivos JSON gerados
 ┣ 📜 convert_xml_to_json.py  # Script principal de conversão
 ┣ 📜 requirements.txt  # Lista de dependências
 ┣ 📜 Dockerfile        # Dockerfile para criar a imagem Docker
 ┣ 📜 docker-compose.yml # Arquivo de configuração do Docker Compose
 ┗ 📜 README.md         # Documentação do projeto
```

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python**
- 📄 **xmltodict** para converter XML para JSON
- 📁 **os** e **shutil** para manipulação de arquivos e diretórios
- 🐳 **Docker** para containerização

---

## 📌 Observações

- Certifique-se de colocar seus arquivos XML na pasta `xmls` antes de rodar o script.
- Após a conversão, os arquivos JSON estarão disponíveis em `xmls-jsons`.
- Os arquivos XML processados serão movidos para `xmls/done`.

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

💡 **Contribuições são bem-vindas!** Se encontrar algum problema ou quiser sugerir melhorias, fique à vontade para abrir uma issue ou pull request.

✨ *Happy coding!* 🚀