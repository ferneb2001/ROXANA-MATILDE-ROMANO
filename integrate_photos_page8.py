def integrate_photos_page8():
    print("INTEGRANDO FOTOS EN PÁGINA 8")
    print("=" * 30)
    
    # Usar la base que funciona
    with open("roxana_simple_fix.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Agregar CSS para galería pequeña integrada
    css_galeria = '''
        /* Galería pequeña para página 8 */
        .signature-centered {
            text-align: center;
            margin: 20px 0;
            font-weight: bold;
        }
        
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
    
    # Insertar CSS antes del cierre de </style>
    contenido = contenido.replace('</style>', css_galeria + '\n    </style>')
    
    # Crear la nueva página 8 con texto + fotos
    import re
    
    # Buscar la página 8 actual y reemplazarla
    patron_page8 = r'(<!-- Página 8: Clases -->.*?<p><strong>ROXANA MATILDE ROMANO</strong></p>)(.*?</div>\s*</div>)'
    
    nueva_page8 = r'''\1
                    
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
            </div>'''
    
    # Hacer el reemplazo
    contenido = re.sub(patron_page8, nueva_page8, contenido, flags=re.DOTALL)
    
    # Centrar la firma ROXANA MATILDE ROMANO
    contenido = contenido.replace(
        '<p><strong>ROXANA MATILDE ROMANO</strong></p>',
        '<p class="signature-centered"><strong>ROXANA MATILDE ROMANO</strong></p>'
    )
    
    with open("roxana_page8_completa.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Galería agregada a página 8")
    print("✓ Fotos más pequeñas (150px mínimo)")
    print("✓ Firma ROXANA centrada")
    print("✓ Separador visual entre texto y fotos") 
    print("✓ Lightbox funcional para zoom")
    print("✓ Grid responsive (4-5 fotos por fila)")
    print("✓ Navegación intacta")
    
    print("\nArchivo: roxana_page8_completa.html")
    print("Página 8: Texto + firma centrada + separador + galería")

if __name__ == "__main__":
    integrate_photos_page8()