def fix_pages_7_8():
    print("ARREGLANDO PÁGINAS 7 Y 8")
    print("=" * 30)
    
    # Leer archivo actual
    with open("index.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Encontrar el inicio de la página 7
    inicio_page7 = contenido.find("<!-- Página 7: Próximos Eventos -->")
    if inicio_page7 == -1:
        print("❌ No se encontró el marcador de página 7")
        return
    
    # Encontrar el final de la página 8 (antes del cierre del book-container)
    # Buscar el div de cierre de la página 8 y el book-container
    final_page8 = contenido.find("</div>\n        \n    </div>", inicio_page7)
    if final_page8 == -1:
        # Buscar alternativo
        final_page8 = contenido.find("</div>\n    \n    <!-- Navegación -->", inicio_page7)
        if final_page8 == -1:
            print("❌ No se encontró el final de página 8")
            return
    
    # Contenido corregido de páginas 7 y 8
    paginas_corregidas = '''        <!-- Página 7: Próximos Eventos -->
        <div class="page page7">
            <div class="content">
                <h2>Próximos Eventos</h2>
                <div class="events-container">
                    <div class="event-item">
                        <div class="event-flyer" onclick="openLightbox('EVENTOS/flyers/Muestra Itaka 001.jpg', 'Muestra Itaka', 'Flyer completo del evento')">
                            <img src="EVENTOS/flyers/Muestra Itaka 001.jpg" alt="Muestra Itaka" loading="lazy">
                        </div>
                        <div class="event-info">
                            <div class="event-type">Exposición</div>
                            <div class="event-title">Muestra Itaka 001</div>
                            <div class="event-details">
                                <p>Haz click en el flyer para ver todos los detalles del evento.</p>
                                <p>Consultas por WhatsApp.</p>
                            </div>
                        </div>
                    </div>
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
                    <p class="signature-centered"><strong>ROXANA MATILDE ROMANO</strong></p>
                    
                    <!-- Separador visual -->
                    <div style="height: 30px;"></div>
                    
                    <!-- Galería del Atelier -->
                    <div class="atelier-gallery-small">
                        <div class="atelier-photo-small" onclick="openLightbox('fotos atelier/ATELIER.jpg', 'Vista del Atelier')">
                            <img src="fotos atelier/ATELIER.jpg" alt="Vista del Atelier" loading="lazy">
                        </div>
                        <div class="atelier-photo-small" onclick="openLightbox('fotos atelier/IMG-20250822-WA0022.jpg', 'Espacio de trabajo')">
                            <img src="fotos atelier/IMG-20250822-WA0022.jpg" alt="Espacio de trabajo" loading="lazy">
                        </div>
                        <div class="atelier-photo-small" onclick="openLightbox('fotos atelier/Imagen de WhatsApp 2025-08-26 a las 09.59.49_0c37599c.jpg', 'Ambiente del Atelier')">
                            <img src="fotos atelier/Imagen de WhatsApp 2025-08-26 a las 09.59.49_0c37599c.jpg" alt="Ambiente del Atelier" loading="lazy">
                        </div>
                        <div class="atelier-photo-small" onclick="openLightbox('fotos atelier/atelier1.jpg', 'Rincón creativo')">
                            <img src="fotos atelier/atelier1.jpg" alt="Rincón creativo" loading="lazy">
                        </div>
                        <div class="atelier-photo-small" onclick="openLightbox('fotos atelier/atelier2.jpg', 'Mesa de trabajo')">
                            <img src="fotos atelier/atelier2.jpg" alt="Mesa de trabajo" loading="lazy">
                        </div>
                        <div class="atelier-photo-small" onclick="openLightbox('fotos atelier/atelier3.jpg', 'Área de pintura')">
                            <img src="fotos atelier/atelier3.jpg" alt="Área de pintura" loading="lazy">
                        </div>
                        <div class="atelier-photo-small" onclick="openLightbox('fotos atelier/foto taller.jpg', 'Taller completo')">
                            <img src="fotos atelier/foto taller.jpg" alt="Taller completo" loading="lazy">
                        </div>
                        <div class="atelier-photo-small" onclick="openLightbox('fotos atelier/frente atelier.jpg', 'Frente del Atelier')">
                            <img src="fotos atelier/frente atelier.jpg" alt="Frente del Atelier" loading="lazy">
                        </div>
                    </div>
                </div>
            </div>
        </div>'''
    
    # Reemplazar las páginas problemáticas
    contenido_nuevo = contenido[:inicio_page7] + paginas_corregidas + contenido[final_page8:]
    
    # Guardar archivo corregido
    with open("index_pages_fixed.html", "w", encoding="utf-8") as f:
        f.write(contenido_nuevo)
    
    print("✓ Página 7: Solo eventos (sin duplicaciones)")
    print("✓ Página 8: Texto del atelier + galería de 8 fotos")
    print("✓ Estructura HTML corregida")
    print("✓ Divs balanceados correctamente")
    
    print("\nArchivo: index_pages_fixed.html")
    print("Para aplicar: copy index_pages_fixed.html index.html")

if __name__ == "__main__":
    fix_pages_7_8()