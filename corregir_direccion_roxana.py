import re

def corregir_direccion_roxana():
    print("CORRIGIENDO DIRECCIÓN DE ROXANA")
    print("=" * 40)
    
    # Leer el archivo actualizado
    with open("roxana_completa_actualizada.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Dirección correcta
    direccion_correcta = "Manuel A. Sáez 2101 - Las Heras - Mendoza"
    
    # Patrones a reemplazar
    patrones_direccion = [
        r"Las Heras, Mendoza, Argentina",
        r"Las Heras - Mendoza - Argentina", 
        r"Las Heras, Mendoza",
        r"Las Heras - Mendoza",
        r"\[EXTRAER DEL CÓDIGO ORIGINAL\]",
        r"Dirección:[^<\n]*"
    ]
    
    # Reemplazar con la dirección correcta
    contenido_corregido = contenido
    
    for patron in patrones_direccion:
        contenido_corregido = re.sub(patron, direccion_correcta, contenido_corregido, flags=re.IGNORECASE)
    
    # Buscar específicamente patrones de contacto para dirección
    patron_direccion_contacto = r'<div class="contact-item">\s*📍[^<]*<[^>]*>[^<]*</div>'
    reemplazo_direccion = f'''<div class="contact-item">
                    📍 Dirección: {direccion_correcta}
                </div>'''
    
    contenido_corregido = re.sub(patron_direccion_contacto, reemplazo_direccion, contenido_corregido, flags=re.DOTALL)
    
    # También buscar y reemplazar en datos personales
    patron_datos_personales = r'Manuel A\. Sáez[^<\n]*'
    if not re.search(patron_datos_personales, contenido_corregido):
        # Si no está, agregarlo donde corresponde
        patron_ubicacion = r'(📍[^<\n]*)'
        contenido_corregido = re.sub(patron_ubicacion, f'📍 Dirección: {direccion_correcta}', contenido_corregido)
    
    # Guardar archivo corregido
    with open("roxana_direccion_corregida.html", "w", encoding="utf-8") as f:
        f.write(contenido_corregido)
    
    print(f"Dirección corregida a: {direccion_correcta}")
    print("Archivo: roxana_direccion_corregida.html")
    
    # Verificar que se aplicó la corrección
    if direccion_correcta in contenido_corregido:
        print("✓ Dirección actualizada correctamente")
    else:
        print("⚠ Verificar manualmente - posible problema en reemplazo")
    
    print("\nPara actualizar el sitio:")
    print("1. copy roxana_direccion_corregida.html index.html")
    print("2. git add .")
    print("3. git commit -m 'Dirección corregida - Manuel A. Sáez 2101'")
    print("4. git push origin main")

if __name__ == "__main__":
    corregir_direccion_roxana()