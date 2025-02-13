import os
import time
import xmltodict
import json
import shutil

# Definir diretório base dentro do contêiner
base_directory = os.path.dirname(os.path.abspath(__file__))
xml_input_dir = os.path.join(base_directory, "xmls")
xml_done_dir = os.path.join(xml_input_dir, "done")
json_output_dir = os.path.join(base_directory, "xmls-jsons")

# Criar diretórios caso não existam
os.makedirs(xml_input_dir, exist_ok=True)
os.makedirs(xml_done_dir, exist_ok=True)
os.makedirs(json_output_dir, exist_ok=True)

print("🟢 Monitorando a pasta XMLs para conversão...")

while True:
    for xml_filename in os.listdir(xml_input_dir):
        if not xml_filename.endswith(".xml"):
            continue

        xml_path = os.path.join(xml_input_dir, xml_filename)
        
        with open(xml_path, "r", encoding="utf-8") as file:
            xml_content = file.read()

        json_data = json.dumps(xmltodict.parse(xml_content), indent=4, ensure_ascii=False)
        
        json_filename = xml_filename.replace(".xml", ".json")
        json_path = os.path.join(json_output_dir, json_filename)

        with open(json_path, "w", encoding="utf-8") as json_file:
            json_file.write(json_data)

        shutil.move(xml_path, os.path.join(xml_done_dir, xml_filename))

        print(f"✅ Convertido: {xml_filename} -> {json_filename}")

    time.sleep(10)  # Verifica a cada 10 segundos por novos arquivos
