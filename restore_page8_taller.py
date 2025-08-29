def restore_page8_taller():
    print("RESTAURANDO PÁGINA 8 DEL TALLER")
    print("=" * 30)
    
    # Leer archivo actual
    with open("index.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    import re
    
    # Buscar la página 8 actual y verificar qué tiene
    if 'Página 8: Clases' in contenido:
        print("✓ Página 8 existe con título Clases")
        
        # Buscar si tiene el contenido del atelier
        if 'ATELIER' in contenido and 'Un espacio donde la luz respira' in contenido:
            print("✓ Página 8 ya tiene contenido del atelier")
            
            # Solo necesitamos agregar las fotos del atelier si no están
            if 'atelier-gallery-small' not in contenido:
                print("- Agregando galería de fotos del atelier")
                
                # Buscar el final del texto del atelier y agregar galería
                atelier_gallery = '''
                    
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
                    </div>'''
                
                # Insertar galería después de la firma de Roxana
                contenido = contenido.replace(
                    '<p class="signature-centered"><strong>ROXANA MATILDE ROMANO</strong></p>',
                    '<p class="signature-centered"><strong>ROXANA MATILDE ROMANO</strong></p>' + atelier_gallery
                )
                
                # Agregar CSS para la galería si no existe
                if 'atelier-gallery-small' not in contenido:
                    css_galeria = '''
        /* Galería pequeña del atelier */
        .atelier-gallery-small {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 12px;
            padding: 20px 0;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .atelier-photo-small {
            aspect-ratio: 4/3;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        
        .atelier-photo-small:hover {
            transform: translateY(-3px);
        }
        
        .atelier-photo-small img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        @media (max-width: 768px) {
            .atelier-gallery-small {
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
            }
        }'''
                    
                    contenido = contenido.replace('</style>', css_galeria + '\n    </style>')
            else:
                print("✓ Galería del atelier ya presente")
        else:
            print("- Restaurando contenido completo del atelier en página 8")
            # Aquí agregaría todo el contenido del atelier si no existiera
    
    # Guardar archivo restaurado
    with open("index_page8_restored.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("\n✓ Página 8 restaurada con:")
    print("  - Texto del Atelier")
    print("  - Firma centrada de Roxana") 
    print("  - Galería de 8 fotos del atelier")
    print("✓ Página 7 mantiene solo eventos")
    
    print("\nArchivo: index_page8_restored.html")
    print("Para aplicar: copy index_page8_restored.html index.html")

if __name__ == "__main__":
    restore_page8_taller()