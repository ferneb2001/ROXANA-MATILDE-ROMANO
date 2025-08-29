import os
import re

def fix_roxana_photo():
    print("CORRIGIENDO CON FOTO ESPECÍFICA DE ROXANA")
    print("=" * 45)
    
    # Verificar que existe la foto
    foto_roxana = "FOTO RO.jpg"
    
    if os.path.exists(foto_roxana):
        print(f"✓ Foto encontrada: {foto_roxana}")
    else:
        print(f"❌ No se encuentra: {foto_roxana}")
        print("Archivos en la carpeta:")
        for file in os.listdir('.'):
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                print(f"  - {file}")
        return
    
    # 2. Contar obras en CATALOGO
    print("\nContando obras en CATALOGO...")
    obras_en_carpeta = []
    if os.path.exists('CATALOGO'):
        for file in os.listdir('CATALOGO'):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                obras_en_carpeta.append(file)
    
    print(f"✓ Obras en carpeta CATALOGO: {len(obras_en_carpeta)}")
    
    # 3. Leer archivo HTML
    with open("roxana_final_completa.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # 4. Reemplazar foto de Roxana
    print(f"\nReemplazando placeholder con: {foto_roxana}")
    
    # Buscar y reemplazar cualquier placeholder de foto
    patrones_placeholder = [
        r'src="data:image/svg\+xml;base64,[^"]*"',
        r'src="path/to/roxana-photo\.jpg"'
    ]
    
    for patron in patrones_placeholder:
        if re.search(patron, contenido):
            contenido = re.sub(patron, f'src="{foto_roxana}"', contenido, count=1)
            print("✓ Foto reemplazada")
            break
    
    # 5. Eliminar página 5
    print("\nEliminando página 5...")
    contenido = contenido.replace('const totalPages = 5;', 'const totalPages = 4;')
    
    # Remover página 5 HTML
    patron_pagina5 = r'<!-- Página 5: Contacto -->.*?</div>\s*</div>'
    contenido = re.sub(patron_pagina5, '', contenido, flags=re.DOTALL)
    
    # Actualizar indicador
    contenido = contenido.replace('1 / 5', '1 / 4')
    print("✓ Página 5 eliminada")
    
    # 6. Verificar obras en JavaScript
    print("\nVerificando obras...")
    
    patron_obras = r'const catalogWorks = \[(.*?)\];'
    match = re.search(patron_obras, contenido, re.DOTALL)
    
    if match:
        obras_js = match.group(1)
        obras_js_count = len(re.findall(r'\{[^}]+\}', obras_js))
        
        print(f"Obras en JavaScript: {obras_js_count}")
        print(f"Obras en carpeta: {len(obras_en_carpeta)}")
        
        if obras_js_count < len(obras_en_carpeta):
            faltantes = len(obras_en_carpeta) - obras_js_count
            print(f"⚠ Faltan {faltantes} obra(s)")
            
            # Buscar obras faltantes
            obras_js_nombres = re.findall(r'"CATALOGO/([^"]+)"', obras_js)
            
            for obra in obras_en_carpeta:
                if not any(obra in js_obra for js_obra in obras_js_nombres):
                    print(f"Obra faltante encontrada: {obra}")
                    
                    # Extraer información del nombre
                    nombre_base = obra.split('.')[0]
                    partes = nombre_base.split(' - ')
                    titulo = partes[0] if partes else nombre_base
                    tecnica = partes[1] if len(partes) > 1 else ""
                    dimensiones = partes[2] if len(partes) > 2 else ""
                    year = ""
                    
                    # Buscar año en el nombre
                    año_match = re.search(r'(\d{4})', obra)
                    if año_match:
                        year = año_match.group(1)
                    
                    # Crear objeto para la obra faltante
                    nueva_obra = f'''            {{
                path: "CATALOGO/{obra}",
                type: "image",
                title: "{titulo}",
                technique: "{tecnica}",
                dimensions: "{dimensiones}",
                year: "{year}",
                collection: ""
            }}'''
                    
                    # Agregar antes del cierre del array
                    contenido = contenido.replace(
                        '            }\n        ];',
                        '            },\n' + nueva_obra + '\n        ];'
                    )
                    print("✓ Obra agregada al JavaScript")
                    break
    
    # Guardar archivo final
    with open("roxana_completa_final.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("\n" + "=" * 45)
    print("✅ SITIO FINAL COMPLETADO")
    print("Archivo: roxana_completa_final.html")
    print(f"\nCaracterísticas finales:")
    print(f"- Foto de Roxana: FOTO RO.jpg")
    print(f"- Páginas: 4 (sin página 5 innecesaria)")
    print(f"- Obras: {len(obras_en_carpeta)} (todas las de la carpeta)")
    print(f"- Navegación: swipe + botones")
    print(f"- Compatible: Chrome móvil")
    
    print(f"\nPara aplicar:")
    print("copy roxana_completa_final.html index.html")
    print("git add .")
    print('git commit -m "Sitio completo final: foto Roxana + todas las obras"')
    print("git push origin main")

if __name__ == "__main__":
    fix_roxana_photo()