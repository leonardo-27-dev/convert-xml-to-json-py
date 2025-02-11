import xmltodict
import json
import os
import shutil

# Diretório base flexível (usando o diretório do script como referência)
base_directory = os.path.dirname(os.path.abspath(__file__))
xml_input_dir = os.path.join(base_directory, "xmls")
xml_done_dir = os.path.join(xml_input_dir, "done")
json_output_dir = os.path.join(base_directory, "xmls-jsons")

# Criar pastas se não existirem
os.makedirs(xml_input_dir, exist_ok=True)
os.makedirs(xml_done_dir, exist_ok=True)
os.makedirs(json_output_dir, exist_ok=True)

# Processar arquivos XML
for xml_filename in os.listdir(xml_input_dir):
    if not xml_filename.endswith(".xml"):
        continue
    
    xml_path = os.path.join(xml_input_dir, xml_filename)
    
    # Ler o conteúdo do arquivo XML
    with open(xml_path, "r", encoding="utf-8") as file:
        xml_content = file.read()
    
    # Converter XML para JSON
    json_data = json.dumps(xmltodict.parse(xml_content), indent=4, ensure_ascii=False)
    
    # Criar o arquivo JSON
    json_filename = xml_filename.replace(".xml", ".json")
    json_path = os.path.join(json_output_dir, json_filename)
    
    with open(json_path, "w", encoding="utf-8") as json_file:
        json_file.write(json_data)
    
    # Mover XML para a pasta done
    shutil.move(xml_path, os.path.join(xml_done_dir, xml_filename))
    
    print(f"Conversão concluída! JSON salvo em: {json_path}")
