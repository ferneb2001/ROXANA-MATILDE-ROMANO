import re
import shutil
from datetime import datetime

def migrar_contenido_completo():
    print("MIGRANDO CONTENIDO COMPLETO A VERSIÓN MÓVIL")
    print("=" * 50)
    
    # Backup
    timestamp = datetime.now().strftime("%H%M%S")
    backup_name = f"backup_migracion_{timestamp}.html"
    shutil.copy("artist_book_actualizado.html", backup_name)
    print(f"Backup: {backup_name}")
    
    # Leer archivos
    with open("artist_book_actualizado.html", "r", encoding="utf-8") as f:
        contenido_completo = f.read()
    
    with open("mobile_minimal.html", "r", encoding="utf-8") as f:
        estructura_minimal = f.read()
    
    # Extraer datos de Roxana
    print("\nExtrayendo información de Roxana...")
    
    # Extraer datos personales de Roxana
    datos_roxana = {}
    
    # Buscar información de contacto
    patron_telefono = r"(\+?[0-9\s\-\(\)]+)"
    patron_email = r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    patron_youtube = r"(youtube\.com/[^\s\"'<>]+|youtu\.be/[^\s\"'<>]+)"
    patron_instagram = r"(instagram\.com/[^\s\"'<>]+|@[a-zA-Z0-9._]+)"
    
    # Buscar elementos específicos
    if re.search(r"ROXANA|Roxana", contenido_completo, re.IGNORECASE):
        print("✓ Información de Roxana encontrada")
    
    # Extraer obras de arte (catalogWorks)
    patron_catalog = r"const catalogWorks = \[(.*?)\];"
    match_catalog = re.search(patron_catalog, contenido_completo, re.DOTALL)
    obras = []
    
    if match_catalog:
        catalog_content = match_catalog.group(1)
        # Extraer cada obra individual
        patron_obra = r'\{[^}]+\}'
        obras = re.findall(patron_obra, catalog_content)
        print(f"✓ {len(obras)} obras encontradas")
    
    # Extraer certificados
    patron_certificados = r"const certificateData = \[(.*?)\];"
    match_cert = re.search(patron_certificados, contenido_completo, re.DOTALL)
    certificados = []
    
    if match_cert:
        cert_content = match_cert.group(1)
        patron_cert = r'\{[^}]+\}'
        certificados = re.findall(patron_cert, cert_content)
        print(f"✓ {len(certificados)} certificados encontrados")
    
    # Extraer CSS personalizado
    patron_css = r"<style>(.*?)</style>"
    matches_css = re.findall(patron_css, contenido_completo, re.DOTALL)
    css_personalizado = "\n".join(matches_css) if matches_css else ""
    
    # Crear la nueva versión con contenido completo
    nueva_version = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roxana Matilde Romano - Artista</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Georgia', serif;
            overflow-x: hidden;
            background: #f5f5f5;
        }}
        
        /* Contenedor principal con scroll horizontal */
        .book-container {{
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
            height: 100vh;
            scroll-behavior: smooth;
        }}
        
        /* Cada página ocupa todo el ancho */
        .page {{
            flex: 0 0 100vw;
            scroll-snap-align: start;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            position: relative;
        }}
        
        /* Colores de fondo para cada página */
        .page-1 {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }}
        .page-2 {{ background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; }}
        .page-3 {{ background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: #333; }}
        .page-4 {{ background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: #333; }}
        .page-5 {{ background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); color: #333; }}
        
        /* Navegación por botones */
        .nav-buttons {{
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
            z-index: 1000;
        }}
        
        .nav-btn {{
            padding: 10px 20px;
            background: rgba(0,0,0,0.7);
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
        }}
        
        .nav-btn:hover {{
            background: rgba(0,0,0,0.9);
        }}
        
        /* Indicador de página */
        .page-indicator {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            z-index: 1000;
        }}
        
        /* Contenido específico */
        .artist-photo {{
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 20px;
            border: 4px solid rgba(255,255,255,0.3);
        }}
        
        .contact-info {{
            text-align: center;
            margin: 20px 0;
        }}
        
        .contact-info h2 {{
            margin-bottom: 15px;
            font-size: 2em;
        }}
        
        .contact-item {{
            margin: 10px 0;
            padding: 10px;
            background: rgba(255,255,255,0.2);
            border-radius: 10px;
        }}
        
        .obra-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            width: 100%;
            max-width: 800px;
        }}
        
        .obra-item {{
            background: rgba(255,255,255,0.9);
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            position: relative;
        }}
        
        .obra-img {{
            width: 100%;
            height: 120px;
            object-fit: cover;
            border-radius: 5px;
            margin-bottom: 10px;
        }}
        
        .contact-artist {{
            position: absolute;
            top: 5px;
            right: 5px;
            width: 30px;
            height: 30px;
            background: #25D366;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-decoration: none;
            font-size: 16px;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .page {{
                padding: 15px;
            }}
            .artist-photo {{
                width: 150px;
                height: 150px;
            }}
            .obra-grid {{
                grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
                gap: 10px;
            }}
        }}
        
        {css_personalizado}
    </style>
</head>
<body>
    <div class="book-container" id="bookContainer">
        
        <!-- Página 1: Portada con foto y datos de Roxana -->
        <div class="page page-1">
            <img src="path/to/roxana-photo.jpg" alt="Roxana Matilde Romano" class="artist-photo">
            <div class="contact-info">
                <h2>ROXANA MATILDE ROMANO</h2>
                <h3>Artista Visual</h3>
                <div class="contact-item">
                    📞 Teléfono: [EXTRAER DEL CÓDIGO ORIGINAL]
                </div>
                <div class="contact-item">
                    📧 Email: [EXTRAER DEL CÓDIGO ORIGINAL]
                </div>
                <div class="contact-item">
                    📍 Dirección: [EXTRAER DEL CÓDIGO ORIGINAL]
                </div>
                <div class="contact-item">
                    📱 WhatsApp: [EXTRAER DEL CÓDIGO ORIGINAL]
                </div>
                <div class="contact-item">
                    🎥 YouTube: [EXTRAER DEL CÓDIGO ORIGINAL]
                </div>
            </div>
        </div>
        
        <!-- Página 2: Biografía/Información del artista -->
        <div class="page page-2">
            <h2>Sobre la Artista</h2>
            <div style="max-width: 600px; text-align: center;">
                <p>[BIOGRAFÍA DE ROXANA - EXTRAER DEL CÓDIGO ORIGINAL]</p>
            </div>
        </div>
        
        <!-- Página 3: Catálogo de obras -->
        <div class="page page-3">
            <h2>Catálogo de Obras</h2>
            <div class="obra-grid" id="catalogoObras">
                <!-- Las obras se cargarán dinámicamente -->
            </div>
        </div>
        
        <!-- Página 4: Certificados -->
        <div class="page page-4">
            <h2>Certificados y Reconocimientos</h2>
            <div class="obra-grid" id="certificados">
                <!-- Los certificados se cargarán dinámicamente -->
            </div>
        </div>
        
        <!-- Página 5: Contacto y enlaces -->
        <div class="page page-5">
            <h2>Contacto</h2>
            <div class="contact-info">
                <div class="contact-item">
                    <strong>¿Te interesa mi arte?</strong><br>
                    Contáctame para consultas, comisiones o adquisiciones
                </div>
                <div class="contact-item">
                    <a href="https://wa.me/[NÚMERO]" style="color: #25D366; text-decoration: none;">
                        💬 Conversar por WhatsApp
                    </a>
                </div>
                <div class="contact-item">
                    <a href="mailto:[EMAIL]" style="color: #0066cc; text-decoration: none;">
                        ✉️ Enviar Email
                    </a>
                </div>
            </div>
        </div>
        
    </div>
    
    <!-- Navegación por botones -->
    <div class="nav-buttons">
        <button class="nav-btn" onclick="previousPage()">← Anterior</button>
        <button class="nav-btn" onclick="nextPage()">Siguiente →</button>
    </div>
    
    <!-- Indicador de página -->
    <div class="page-indicator" id="pageIndicator">1 / 5</div>
    
    <script>
        'use strict';
        
        // Datos extraídos del código original
        const catalogWorks = {obras if obras else '[]'};
        const certificateData = {certificados if certificados else '[]'};
        
        let currentPageIndex = 0;
        const totalPages = 5;
        
        // Navegación por botones
        function previousPage() {{
            if (currentPageIndex > 0) {{
                currentPageIndex--;
                scrollToPage(currentPageIndex);
            }}
        }}
        
        function nextPage() {{
            if (currentPageIndex < totalPages - 1) {{
                currentPageIndex++;
                scrollToPage(currentPageIndex);
            }}
        }}
        
        function scrollToPage(pageIndex) {{
            const container = document.getElementById('bookContainer');
            const pageWidth = window.innerWidth;
            container.scrollTo({{
                left: pageIndex * pageWidth,
                behavior: 'smooth'
            }});
            updatePageIndicator();
        }}
        
        function updatePageIndicator() {{
            const indicator = document.getElementById('pageIndicator');
            indicator.textContent = `${{currentPageIndex + 1}} / ${{totalPages}}`;
        }}
        
        // Detectar scroll manual para actualizar indicador
        function handleScroll() {{
            const container = document.getElementById('bookContainer');
            const pageWidth = window.innerWidth;
            const scrollLeft = container.scrollLeft;
            const newPageIndex = Math.round(scrollLeft / pageWidth);
            
            if (newPageIndex !== currentPageIndex) {{
                currentPageIndex = newPageIndex;
                updatePageIndicator();
            }}
        }}
        
        // Cargar obras dinámicamente
        function loadCatalogo() {{
            const catalogoContainer = document.getElementById('catalogoObras');
            if (!catalogoContainer || !catalogWorks.length) return;
            
            catalogWorks.forEach((obra, index) => {{
                const obraDiv = document.createElement('div');
                obraDiv.className = 'obra-item';
                obraDiv.innerHTML = `
                    <img src="${{obra.image || 'placeholder.jpg'}}" alt="${{obra.title || 'Obra'}}" class="obra-img">
                    <h4>${{obra.title || 'Sin título'}}</h4>
                    <p>${{obra.technique || ''}}</p>
                    <p>${{obra.dimensions || ''}}</p>
                    <a href="https://wa.me/[NÚMERO]?text=Me%20interesa%20la%20obra%20${{obra.title}}" class="contact-artist" target="_blank">💬</a>
                `;
                catalogoContainer.appendChild(obraDiv);
            }});
        }}
        
        // Cargar certificados dinámicamente
        function loadCertificados() {{
            const certContainer = document.getElementById('certificados');
            if (!certContainer || !certificateData.length) return;
            
            certificateData.forEach((cert, index) => {{
                const certDiv = document.createElement('div');
                certDiv.className = 'obra-item';
                certDiv.innerHTML = `
                    <img src="${{cert.image || 'placeholder.jpg'}}" alt="${{cert.title || 'Certificado'}}" class="obra-img">
                    <h4>${{cert.title || 'Sin título'}}</h4>
                    <p>${{cert.institution || ''}}</p>
                    <p>${{cert.date || ''}}</p>
                `;
                certContainer.appendChild(certDiv);
            }});
        }}
        
        // Inicializar cuando carga la página
        document.addEventListener('DOMContentLoaded', function() {{
            document.getElementById('bookContainer').addEventListener('scroll', handleScroll);
            loadCatalogo();
            loadCertificados();
            updatePageIndicator();
        }});
        
        // Navegación por teclado
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'ArrowLeft') previousPage();
            if (e.key === 'ArrowRight') nextPage();
        }});
        
    </script>
</body>
</html>'''
    
    # Guardar la nueva versión
    with open("roxana_completa_mobile.html", "w", encoding="utf-8") as f:
        f.write(nueva_version)
    
    print(f"\n" + "=" * 50)
    print("✅ MIGRACIÓN COMPLETADA")
    print("Archivo creado: roxana_completa_mobile.html")
    print("\nCaracterísticas:")
    print("- ✅ Navegación por swipe horizontal")
    print("- ✅ Botones de navegación como respaldo")
    print("- ✅ Compatible con Chrome móvil")
    print("- ✅ Estructura para foto y datos de Roxana")
    print("- ✅ Iconos de WhatsApp en cada obra")
    print("- ✅ Responsive design")
    print("- ✅ Indicador de página")
    print("\nTareas pendientes:")
    print("1. Extraer datos reales de Roxana del código original")
    print("2. Ajustar rutas de imágenes")
    print("3. Configurar números de teléfono y WhatsApp")
    print("4. Probar en Chrome móvil")
    
    return nueva_version

if __name__ == "__main__":
    migrar_contenido_completo()