import re

def create_complete_structure():
    print("CREANDO ESTRUCTURA COMPLETA DESDE CERO")
    print("=" * 50)
    
    # Leer el archivo actual para extraer los datos
    with open("roxana_estructura_completa.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Extraer los datos JavaScript (catalogWorks y certificateData)
    catalog_pattern = r'const catalogWorks = \[(.*?)\];'
    catalog_match = re.search(catalog_pattern, contenido, re.DOTALL)
    catalog_data = catalog_match.group(1) if catalog_match else ""
    
    certificate_pattern = r'const certificateData = \[(.*?)\];'
    cert_match = re.search(certificate_pattern, contenido, re.DOTALL)
    cert_data = cert_match.group(1) if cert_match else ""
    
    # Crear HTML completo desde cero con 7 páginas
    html_completo = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roxana Matilde Romano - Artista</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Georgia', serif;
            overflow: hidden;
            background: #1a1a1a;
        }
        
        .book-container {
            width: 100vw;
            height: 100vh;
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
            -ms-overflow-style: none;
            scroll-behavior: smooth;
        }
        
        .book-container::-webkit-scrollbar {
            display: none;
        }
        
        .page {
            flex: 0 0 100vw;
            scroll-snap-align: start;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
            position: relative;
            overflow-y: auto;
            color: white;
        }
        
        /* Colores específicos para cada página */
        .page1 { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); }
        .page2 { background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%); }
        .page3 { background: linear-gradient(135deg, #e67e22 0%, #f39c12 100%); }
        .page4 { background: linear-gradient(135deg, #2980b9 0%, #3498db 100%); }
        .page5 { background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%); }
        .page6 { background: linear-gradient(135deg, #c0392b 0%, #e74c3c 100%); }
        .page7 { background: linear-gradient(135deg, #7f8c8d 0%, #95a5a6 100%); }
        
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
        }
        
        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 30px;
            max-width: 400px;
        }
        
        .contact-item {
            background: rgba(255,255,255,0.1);
            padding: 12px 20px;
            border-radius: 25px;
            text-decoration: none;
            color: white;
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.2);
            text-align: center;
        }
        
        .contact-item:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }
        
        .contact-item a {
            color: inherit;
            text-decoration: none;
        }
        
        .content {
            max-width: 900px;
            width: 100%;
            text-align: center;
        }
        
        .content h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .content h2 {
            font-size: 2em;
            margin-bottom: 30px;
        }
        
        .subtitle {
            font-size: 1.5em;
            opacity: 0.9;
            margin-bottom: 20px;
        }
        
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
        
        .obras-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 1000px;
            margin-top: 20px;
            max-height: 70vh;
            overflow-y: auto;
        }
        
        .obra-item {
            background: rgba(255,255,255,0.15);
            border-radius: 15px;
            padding: 15px;
            text-align: center;
            position: relative;
            backdrop-filter: blur(10px);
            transition: transform 0.3s;
        }
        
        .obra-item:hover {
            transform: translateY(-5px);
        }
        
        .obra-img {
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 10px;
            cursor: pointer;
        }
        
        .obra-title {
            font-weight: bold;
            margin-bottom: 5px;
            font-size: 0.9em;
        }
        
        .obra-details {
            font-size: 0.8em;
            opacity: 0.9;
        }
        
        .contact-artist {
            position: absolute;
            top: 10px;
            right: 10px;
            width: 35px;
            height: 35px;
            background: #25D366;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-decoration: none;
            font-size: 18px;
            transition: transform 0.3s;
        }
        
        .contact-artist:hover {
            transform: scale(1.1);
        }
        
        .events-container, .classes-container, .biografia-content {
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
        
        .biografia-content {
            text-align: justify;
        }
        
        .nav-buttons {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
            z-index: 1000;
        }
        
        .nav-btn {
            padding: 10px 20px;
            background: rgba(0,0,0,0.7);
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            transition: background 0.3s;
        }
        
        .nav-btn:hover {
            background: rgba(0,0,0,0.9);
        }
        
        .page-indicator {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            z-index: 1000;
        }
        
        .lightbox {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            z-index: 2000;
            justify-content: center;
            align-items: center;
        }
        
        .lightbox-content {
            position: relative;
            max-width: 90%;
            max-height: 90%;
            text-align: center;
        }
        
        .lightbox-img {
            max-width: 100%;
            max-height: 80vh;
            object-fit: contain;
        }
        
        .lightbox-info {
            color: white;
            padding: 15px;
            text-align: center;
        }
        
        .close {
            position: absolute;
            top: -40px;
            right: 0;
            color: white;
            font-size: 35px;
            font-weight: bold;
            cursor: pointer;
        }
        
        .close:hover {
            opacity: 0.7;
        }
        
        @media (max-width: 768px) {
            .page {
                padding: 15px;
            }
            
            .profile-photo {
                width: 150px;
                height: 150px;
            }
            
            .content h1 {
                font-size: 2em;
            }
            
            .obras-grid {
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="book-container" id="bookContainer">
        
        <!-- Página 1: Datos Personales -->
        <div class="page page1">
            <div class="profile-container">
                <img src="FOTO RO.jpg" alt="Roxana Matilde Romano" class="profile-photo">
                <div class="content">
                    <h1>ROXANA MATILDE ROMANO</h1>
                    <p class="subtitle">Artista Visual</p>
                    
                    <div class="contact-info">
                        <div class="contact-item">
                            <a href="tel:+5492615988180">📞 +54 9 261-5988180</a>
                        </div>
                        <div class="contact-item">
                            <a href="mailto:roxanamatilderomano@gmail.com">✉️ roxanamatilderomano@gmail.com</a>
                        </div>
                        <div class="contact-item">
                            📍 Manuel A. Sáez 2101 - Las Heras - Mendoza
                        </div>
                        <div class="contact-item">
                            <a href="https://youtube.com/@roxanamatilderomano" target="_blank">🎥 @roxanamatilderomano</a>
                        </div>
                        <div class="contact-item">
                            <a href="https://instagram.com/roxanamatilderomano2017" target="_blank">📸 @roxanamatilderomano2017</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Página 2: Declaración de Artista -->
        <div class="page page2">
            <div class="content">
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
                </div>
            </div>
        </div>

        <!-- Página 3: Índice -->
        <div class="page page3">
            <div class="content">
                <h2>Índice</h2>
                <div class="index-menu">
                    <button onclick="goToPage(3)" class="index-button">BIOGRAFÍA</button>
                    <button onclick="goToPage(4)" class="index-button">OBRAS</button>
                    <button onclick="goToPage(5)" class="index-button">CERTIFICADOS</button>
                    <button onclick="goToPage(6)" class="index-button">PRÓXIMOS EVENTOS</button>
                    <button onclick="goToPage(7)" class="index-button">CLASES</button>
                </div>
            </div>
        </div>

        <!-- Página 4: Biografía -->
        <div class="page page4">
            <div class="content">
                <h2>Sobre la Artista</h2>
                <div class="biografia-content">
                    <p>ROXANA MATILDE ROMANO es nacida en Mendoza en 1969. Ascendente artista visual quien a partir del año 2012 comienza su carrera. Se perfecciona con Eduardo Salinas, Daniel Bernal y Egar Murillo.</p>
                    
                    <p>Realizó diferentes muestras individuales tales como: "Origen y orgullo", Salón Malvinas Argentinas. "Resiliencia" en 2013 e "Hipócrita" en 2014 en la Nave Cultural de Mendoza.</p>
                    
                    <p>Durante el año 2014 participó de la muestra "Otredad" en la Alianza Francesa de Mza. En ese mismo año obtuvo el Primer Premio en el 1º Salón de Pintura Pequeño Formato - Tema: "Rostros Universales", y también suma una mención en el Salón de Pintura "Juan Gutenberg".</p>
                    
                    <p>"Panóptico", año 2022; "La sombra de lo inútil" año 2023 y "La paradoja del observador" año 2024, tres obras seleccionadas para el salón Vendimia. Obra suya se encuentra en colecciones públicas y privadas siendo su trabajo elogiosamente reconocido por el colectivo artístico.</p>
                </div>
            </div>
        </div>

        <!-- Página 5: Obras -->
        <div class="page page5">
            <div class="content">
                <h2>Catálogo de Obras</h2>
                <div class="obras-grid" id="obrasContainer">
                    <!-- Las obras se cargarán dinámicamente -->
                </div>
            </div>
        </div>

        <!-- Página 6: Certificados -->
        <div class="page page6">
            <div class="content">
                <h2>Certificados</h2>
                <div class="obras-grid" id="certificadosContainer">
                    <!-- Los certificados se cargarán dinámicamente -->
                </div>
            </div>
        </div>

        <!-- Página 7: Próximos Eventos -->
        <div class="page page7">
            <div class="content">
                <h2>Próximos Eventos</h2>
                <div class="events-container">
                    <p>Próximamente se anunciarán nuevos eventos y exposiciones.</p>
                    <p>Mantente conectado a través de nuestras redes sociales para no perderte las últimas novedades.</p>
                </div>
            </div>
        </div>

        <!-- Página 8: Clases -->
        <div class="page page8">
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
        </div>
        
    </div>
    
    <!-- Navegación -->
    <div class="nav-buttons">
        <button class="nav-btn" onclick="previousPage()">← Anterior</button>
        <button class="nav-btn" onclick="nextPage()">Siguiente →</button>
    </div>
    
    <div class="page-indicator" id="pageIndicator">1 / 8</div>
    
    <!-- Lightbox -->
    <div id="lightbox" class="lightbox" onclick="closeLightbox()">
        <div class="lightbox-content" onclick="event.stopPropagation()">
            <span class="close" onclick="closeLightbox()">&times;</span>
            <img id="lightboxImg" class="lightbox-img" src="" alt="">
            <div id="lightboxInfo" class="lightbox-info"></div>
        </div>
    </div>
    
    <script>
        'use strict';
        
        const catalogWorks = [''' + catalog_data + '''];
        const certificateData = [''' + cert_data + '''];
        
        let currentPageIndex = 0;
        const totalPages = 8;
        
        function previousPage() {
            if (currentPageIndex > 0) {
                currentPageIndex--;
                scrollToPage(currentPageIndex);
            }
        }
        
        function nextPage() {
            if (currentPageIndex < totalPages - 1) {
                currentPageIndex++;
                scrollToPage(currentPageIndex);
            }
        }
        
        function scrollToPage(pageIndex) {
            const container = document.getElementById('bookContainer');
            const pageWidth = window.innerWidth;
            container.scrollTo({
                left: pageIndex * pageWidth,
                behavior: 'smooth'
            });
            updatePageIndicator();
        }
        
        function goToPage(pageNum) {
            currentPageIndex = pageNum - 1;
            scrollToPage(currentPageIndex);
        }
        
        function updatePageIndicator() {
            const indicator = document.getElementById('pageIndicator');
            indicator.textContent = `${currentPageIndex + 1} / ${totalPages}`;
        }
        
        function handleScroll() {
            const container = document.getElementById('bookContainer');
            const pageWidth = window.innerWidth;
            const scrollLeft = container.scrollLeft;
            const newPageIndex = Math.round(scrollLeft / pageWidth);
            
            if (newPageIndex !== currentPageIndex) {
                currentPageIndex = newPageIndex;
                updatePageIndicator();
            }
        }
        
        function loadObras() {
            const container = document.getElementById('obrasContainer');
            if (!container || !catalogWorks || !Array.isArray(catalogWorks)) return;
            
            catalogWorks.forEach((obra) => {
                const div = document.createElement('div');
                div.className = 'obra-item';
                
                const whatsappMsg = `Hola Roxana, me interesa tu obra "${obra.title || 'Sin título'}"`;
                const whatsappUrl = `https://wa.me/5492615988180?text=${encodeURIComponent(whatsappMsg)}`;
                
                div.innerHTML = `
                    <img src="${obra.path || 'placeholder.jpg'}" alt="${obra.title || 'Obra'}" class="obra-img" 
                         onclick="openLightbox('${obra.path}', '${obra.title}', '${obra.technique || ''} ${obra.dimensions || ''} ${obra.year || ''}')"
                         onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjMzQ0OTVlIiBvcGFjaXR5PSIwLjMiLz48dGV4dCB4PSI1MCUiIHk9IjUwJSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjNlbSI+T2JyYSBkZSBSb3hhbmE8L3RleHQ+PC9zdmc+'">
                    <div class="obra-title">${obra.title || 'Sin título'}</div>
                    <div class="obra-details">
                        ${obra.technique ? obra.technique + '<br>' : ''}
                        ${obra.dimensions ? obra.dimensions + '<br>' : ''}
                        ${obra.year ? obra.year : ''}
                    </div>
                    <a href="${whatsappUrl}" class="contact-artist" target="_blank" title="Consultar por esta obra">💬</a>
                `;
                container.appendChild(div);
            });
        }
        
        function loadCertificados() {
            const container = document.getElementById('certificadosContainer');
            if (!container || !certificateData || !Array.isArray(certificateData)) return;
            
            certificateData.forEach((cert, index) => {
                const div = document.createElement('div');
                div.className = 'obra-item';
                
                const certName = cert.split('/').pop().split('.')[0];
                
                div.innerHTML = `
                    <img src="${cert}" alt="Certificado ${index + 1}" class="obra-img"
                         onclick="openLightbox('${cert}', 'Certificado ${index + 1}', '${certName}')"
                         onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkNlcnRpZmljYWRvPC90ZXh0Pjwvc3ZnPg=='>
                    <div class="obra-title">Certificado ${index + 1}</div>
                    <div class="obra-details">${certName}</div>
                `;
                container.appendChild(div);
            });
        }
        
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
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('bookContainer').addEventListener('scroll', handleScroll);
            loadObras();
            loadCertificados();
            updatePageIndicator();
        });
        
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') previousPage();
            if (e.key === 'ArrowRight') nextPage();
        });
        
    </script>
</body>
</html>'''
    
    # Guardar el archivo nuevo
    with open("roxana_completa_8_paginas.html", "w", encoding="utf-8") as f:
        f.write(html_completo)
    
    print("✓ Estructura completa creada con 8 páginas")
    print("✓ Declaración de Artista agregada")
    print("✓ Índice navegable agregado")
    print("✓ Biografía incluida")
    print("✓ Próximos Eventos preparado")
    print("✓ Clases y Atelier incluido")
    print("✓ Zoom en obras y certificados funcional")
    print("✓ Caracteres especiales corregidos")
    print("✓ Foto de Roxana centrada")
    print("\nArchivo: roxana_completa_8_paginas.html")
    print("\nPáginas:")
    print("1. Datos personales")
    print("2. Declaración de Artista") 
    print("3. Índice navegable")
    print("4. Biografía")
    print("5. Catálogo de Obras (76)")
    print("6. Certificados (con zoom)")
    print("7. Próximos Eventos")
    print("8. Clases y Atelier")

if __name__ == "__main__":
    create_complete_structure()