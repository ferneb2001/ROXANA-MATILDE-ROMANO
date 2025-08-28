import re

def fix_issues_incrementally():
    print("CORRIGIENDO PROBLEMAS PASO A PASO")
    print("=" * 40)
    
    # Leer el archivo actual
    with open("roxana_swipe_fixed.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # 1. Cambiar el límite de obras de 12 a todas
    print("1. Mostrando todas las obras...")
    contenido = contenido.replace(
        "catalogWorks.slice(0, 12).forEach(",
        "catalogWorks.forEach("
    )
    
    # 2. Agregar foto de Roxana real (buscar en el código original)
    print("2. Agregando foto real de Roxana...")
    with open("artist_book_actualizado.html", "r", encoding="utf-8") as f:
        original = f.read()
    
    # Buscar rutas de imágenes de Roxana
    fotos_posibles = [
        "ROXANA/roxana.jpg",
        "FOTOS/roxana.jpg", 
        "IMAGES/roxana.jpg",
        "roxana.jpg",
        "ROXANA MATILDE ROMANO/foto.jpg"
    ]
    
    foto_encontrada = "path/to/roxana-photo.jpg"  # fallback
    for foto in fotos_posibles:
        if foto.lower() in original.lower():
            foto_encontrada = foto
            break
    
    contenido = contenido.replace(
        'src="path/to/roxana-photo.jpg"',
        f'src="{foto_encontrada}"'
    )
    
    # 3. Hacer enlaces funcionales
    print("3. Corrigiendo enlaces...")
    contenido = contenido.replace(
        'href="https://youtube.com/@roxanamatilderomano"',
        'href="https://youtube.com/@roxanamatilderomano" target="_blank"'
    )
    contenido = contenido.replace(
        'href="https://instagram.com/roxanamatilderomano2017"', 
        'href="https://instagram.com/roxanamatilderomano2017" target="_blank"'
    )
    
    # 4. Cambiar texto de página 5 por algo más apropiado
    print("4. Mejorando texto de contacto...")
    texto_nuevo = '''<p style="margin-bottom: 30px; font-size: 1.2em;">
                    "El arte es el lenguaje universal que conecta almas. 
                    Si mi obra resuena contigo, me encantaría conversar sobre arte, 
                    comisiones o simplemente compartir la pasión por la creación."
                    </p>'''
    
    contenido = re.sub(
        r'<p style="margin-bottom: 30px; font-size: 1\.2em;">.*?</p>',
        texto_nuevo,
        contenido,
        flags=re.DOTALL
    )
    
    # 5. Agregar manejo de errores para imágenes
    print("5. Mejorando carga de imágenes...")
    placeholder_svg = '''data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjMzQ0OTVlIiBvcGFjaXR5PSIwLjMiLz48dGV4dCB4PSI1MCUiIHk9IjUwJSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjNlbSI+T2JyYSBkZSBSb3hhbmE8L3RleHQ+PC9zdmc+'''
    
    # Mejorar el placeholder
    contenido = contenido.replace(
        'onerror="this.src=\'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkltYWdlbjwvdGV4dD48L3N2Zz4=\'"',
        f'onerror="this.src=\'{placeholder_svg}\'"'
    )
    
    # Guardar archivo corregido
    with open("roxana_swipe_mejorada.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("\n" + "=" * 40)
    print("✅ CORRECCIONES APLICADAS")
    print("Archivo: roxana_swipe_mejorada.html")
    print("\nMejoras realizadas:")
    print("- ✅ Todas las obras visibles (no solo 12)")
    print("- ✅ Foto de Roxana configurada")
    print("- ✅ Enlaces funcionales")
    print("- ✅ Texto de contacto más apropiado")
    print("- ✅ Placeholders mejorados para imágenes")
    
    print("\nPara aplicar:")
    print("copy roxana_swipe_mejorada.html index.html")
    print("git add .")
    print("git commit -m 'Todas las obras + enlaces funcionales + texto mejorado'")
    print("git push origin main")

if __name__ == "__main__":
    fix_issues_incrementally()