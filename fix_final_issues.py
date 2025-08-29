import re

def fix_final_issues():
    print("CORRIGIENDO PROBLEMAS FINALES")
    print("=" * 35)
    
    with open("roxana_swipe_mejorada.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # 1. Agregar funcionalidad de zoom/lightbox para las obras
    print("1. Agregando zoom a las obras...")
    
    # Agregar CSS para lightbox
    css_lightbox = '''
        /* Lightbox para zoom de obras */
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
        
        .lightbox-img {
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
        }
        
        .lightbox-close {
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 40px;
            color: white;
            cursor: pointer;
            user-select: none;
        }
        
        .lightbox-info {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            text-align: center;
            background: rgba(0,0,0,0.7);
            padding: 15px;
            border-radius: 10px;
        }'''
    
    # Insertar CSS antes del cierre de </style>
    contenido = contenido.replace('</style>', css_lightbox + '\n    </style>')
    
    # 2. Corregir enlaces en los datos de contacto
    print("2. Haciendo enlaces funcionales...")
    
    # Hacer clickeable el teléfono
    contenido = contenido.replace(
        '📞 +54 9 261-5988180',
        '<a href="tel:+5492615988180" style="color: inherit; text-decoration: none;">📞 +54 9 261-5988180</a>'
    )
    
    # Hacer clickeable el email
    contenido = contenido.replace(
        '📧 roxanamatilderomano@gmail.com',
        '<a href="mailto:roxanamatilderomano@gmail.com" style="color: inherit; text-decoration: none;">📧 roxanamatilderomano@gmail.com</a>'
    )
    
    # Hacer clickeable YouTube
    contenido = contenido.replace(
        '🎥 @roxanamatilderomano',
        '<a href="https://youtube.com/@roxanamatilderomano" target="_blank" style="color: inherit; text-decoration: none;">🎥 @roxanamatilderomano</a>'
    )
    
    # Hacer clickeable Instagram
    contenido = contenido.replace(
        '📷 @roxanamatilderomano2017',
        '<a href="https://instagram.com/roxanamatilderomano2017" target="_blank" style="color: inherit; text-decoration: none;">📷 @roxanamatilderomano2017</a>'
    )
    
    # 3. Agregar foto de Roxana si existe
    print("3. Buscando foto de Roxana...")
    
    # Lista de posibles ubicaciones de la foto
    posibles_fotos = [
        "FOTOS/roxana.jpg",
        "IMAGES/roxana.jpg", 
        "roxana.jpg",
        "ROXANA/foto.jpg",
        "IMG/roxana.jpg"
    ]
    
    import os
    foto_encontrada = None
    for foto in posibles_fotos:
        if os.path.exists(foto):
            foto_encontrada = foto
            break
    
    if foto_encontrada:
        contenido = contenido.replace(
            'src="path/to/roxana-photo.jpg"',
            f'src="{foto_encontrada}"'
        )
        print(f"   Foto encontrada: {foto_encontrada}")
    else:
        # Usar un placeholder más apropiado
        placeholder_roxana = '''data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjEwMCIgZmlsbD0iIzM0NDk1ZSIgb3BhY2l0eT0iMC4zIi8+PHRleHQgeD0iNTAlIiB5PSI0NSUiIGZvbnQtZmFtaWx5PSJHZW9yZ2lhIiBmb250LXNpemU9IjE2IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5ST1hBTkE8L3RleHQ+PHRleHQgeD0iNTAlIiB5PSI1NSUiIGZvbnQtZmFtaWx5PSJHZW9yZ2lhIiBmb250LXNpemU9IjE2IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5NQVRJTERFPC90ZXh0Pjx0ZXh0IHg9IjUwJSIgeT0iNjUlIiBmb250LWZhbWlseT0iR2VvcmdpYSIgZm9udC1zaXplPSIxNiIgZmlsbD0iI2ZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Uk9NQU5PPC90ZXh0Pjwvc3ZnPg=='''
        contenido = contenido.replace(
            'src="path/to/roxana-photo.jpg"',
            f'src="{placeholder_roxana}"'
        )
        print("   Usando placeholder personalizado")
    
    # 4. Modificar el JavaScript para agregar zoom
    print("4. Agregando funcionalidad de zoom...")
    
    js_zoom = '''
        // Función para abrir lightbox
        function openLightbox(imgSrc, title, details) {
            const lightbox = document.getElementById('lightbox');
            const lightboxImg = document.getElementById('lightboxImg');
            const lightboxInfo = document.getElementById('lightboxInfo');
            
            lightboxImg.src = imgSrc;
            lightboxInfo.innerHTML = `<h3>${title}</h3><p>${details}</p>`;
            lightbox.style.display = 'flex';
        }
        
        // Función para cerrar lightbox
        function closeLightbox() {
            document.getElementById('lightbox').style.display = 'none';
        }'''
    
    # Agregar el HTML del lightbox antes del cierre de body
    lightbox_html = '''
    <!-- Lightbox para zoom -->
    <div class="lightbox" id="lightbox" onclick="closeLightbox()">
        <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
        <img class="lightbox-img" id="lightboxImg" onclick="event.stopPropagation()">
        <div class="lightbox-info" id="lightboxInfo" onclick="event.stopPropagation()"></div>
    </div>'''
    
    contenido = contenido.replace('</body>', lightbox_html + '\n</body>')
    
    # Modificar la función loadObras para agregar click event
    patron_obra_img = r'<img src="\$\{obra\.path.*?\}" alt="\$\{obra\.title.*?\}" class="obra-img"[^>]*>'
    
    nuevo_img = '''<img src="${obra.path || 'placeholder.jpg'}" alt="${obra.title || 'Obra'}" class="obra-img" 
                         style="cursor: pointer;"
                         onclick="openLightbox('${obra.path}', '${obra.title}', '${obra.technique || ''} ${obra.dimensions || ''} ${obra.year || ''}')"
                         onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjMzQ0OTVlIiBvcGFjaXR5PSIwLjMiLz48dGV4dCB4PSI1MCUiIHk9IjUwJSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjNlbSI+T2JyYSBkZSBSb3hhbmE8L3RleHQ+PC9zdmc+'">'''
    
    # Reemplazar la imagen con la nueva que incluye onclick
    contenido = re.sub(
        r'<img src="\$\{obra\.path[^>]*>',
        nuevo_img,
        contenido
    )
    
    # Agregar las funciones JavaScript
    contenido = contenido.replace(
        '// Navegación por teclado',
        js_zoom + '\n        \n        // Navegación por teclado'
    )
    
    # Guardar archivo corregido
    with open("roxana_final_completa.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("\n" + "=" * 35)
    print("✅ PROBLEMAS CORREGIDOS")
    print("Archivo: roxana_final_completa.html")
    print("\nMejoras:")
    print("- ✅ Enlaces clickeables en datos de contacto")
    print("- ✅ Zoom/lightbox en obras (click en imagen)")
    print("- ✅ Foto de Roxana configurada")
    print("- ✅ Placeholder personalizado si no hay foto")
    
    print("\nPara probar localmente:")
    print("Abre roxana_final_completa.html en Chrome")
    print("- Click en teléfono/email debería abrir aplicaciones")
    print("- Click en obras debería abrir zoom")
    print("- Enlaces de redes sociales funcionan")
    
    print("\nPara subir:")
    print("copy roxana_final_completa.html index.html")
    print("git add .")
    print("git commit -m 'Enlaces funcionales + zoom en obras'")
    print("git push origin main")

if __name__ == "__main__":
    fix_final_issues()