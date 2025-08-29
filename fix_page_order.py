import re

def fix_page_order():
    print("CORRIGIENDO ORDEN DE PÁGINAS")
    print("=" * 40)
    
    # Leer el archivo actual
    with open("roxana_completa_8_paginas.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Corregir orden: mover biografía después de Declaración de Artista
    # y actualizar el índice
    
    nueva_estructura_paginas = '''        <!-- Página 1: Datos Personales -->
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

        <!-- Página 3: Sobre la Artista (Biografía) -->
        <div class="page page3">
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

        <!-- Página 4: Índice -->
        <div class="page page4">
            <div class="content">
                <h2>Índice</h2>
                <div class="index-menu">
                    <button onclick="goToPage(5)" class="index-button">OBRAS</button>
                    <button onclick="goToPage(6)" class="index-button">CERTIFICADOS</button>
                    <button onclick="goToPage(7)" class="index-button">PRÓXIMOS EVENTOS</button>
                    <button onclick="goToPage(8)" class="index-button">CLASES</button>
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
        </div>'''
    
    # Reemplazar las páginas en el contenido
    patron_paginas = r'(\s*<!-- Página 1: Datos Personales -->.*?<!-- Página 8: Clases -->.*?</div>\s*</div>)'
    contenido = re.sub(patron_paginas, nueva_estructura_paginas, contenido, flags=re.DOTALL)
    
    # Actualizar el color de la página 4 (índice) en CSS
    contenido = contenido.replace('.page4 { background: linear-gradient(135deg, #2980b9 0%, #3498db 100%); }',
                                '.page4 { background: linear-gradient(135deg, #e67e22 0%, #f39c12 100%); }')
    contenido = contenido.replace('.page3 { background: linear-gradient(135deg, #e67e22 0%, #f39c12 100%); }',
                                '.page3 { background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%); }')
    
    # Guardar archivo corregido
    with open("roxana_orden_corregido.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Orden de páginas corregido")
    print("✓ 'Sobre la Artista' movido después de Declaración")
    print("✓ 'Biografía' removido del índice") 
    print("✓ Enlaces del índice actualizados")
    print("\nNuevo orden:")
    print("1. Datos personales")
    print("2. Declaración de Artista")
    print("3. Sobre la Artista")
    print("4. Índice (sin biografía)")
    print("5. Obras")
    print("6. Certificados")
    print("7. Próximos Eventos")  
    print("8. Clases")
    print("\nArchivo: roxana_orden_corregido.html")

if __name__ == "__main__":
    fix_page_order()