import re

def extraer_datos_roxana():
    print("EXTRAYENDO DATOS REALES DE ROXANA")
    print("=" * 40)
    
    # Leer el archivo original
    with open("artist_book_actualizado.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Leer el archivo migrado
    with open("roxana_completa_mobile.html", "r", encoding="utf-8") as f:
        contenido_mobile = f.read()
    
    datos_encontrados = {}
    
    # Buscar información de contacto específica
    patrones = {
        'telefono': r'(\+?54\s?9?\s?26\d{8,10}|\+?54\s?26\d{8,10}|26\d{8,10})',
        'email': r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
        'whatsapp': r'(wa\.me/[\d+]+|whatsapp.*?(\+?54\s?9?\s?26\d{8,10}))',
        'youtube': r'(youtube\.com/[^\s"\'<>]+|youtu\.be/[^\s"\'<>]+)',
        'instagram': r'(instagram\.com/[^\s"\'<>]+)',
        'direccion': r'(Mendoza|Las Heras|Argentina|Dirección[:\s]*([^<\n]+))'
    }
    
    for tipo, patron in patrones.items():
        matches = re.findall(patron, contenido, re.IGNORECASE)
        if matches:
            datos_encontrados[tipo] = matches
            print(f"✓ {tipo}: {matches}")
    
    # Buscar texto específico de Roxana
    patron_biografia = r'(Roxana[^<]*(?:<[^>]*>[^<]*)*artista[^<]*(?:<[^>]*>[^<]*)*)'
    match_bio = re.search(patron_biografia, contenido, re.IGNORECASE | re.DOTALL)
    if match_bio:
        biografia = re.sub(r'<[^>]+>', ' ', match_bio.group(1))
        datos_encontrados['biografia'] = biografia.strip()
        print(f"✓ Biografía encontrada: {biografia[:100]}...")
    
    # Buscar rutas de imágenes de Roxana
    patron_foto = r'(roxana[^"\']*\.(jpg|jpeg|png|gif))'
    matches_foto = re.findall(patron_foto, contenido, re.IGNORECASE)
    if matches_foto:
        datos_encontrados['foto'] = matches_foto
        print(f"✓ Fotos encontradas: {matches_foto}")
    
    # Actualizar el archivo móvil con los datos reales
    contenido_actualizado = contenido_mobile
    
    # Reemplazar placeholders con datos reales
    if 'telefono' in datos_encontrados:
        telefono = datos_encontrados['telefono'][0]
        if isinstance(telefono, tuple):
            telefono = telefono[0]
        contenido_actualizado = contenido_actualizado.replace('[EXTRAER DEL CÓDIGO ORIGINAL]', telefono)
        contenido_actualizado = contenido_actualizado.replace('[NÚMERO]', telefono.replace(' ', '').replace('+', ''))
    
    if 'email' in datos_encontrados:
        email = datos_encontrados['email'][0]
        contenido_actualizado = contenido_actualizado.replace('[EMAIL]', email)
    
    if 'biografia' in datos_encontrados:
        biografia = datos_encontrados['biografia']
        contenido_actualizado = contenido_actualizado.replace('[BIOGRAFÍA DE ROXANA - EXTRAER DEL CÓDIGO ORIGINAL]', biografia)
    
    # Buscar y extraer el número de WhatsApp específico
    patron_whatsapp_completo = r'wa\.me/(\d+)'
    match_wa = re.search(patron_whatsapp_completo, contenido)
    if match_wa:
        numero_wa = match_wa.group(1)
        contenido_actualizado = contenido_actualizado.replace('wa.me/[NÚMERO]', f'wa.me/{numero_wa}')
        print(f"✓ WhatsApp: {numero_wa}")
    
    # Guardar archivo actualizado
    with open("roxana_completa_actualizada.html", "w", encoding="utf-8") as f:
        f.write(contenido_actualizado)
    
    print("\n" + "=" * 40)
    print("✅ DATOS EXTRAÍDOS Y ACTUALIZADOS")
    print("Archivo: roxana_completa_actualizada.html")
    
    # Mostrar resumen
    print("\nDatos extraídos:")
    for tipo, datos in datos_encontrados.items():
        print(f"  {tipo}: {datos}")
    
    print("\nPróximos pasos:")
    print("1. Revisar roxana_completa_actualizada.html")
    print("2. Ajustar rutas de imágenes si es necesario")
    print("3. Probar en Chrome móvil")
    print("4. Si funciona: copy roxana_completa_actualizada.html index.html")

if __name__ == "__main__":
    extraer_datos_roxana()