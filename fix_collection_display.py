def fix_collection_display():
    print("ARREGLANDO DISPLAY DE 'COLECCIÓN PRIVADA'")
    print("=" * 40)
    
    with open("roxana_touch_restored.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    import re
    
    # Buscar la función loadObras y modificarla para mostrar collection
    patron_load_obras = r'(div\.innerHTML = `.*?<div class="obra-details">.*?\$\{obra\.year \? obra\.year : \'\'\}.*?</div>.*?`;)'
    
    nuevo_html_obra = '''div.innerHTML = `
                    <img src="${obra.path || 'placeholder.jpg'}" alt="${obra.title || 'Obra'}" class="obra-img" 
                         onclick="openLightbox('${obra.path}', '${obra.title}', '${obra.technique || ''} ${obra.dimensions || ''} ${obra.year || ''}')"
                         onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjMzQ0OTVlIiBvcGFjaXR5PSIwLjMiLz48dGV4dCB4PSI1MCUiIHk9IjUwJSIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXNpemU9IjE0IiBmaWxsPSIjZmZmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjNlbSI+T2JyYSBkZSBSb3hhbmE8L3RleHQ+PC9zdmc+">
                    <div class="obra-title">${obra.title || 'Sin título'}</div>
                    <div class="obra-details">
                        ${obra.technique ? obra.technique + '<br>' : ''}
                        ${obra.dimensions ? obra.dimensions + '<br>' : ''}
                        ${obra.year ? obra.year + '<br>' : ''}
                        ${obra.collection ? '<em style="color: #d4af37; font-size: 0.85em;">' + obra.collection + '</em>' : ''}
                    </div>
                    <a href="${whatsappUrl}" class="contact-artist" target="_blank" title="Consultar por esta obra">💬</a>
                `;'''
    
    contenido = re.sub(patron_load_obras, nuevo_html_obra, contenido, flags=re.DOTALL)
    
    with open("roxana_collection_fixed.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ 'Colección privada' ahora visible debajo de las obras")
    print("✓ Texto en dorado (#d4af37) y cursiva")
    print("✓ Tamaño ligeramente menor (0.85em)")
    print("✓ Solo aparece si la obra tiene colección especificada")
    
    print("\nArchivo: roxana_collection_fixed.html")
    print("Las obras con colección privada mostrarán el texto debajo")

if __name__ == "__main__":
    fix_collection_display()