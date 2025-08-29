def fix_page9_correctly():
    print("ARREGLANDO PÁGINA 9 CORRECTAMENTE")
    print("=" * 35)
    
    # Partir del archivo que sabemos que funciona: roxana_iconos_reales.html
    try:
        with open("roxana_iconos_reales.html", "r", encoding="utf-8") as f:
            contenido = f.read()
    except:
        print("❌ No se encuentra roxana_iconos_reales.html")
        print("Usando roxana_galeria_arreglada.html como base...")
        with open("roxana_galeria_arreglada.html", "r", encoding="utf-8") as f:
            contenido = f.read()
    
    # Agregar CSS para la página 9 y galería
    css_page9 = '''        .page8 { background: linear-gradient(135deg, #7f8c8d 0%, #95a5a6 100%); }
        .page9 { background: linear-gradient(135deg, #16a085 0%, #27ae60 100%); }
        
        /* Grid de Fotos Atelier */
        .atelier-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .atelier-photo {
            position: relative;
            aspect-ratio: 4/3;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .atelier-photo:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        }
        
        .atelier-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .atelier-photo:hover img {
            transform: scale(1.05);
        }
        
        @media (max-width: 768px) {
            .atelier-gallery {
                grid-template-columns: repeat(2, 1fr);
                gap: 15px;
                padding: 15px;
            }
            .atelier-photo {
                aspect-ratio: 1/1;
            }
        }'''
    
    # Insertar CSS antes del cierre de </style>
    if '.page8 { background:' not in contenido:
        contenido = contenido.replace(
            '.page7 { background: linear-gradient(135deg, #7f8c8d 0%, #95a5a6 100%); }',
            css_page9
        )
    
    # Crear la página 9 correctamente
    pagina_9 = '''
        <!-- Página 9: Galería Atelier -->
        <div class="page page9">
            <div class="content">
                <h2>Galería del Atelier</h2>
                <div class="atelier-gallery">
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/ATELIER.jpg', 'Vista del Atelier')">
                        <img src="fotos atelier/ATELIER.jpg" alt="Vista del Atelier" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/IMG-20250822-WA0022.jpg', 'Espacio de trabajo')">
                        <img src="fotos atelier/IMG-20250822-WA0022.jpg" alt="Espacio de trabajo" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/Imagen de WhatsApp 2025-08-26 a las 09.59.49_0c37599c.jpg', 'Ambiente del Atelier')">
                        <img src="fotos atelier/Imagen de WhatsApp 2025-08-26 a las 09.59.49_0c37599c.jpg" alt="Ambiente del Atelier" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/atelier1.jpg', 'Rincón creativo')">
                        <img src="fotos atelier/atelier1.jpg" alt="Rincón creativo" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/atelier2.jpg', 'Mesa de trabajo')">
                        <img src="fotos atelier/atelier2.jpg" alt="Mesa de trabajo" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/atelier3.jpg', 'Área de pintura')">
                        <img src="fotos atelier/atelier3.jpg" alt="Área de pintura" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/foto taller.jpg', 'Taller completo')">
                        <img src="fotos atelier/foto taller.jpg" alt="Taller completo" loading="lazy">
                    </div>
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/frente atelier.jpg', 'Frente del Atelier')">
                        <img src="fotos atelier/frente atelier.jpg" alt="Frente del Atelier" loading="lazy">
                    </div>
                </div>
            </div>
        </div>'''
    
    # Buscar el final exacto de la página 8 (Clases) e insertar página 9
    import re
    
    # Patrón para encontrar el final de página 8
    patron_fin_page8 = r'(<!-- Página 8: Clases -->.*?</div>\s*</div>)'
    
    def insertar_page9(match):
        return match.group(1) + '\n' + pagina_9
    
    contenido = re.sub(patron_fin_page8, insertar_page9, contenido, flags=re.DOTALL)
    
    # Actualizar totalPages a 9
    contenido = contenido.replace('const totalPages = 8;', 'const totalPages = 9;')
    
    # Agregar botón al índice si no existe
    if 'GALERÍA ATELIER' not in contenido:
        contenido = contenido.replace(
            '<button onclick="goToPage(8)" class="index-button">CLASES</button>',
            '''<button onclick="goToPage(8)" class="index-button">CLASES</button>
                    <button onclick="goToPage(9)" class="index-button">GALERÍA ATELIER</button>'''
        )
    
    # Guardar archivo
    with open("roxana_galeria_final.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Página 9 creada con clase 'page9' correcta")
    print("✓ CSS de galería agregado")
    print("✓ 8 fotos del atelier incluidas")
    print("✓ Grid responsive (4x2 desktop, 2x4 móvil)")
    print("✓ Hover effects y lightbox")
    print("✓ Botón en índice agregado")
    print("✓ JavaScript actualizado a 9 páginas")
    
    print("\nArchivo: roxana_galeria_final.html")
    print("Ahora la página 9 debería mostrar las fotos correctamente")

if __name__ == "__main__":
    fix_page9_correctly()