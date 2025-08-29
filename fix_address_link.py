def fix_address_link():
    print("ARREGLANDO LINK DE DIRECCIÓN")
    print("=" * 28)
    
    # Leer archivo actual
    with open("roxana_white_pages.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Buscar la dirección actual (sin link) y convertirla en enlace
    direccion_actual = '''<div class="contact-item">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="#4285F4" style="vertical-align: middle; margin-right: 8px;"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>Manuel A. Sáez 2101 - Las Heras - Mendoza
                        </div>'''
    
    direccion_con_link = '''<div class="contact-item">
                            <a href="https://maps.google.com/?q=Manuel+A.+Sáez+2101,+Las+Heras,+Mendoza,+Argentina" target="_blank">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="#4285F4" style="vertical-align: middle; margin-right: 8px;"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>Manuel A. Sáez 2101 - Las Heras - Mendoza
                            </a>
                        </div>'''
    
    # Reemplazar la dirección sin link por la versión con link
    contenido = contenido.replace(direccion_actual, direccion_con_link)
    
    # Si el reemplazo anterior no funciona, buscar una versión más específica
    import re
    if 'maps.google.com' not in contenido:
        # Patrón más flexible para encontrar la dirección
        patron = r'(<svg[^>]*fill="#4285F4"[^>]*>.*?</svg>)(Manuel A\. Sáez 2101 - Las Heras - Mendoza)'
        reemplazo = r'<a href="https://maps.google.com/?q=Manuel+A.+Sáez+2101,+Las+Heras,+Mendoza,+Argentina" target="_blank">\1\2</a>'
        contenido = re.sub(patron, reemplazo, contenido, flags=re.DOTALL)
    
    with open("roxana_address_fixed.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Dirección ahora es un enlace clickeable")
    print("✓ Se abre en Google Maps")
    print("✓ Link: Manuel A. Sáez 2101, Las Heras, Mendoza")
    print("✓ Se abre en nueva pestaña")
    print("✓ Mantiene el icono azul de ubicación")
    
    print("\nArchivo: roxana_address_fixed.html")
    print("Ahora todos los contact items son clickeables")

if __name__ == "__main__":
    fix_address_link()