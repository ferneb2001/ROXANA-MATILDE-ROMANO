def create_separate_page9():
    print("CREANDO PÁGINA 9 SEPARADA PARA FOTOS")
    print("=" * 35)
    
    # Leer archivo limpio sin página 9
    with open("roxana_sin_page9.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Agregar CSS para página 9 y galería
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
        
        .signature-centered {
            text-align: center;
            margin: 25px 0;
            font-weight: bold;
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
    
    # Insertar CSS
    contenido = contenido.replace('</style>', css_page9 + '\n    </style>')
    
    # Centrar firma en página 8
    contenido = contenido.replace(
        '<p><strong>ROXANA MATILDE ROMANO</strong></p>',
        '<p class="signature-centered"><strong>ROXANA MATILDE ROMANO</strong></p>'
    )
    
    # Crear página 9 solo con fotos
    pagina_9_fotos = '''
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
    
    # Insertar página 9 antes del cierre de </body>
    contenido = contenido.replace('</body>', pagina_9_fotos + '\n    \n    </body>')
    
    # Actualizar JavaScript a 9 páginas
    contenido = contenido.replace('const totalPages = 8;', 'const totalPages = 9;')
    
    # Agregar botón al índice
    contenido = contenido.replace(
        '<button onclick="goToPage(8)" class="index-button">CLASES</button>',
        '''<button onclick="goToPage(8)" class="index-button">CLASES</button>
                    <button onclick="goToPage(9)" class="index-button">GALERÍA ATELIER</button>'''
    )
    
    # Guardar archivo final
    with open("roxana_8_texto_9_fotos.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Página 8: Solo texto con firma centrada")
    print("✓ Página 9: Solo galería de fotos del atelier")
    print("✓ CSS para página 9 (fondo verde)")
    print("✓ Grid de 8 fotos con hover effects")
    print("✓ Botón 'Galería Atelier' en índice")
    print("✓ JavaScript actualizado a 9 páginas")
    print("✓ Lightbox funcional para las fotos")
    
    print("\nArchivo: roxana_8_texto_9_fotos.html")
    print("Página 8: Texto | Página 9: Fotos")

if __name__ == "__main__":
    create_separate_page9()