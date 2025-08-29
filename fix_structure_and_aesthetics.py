import re
import os

def fix_structure_and_aesthetics():
    print("CORRIGIENDO ESTRUCTURA Y ESTÉTICA")
    print("=" * 45)
    
    # Leer archivo con swipe
    with open("roxana_certificados_zoom.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Leer archivo original para extraer contenido faltante
    with open("artist_book_actualizado.html", "r", encoding="utf-8") as f:
        original = f.read()
    
    # 1. CORREGIR FOTO DE ROXANA - centrar en círculo
    print("1. Corrigiendo posición de foto de Roxana...")
    
    # Encontrar y corregir CSS de la foto
    foto_css_fix = """
        .profile-photo {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            object-position: center;
            border: 4px solid white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            margin: 0 auto 30px auto;
            display: block;
        }"""
    
    # Reemplazar o agregar CSS de la foto
    if '.profile-photo' in contenido:
        patron_foto_css = r'\.profile-photo \{[^}]*\}'
        contenido = re.sub(patron_foto_css, foto_css_fix.strip().replace('\n        ', '\n            '), contenido)
    else:
        contenido = contenido.replace('</style>', foto_css_fix + '\n        </style>')
    
    # 2. EXTRAER DECLARACIÓN DE ARTISTA del original
    print("2. Extrayendo Declaración de Artista...")
    
    # Buscar la declaración en el HTML original
    patron_declaracion = r'<h2[^>]*>Declaración de Artista</h2>(.*?)(?=<h2|<div class="section"|\s*</div>\s*<div|$)'
    match_declaracion = re.search(patron_declaracion, original, re.DOTALL | re.IGNORECASE)
    
    declaracion_content = """
                <h2>Declaración de Artista</h2>
                <div class="artist-statement">
                    <blockquote>
                        "Somos seres complejos, esto motiva mi imaginación generando teorías, 
                        poesía, imágenes... Que luego se transforman en obras"
                    </blockquote>
                    <p>Entiendo la vida como un segmento (inicio-final), la manera en que la transito es la que determinará mi ser.</p>
                    <p>Asumirme en el presente me genera una pregunta: ¿Qué hay después?</p>
                    <p>Estoy, existo, el problema es "El obstáculo"..</p>
                    <p>...Trabajo y me aturdo para sobrevivirlo</p>
                    <p>...Me someto a la realidad y me encierro</p>
                    <p>...Pendular eternamente en la desidia que él me genera, o negar su presencia y navegar en su densitud.</p>
                    <p>Aunque indefectiblemente sigo el camino, siempre me pregunto ¿Qué hay después?</p>
                </div>"""
    
    if match_declaracion:
        declaracion_content = match_declaracion.group(0)
    
    # 3. REESTRUCTURAR PÁGINAS - agregar Declaración después de datos personales
    print("3. Reestructurando páginas...")
    
    # Modificar la estructura para incluir más páginas
    nueva_estructura = '''
        <div class="page" id="page1">
            <div class="profile-container">
                <img src="FOTO RO.jpg" alt="Roxana Matilde Romano" class="profile-photo">
                <h1>ROXANA MATILDE ROMANO</h1>
                <p class="subtitle">Artista Visual</p>
                
                <div class="contact-info">
                    <a href="tel:+5492615988180" class="contact-item">
                        📞 +54 9 261-5988180
                    </a>
                    <a href="mailto:roxanamatilderomano@gmail.com" class="contact-item">
                        ✉️ roxanamatilderomano@gmail.com
                    </a>
                    <div class="contact-item">
                        📍 Manuel A. Sáez 2101 - Las Heras - Mendoza
                    </div>
                    <a href="https://youtube.com/@roxanamatilderomano" target="_blank" class="contact-item">
                        🎥 @roxanamatilderomano
                    </a>
                    <a href="https://instagram.com/roxanamatilderomano2017" target="_blank" class="contact-item">
                        📸 @roxanamatilderomano2017
                    </a>
                </div>
            </div>
        </div>

        <div class="page" id="page2">
            <div class="content">''' + declaracion_content + '''
            </div>
        </div>

        <div class="page" id="page3">
            <div class="content">
                <h2>Índice</h2>
                <div class="index-menu">
                    <button onclick="goToPage(4)" class="index-button">OBRAS</button>
                    <button onclick="goToPage(5)" class="index-button">CERTIFICADOS</button>
                    <button onclick="goToPage(6)" class="index-button">PRÓXIMOS EVENTOS</button>
                    <button onclick="goToPage(7)" class="index-button">CLASES</button>
                </div>
            </div>
        </div>

        <div class="page" id="page4">
            <div class="content">
                <h2>Catálogo de Obras</h2>
                <div id="obrasContainer" class="obras-grid"></div>
            </div>
        </div>

        <div class="page" id="page5">
            <div class="content">
                <h2>Certificados</h2>
                <div id="certificadosContainer" class="obras-grid"></div>
            </div>
        </div>

        <div class="page" id="page6">
            <div class="content">
                <h2>Próximos Eventos</h2>
                <div class="events-container">
                    <p>Próximamente se anunciarán nuevos eventos y exposiciones.</p>
                    <p>Mantente conectado a través de nuestras redes sociales para no perderte las últimas novedades.</p>
                </div>
            </div>
        </div>

        <div class="page" id="page7">
            <div class="content">
                <h2>Clases</h2>
                <div class="classes-container">
                    <h3>ATELIER</h3>
                    <p><em>Un espacio donde la luz respira...</em></p>
                    <p><strong>B</strong>añado por la generosa luz del sol mendocino, es mucho más que un estudio: es un refugio para el espíritu creativo. Adentrarse en su bohemia es sumergirse en un ambiente introspectivo, en donde tu vocabulario profundo podrá expresarse sobre el lienzo virgen.</p>
                    <p>Ya seas un principiante curioso o un creador experimentado, aquí encontrarás un espacio inspirador y pacífico.</p>
                    <p>Descubre tu potencial y nutre tu talento en un entorno estimulante y acogedor.</p>
                    <p>Estás invitado para que juntos exploremos tu propia abstracción artística.</p>
                    <p><strong>ROXANA MATILDE ROMANO</strong></p>
                </div>
            </div>
        </div>'''
    
    # Reemplazar la estructura actual de páginas
    patron_paginas = r'<div class="page".*?</div>\s*</div>\s*</div>'
    contenido = re.sub(patron_paginas, nueva_estructura.strip(), contenido, flags=re.DOTALL)
    
    # 4. AGREGAR CSS PARA NUEVOS ELEMENTOS
    print("4. Agregando estilos...")
    
    nuevos_estilos = """
        .artist-statement {
            text-align: left;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .artist-statement blockquote {
            font-style: italic;
            font-size: 1.2em;
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
        }
        
        .index-menu {
            display: flex;
            flex-direction: column;
            gap: 20px;
            max-width: 400px;
            margin: 0 auto;
        }
        
        .index-button {
            background: rgba(255,255,255,0.2);
            border: 2px solid rgba(255,255,255,0.3);
            color: white;
            padding: 15px 30px;
            border-radius: 10px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .index-button:hover {
            background: rgba(255,255,255,0.3);
            border-color: rgba(255,255,255,0.5);
            transform: translateY(-2px);
        }
        
        .events-container, .classes-container {
            max-width: 800px;
            margin: 0 auto;
            text-align: left;
            line-height: 1.6;
        }
        
        .classes-container h3 {
            text-align: center;
            font-size: 1.5em;
            margin-bottom: 20px;
        }
        
        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 30px;
        }
        
        .contact-item {
            background: rgba(255,255,255,0.1);
            padding: 12px 20px;
            border-radius: 25px;
            text-decoration: none;
            color: white;
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .contact-item:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }"""
    
    contenido = contenido.replace('</style>', nuevos_estilos + '\n        </style>')
    
    # 5. ACTUALIZAR INDICADOR DE PÁGINAS
    print("5. Actualizando navegación...")
    
    # Cambiar el total de páginas de 4 a 7
    contenido = contenido.replace('currentPage + " / 4"', 'currentPage + " / 7"')
    contenido = contenido.replace('currentPage === 4', 'currentPage === 7')
    contenido = contenido.replace('if (currentPage < 4)', 'if (currentPage < 7)')
    
    # Agregar función goToPage para el índice
    goto_function = '''
        function goToPage(pageNum) {
            currentPage = pageNum;
            updateDisplay();
        }'''
    
    contenido = contenido.replace('// Navegación por teclado', goto_function + '\n        \n        // Navegación por teclado')
    
    # Guardar archivo corregido
    with open("roxana_estructura_completa.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("=" * 45)
    print("ESTRUCTURA CORREGIDA")
    print("Archivo: roxana_estructura_completa.html")
    print("\nNuevas páginas:")
    print("1. Datos personales con foto centrada")
    print("2. Declaración de Artista")  
    print("3. Índice navegable")
    print("4. Catálogo de Obras")
    print("5. Certificados")
    print("6. Próximos Eventos")
    print("7. Clases y Atelier")
    print("\nPrueba el archivo antes de subir")

if __name__ == "__main__":
    fix_structure_and_aesthetics()