import os

def add_atelier_gallery():
    print("AGREGANDO GALERÍA GRID DEL ATELIER")
    print("=" * 35)
    
    # Leer archivo con iconos que funciona
    with open("roxana_iconos_reales.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Verificar fotos en carpeta
    fotos_atelier = []
    if os.path.exists("fotos atelier"):
        archivos = os.listdir("fotos atelier")
        for archivo in sorted(archivos):
            if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                fotos_atelier.append(archivo)
        print(f"✓ Encontradas {len(fotos_atelier)} fotos en 'fotos atelier'")
    
    # Agregar CSS para el grid de fotos
    css_grid = '''
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
    contenido = contenido.replace('</style>', css_grid + '\n    </style>')
    
    # Generar HTML del grid
    fotos_html = []
    for i, foto in enumerate(fotos_atelier):
        foto_html = f'''
                    <div class="atelier-photo" onclick="openLightbox('fotos atelier/{foto}', 'Atelier {i+1}')">
                        <img src="fotos atelier/{foto}" alt="Atelier {i+1}" loading="lazy">
                    </div>'''
        fotos_html.append(foto_html)
    
    # Crear página 9 del grid
    pagina_gallery = f'''
        <!-- Página 9: Galería Atelier -->
        <div class="page" id="page9" style="display: none;">
            <div class="page-content">
                <h2 style="text-align: center; color: #d4af37; margin-bottom: 30px; font-size: 2.5em;">
                    Galería del Atelier
                </h2>
                <div class="atelier-gallery">{''.join(fotos_html)}
                </div>
            </div>
        </div>'''
    
    # Encontrar donde insertar la nueva página (después de página 8)
    # Buscar el cierre de la página 8 (Clases)
    patron_page8 = r'<!-- Página 8: Clases -->(.*?)</div>\s*</div>'
    
    def insertar_gallery(match):
        return match.group(0) + '\n' + pagina_gallery
    
    import re
    contenido = re.sub(patron_page8, insertar_gallery, contenido, flags=re.DOTALL)
    
    # Actualizar totalPages en JavaScript
    contenido = contenido.replace('const totalPages = 8;', 'const totalPages = 9;')
    
    # Actualizar los botones del índice para incluir el Atelier Gallery
    # Buscar la página del índice y agregar el botón
    indice_patron = r'(<button onclick="goToPage\(8\)">Clases</button>)'
    indice_reemplazo = r'\1\n                <button onclick="goToPage(9)">Galería Atelier</button>'
    contenido = re.sub(indice_patron, indice_reemplazo, contenido)
    
    # Actualizar la función updatePageIndicator para manejar página 9
    update_pattern = r'(case 8:\s+return "Clases";)'
    update_replacement = r'\1\n                case 9:\n                    return "Galería Atelier";'
    contenido = re.sub(update_pattern, update_replacement, contenido)
    
    # Guardar archivo con galería
    with open("roxana_con_galeria_atelier.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Página 9 agregada: Galería del Atelier")
    print("✓ Grid responsive: 4 columnas desktop, 2 columnas móvil")
    print("✓ Hover effects y transiciones suaves")
    print("✓ Clickeable para zoom (usa lightbox existente)")
    print("✓ Botón agregado al índice")
    print("✓ JavaScript actualizado para 9 páginas")
    print(f"✓ {len(fotos_atelier)} fotos incluidas")
    print("\nArchivo: roxana_con_galeria_atelier.html")
    print("La galería será la página 9, después de 'Clases'")
    print("\nPara navegar: Índice → 'Galería Atelier' o swipe hasta página 9")

if __name__ == "__main__":
    add_atelier_gallery()