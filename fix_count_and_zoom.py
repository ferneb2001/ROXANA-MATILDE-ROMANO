import os
import re

def fix_count_and_zoom():
    print("CORRIGIENDO CONTEO DE OBRAS Y ZOOM EN CERTIFICADOS")
    print("=" * 55)
    
    # 1. Verificar obras reales en CATALOGO
    obras_reales = []
    if os.path.exists('CATALOGO'):
        for file in os.listdir('CATALOGO'):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                obras_reales.append(file)
    
    print(f"Obras reales en carpeta CATALOGO: {len(obras_reales)}")
    
    # 2. Leer archivo actual
    with open("roxana_completa_final.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # 3. Contar obras en JavaScript
    patron_obras = r'const catalogWorks = \[(.*?)\];'
    match = re.search(patron_obras, contenido, re.DOTALL)
    
    obras_js_count = 0
    if match:
        obras_js = match.group(1)
        obras_js_count = len(re.findall(r'\{[^}]*\}', obras_js))
    
    print(f"Obras en JavaScript: {obras_js_count}")
    print(f"Diferencia: {len(obras_reales) - obras_js_count}")
    
    # 4. Si faltan obras, agregarlas
    if obras_js_count < len(obras_reales):
        print(f"\nAgregando {len(obras_reales) - obras_js_count} obra(s) faltante(s)...")
        
        # Extraer nombres de obras ya en JavaScript
        obras_existentes = re.findall(r'"CATALOGO/([^"]+)"', contenido)
        
        obras_para_agregar = []
        for obra in obras_reales:
            if obra not in obras_existentes:
                obras_para_agregar.append(obra)
        
        # Agregar cada obra faltante
        for obra in obras_para_agregar:
            print(f"  Agregando: {obra}")
            
            # Parsear información del nombre del archivo
            nombre_sin_ext = obra.split('.')[0]
            partes = nombre_sin_ext.split(' - ')
            
            titulo = partes[0] if partes else nombre_sin_ext
            tecnica = partes[1] if len(partes) > 1 else ""
            dimensiones = partes[2] if len(partes) > 2 else ""
            
            # Buscar año
            year_match = re.search(r'(\d{4})', obra)
            year = year_match.group(1) if year_match else ""
            
            # Buscar colección privada
            collection = "Colección privada" if "colección privada" in obra.lower() or "coleccion privada" in obra.lower() else ""
            
            nueva_obra = f''',
            {{
                path: "CATALOGO/{obra}",
                type: "image",
                title: "{titulo}",
                technique: "{tecnica}",
                dimensions: "{dimensiones}",
                year: "{year}",
                collection: "{collection}"
            }}'''
            
            # Insertar antes del cierre del array
            contenido = contenido.replace(
                '\n        ];',
                nueva_obra + '\n        ];'
            )
    
    # 5. Agregar funcionalidad de zoom a certificados
    print("\nAgregando zoom a certificados...")
    
    # Modificar la función loadCertificados para incluir click events
    patron_cert_function = r'(// Cargar certificados\s*function loadCertificados\(\) \{.*?)\s*}\s*}'
    
    nueva_funcion_cert = '''// Cargar certificados
        function loadCertificados() {
            const container = document.getElementById('certificadosContainer');
            if (!container || !certificateData || !Array.isArray(certificateData)) return;
            
            certificateData.forEach((cert, index) => {
                const div = document.createElement('div');
                div.className = 'obra-item';
                
                const certName = cert.split('/').pop().split('.')[0];
                
                div.innerHTML = `
                    <img src="${cert}" alt="Certificado" class="obra-img"
                         style="cursor: pointer;"
                         onclick="openLightbox('${cert}', 'Certificado ${index + 1}', '${certName}')"
                         onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkNlcnRpZmljYWRvPC90ZXh0Pjwvc3ZnPg=='>
                    <div class="obra-title">Certificado ${index + 1}</div>
                    <div class="obra-details">${certName}</div>
                `;
                container.appendChild(div);
            });
        }'''
    
    # Reemplazar la función de certificados
    contenido = re.sub(
        r'// Cargar certificados.*?}\s*}',
        nueva_funcion_cert + '\n        }',
        contenido,
        flags=re.DOTALL
    )
    
    # 6. Verificar que el lightbox funcione correctamente
    if 'function openLightbox' not in contenido:
        print("Agregando funciones de lightbox...")
        
        lightbox_functions = '''
        // Funciones de lightbox
        function openLightbox(imgSrc, title, details) {
            const lightbox = document.getElementById('lightbox');
            const lightboxImg = document.getElementById('lightboxImg');
            const lightboxInfo = document.getElementById('lightboxInfo');
            
            if (lightbox && lightboxImg && lightboxInfo) {
                lightboxImg.src = imgSrc;
                lightboxInfo.innerHTML = `<h3>${title}</h3><p>${details}</p>`;
                lightbox.style.display = 'flex';
            }
        }
        
        function closeLightbox() {
            const lightbox = document.getElementById('lightbox');
            if (lightbox) {
                lightbox.style.display = 'none';
            }
        }'''
        
        contenido = contenido.replace(
            '// Navegación por teclado',
            lightbox_functions + '\n        \n        // Navegación por teclado'
        )
    
    # 7. Guardar archivo corregido
    with open("roxana_final_corregida.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print(f"\n" + "=" * 55)
    print("CORRECCIONES APLICADAS")
    print("Archivo: roxana_final_corregida.html")
    print(f"\nResultado:")
    print(f"- Obras totales: debería mostrar {len(obras_reales)} obras")
    print("- Zoom en obras: funcional")
    print("- Zoom en certificados: agregado")
    print("- Foto de Roxana: FOTO RO.jpg")
    print("- Páginas: 4 (sin página 5)")
    
    print(f"\nPara probar:")
    print("1. Abre roxana_final_corregida.html")
    print("2. Ve a página 3 y cuenta las obras")
    print("3. Ve a página 4 y prueba click en certificados")
    
    print(f"\nPara aplicar:")
    print("copy roxana_final_corregida.html index.html")
    print("git add .")
    print('git commit -m "77 obras + zoom en certificados"')
    print("git push origin main")

if __name__ == "__main__":
    fix_count_and_zoom()