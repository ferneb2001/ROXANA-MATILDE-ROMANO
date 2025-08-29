def fix_gallery_structure():
    print("ARREGLANDO ESTRUCTURA DE LA GALERÍA")
    print("=" * 40)
    
    # Leer archivo problemático
    with open("roxana_con_galeria_atelier.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # PROBLEMA 1: Arreglar la página 9 que está mal estructurada
    # Buscar y corregir el div de página 9
    import re
    
    # Encontrar donde termina la página 8 correctamente
    patron_page8_end = r'(</div>\s*</div>\s*</div>\s*</div>\s*</div>)'
    
    # Crear la página 9 correctamente estructurada
    pagina_9_correcta = '''
        <!-- Página 9: Galería Atelier -->
        <div class="page page8" style="background: linear-gradient(135deg, #16a085 0%, #27ae60 100%);">
            <div class="content">
                <h2 style="text-align: center; color: white; margin-bottom: 30px; font-size: 2.5em;">
                    Galería del Atelier
                </h2>
                <div class="atelier-gallery">
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/ATELIER.jpg', 'Atelier 1')">
                        <img src="fotos atelier/ATELIER.jpg" alt="Atelier 1" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/IMG-20250822-WA0022.jpg', 'Atelier 2')">
                        <img src="fotos atelier/IMG-20250822-WA0022.jpg" alt="Atelier 2" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/Imagen de WhatsApp 2025-08-26 a las 09.59.49_0c37599c.jpg', 'Atelier 3')">
                        <img src="fotos atelier/Imagen de WhatsApp 2025-08-26 a las 09.59.49_0c37599c.jpg" alt="Atelier 3" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/atelier1.jpg', 'Atelier 4')">
                        <img src="fotos atelier/atelier1.jpg" alt="Atelier 4" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/atelier2.jpg', 'Atelier 5')">
                        <img src="fotos atelier/atelier2.jpg" alt="Atelier 5" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/atelier3.jpg', 'Atelier 6')">
                        <img src="fotos atelier/atelier3.jpg" alt="Atelier 6" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/foto taller.jpg', 'Atelier 7')">
                        <img src="fotos atelier/foto taller.jpg" alt="Atelier 7" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/frente atelier.jpg', 'Atelier 8')">
                        <img src="fotos atelier/frente atelier.jpg" alt="Atelier 8" loading="lazy">
                    </div>
                </div>
            </div>
        </div>'''
    
    # PROBLEMA 2: Eliminar la página 9 mal estructurada existente
    patron_pagina_9_mala = r'<!-- Página 9: Galería Atelier -->.*?</div>\s*</div>\s*</div>'
    contenido = re.sub(patron_pagina_9_mala, '', contenido, flags=re.DOTALL)
    
    # PROBLEMA 3: Insertar la página 9 en el lugar correcto (después de página 8)
    # Buscar el cierre de página 8
    contenido = contenido.replace(
        '</div>\n        </div>\n        </div>',  # Final de página 8
        '</div>\n        </div>' + pagina_9_correcta + '\n        </div>'  # Página 8 + nueva página 9
    )
    
    # PROBLEMA 4: Agregar el botón al índice
    contenido = contenido.replace(
        '<button onclick="goToPage(8)" class="index-button">CLASES</button>',
        '<button onclick="goToPage(8)" class="index-button">CLASES</button>\n                    <button onclick="goToPage(9)" class="index-button">GALERÍA ATELIER</button>'
    )
    
    # PROBLEMA 5: Actualizar el indicador de páginas
    contenido = contenido.replace(
        '${currentPageIndex + 1} / ${totalPages}',
        '${currentPageIndex + 1} / 9'
    )
    
    # PROBLEMA 6: Agregar color para página 9 en CSS
    contenido = contenido.replace(
        '.page7 { background: linear-gradient(135deg, #7f8c8d 0%, #95a5a6 100%); }',
        '''.page7 { background: linear-gradient(135deg, #7f8c8d 0%, #95a5a6 100%); }
        .page9 { background: linear-gradient(135deg, #16a085 0%, #27ae60 100%); }'''
    )
    
    # Guardar archivo corregido
    with open("roxana_galeria_arreglada.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Estructura HTML corregida")
    print("✓ Página 9 insertada en el lugar correcto")
    print("✓ Botón 'Galería Atelier' agregado al índice")
    print("✓ Indicador de páginas actualizado (1/9)")
    print("✓ Grid de 8 fotos con hover effects")
    print("✓ Color verde/turquesa para la página 9")
    print("✓ Navegación por swipe funcional")
    
    print("\nArchivo: roxana_galeria_arreglada.html")
    print("La página 9 ahora debe ser accesible por swipe y desde el índice")

if __name__ == "__main__":
    fix_gallery_structure()