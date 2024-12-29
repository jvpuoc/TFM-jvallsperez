import xml.etree.ElementTree as ET
import re
import os

def procesar_xml(xml_file, output_file="salida_unica_6017_6032.txt"):
    empty = False

    if os.path.getsize(xml_file) == 0:
        empty = True
        print(xml_file + " was an empty file")

    if not empty:

        # Parsear el archivo XML
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Crear una lista para almacenar las URL
        urls = []

        # Buscar todos los hosts y extraer IP y puerto
        for host in root.findall(".//host"):
            ip = host.find(".//address").get("addr")
            port = host.find(".//port").get("portid")
            
            # Determinar el esquema (http o https) en función del puerto
            if port in ["443", "8443"]:
                url = f"https://{ip}:{port}"
            else:
                url = f"http://{ip}:{port}"
            
            urls.append(url)

        # Escribir las URLs en el archivo de salida, agregando al archivo existente
        with open(output_file, "a") as f:
            for url in urls:
                f.write(url + "\n")

        print(f"URLs del archivo '{xml_file}' agregadas a '{output_file}'.")

# filename = ".indicar nombre del archivo a procesar"
procesar_xml(filename)

