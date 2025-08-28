import re

def fix_javascript_data():
    print("CORRIGIENDO DATOS JAVASCRIPT")
    print("=" * 35)
    
    # Leer el archivo con problemas
    with open("roxana_swipe_completa.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Leer el archivo original para obtener datos correctos
    with open("artist_book_actualizado.html", "r", encoding="utf-8") as f:
        original = f.read()
    
    # Extraer correctamente el catalogWorks como JavaScript válido
    patron_catalog = r"const catalogWorks = (\[[\s\S]*?\]);;"
    match_catalog = re.search(patron_catalog, original)
    catalog_js = "[]"
    
    if match_catalog:
        catalog_js = match_catalog.group(1)
        print("✓ Catálogo extraído correctamente")
    
    # Extraer certificateData correctamente
    patron_cert = r"const certificateData = (\[[\s\S]*?\]);"
    match_cert = re.search(patron_cert, original)
    cert_js = "[]"
    
    if match_cert:
        cert_js = match_cert.group(1)
        print("✓ Certificados extraídos correctamente")
    
    # Reemplazar los datos problemáticos en el archivo
    # Buscar y reemplazar const catalogWorks
    patron_replace_catalog = r"const catalogWorks = \[.*?\];"
    contenido_corregido = re.sub(patron_replace_catalog, f"const catalogWorks = {catalog_js};", contenido, flags=re.DOTALL)
    
    # Buscar y reemplazar const certificateData
    patron_replace_cert = r"const certificateData = \[.*?\];"
    contenido_corregido = re.sub(patron_replace_cert, f"const certificateData = {cert_js};", contenido_corregido, flags=re.DOTALL)
    
    # Guardar el archivo corregido
    with open("roxana_swipe_fixed.html", "w", encoding="utf-8") as f:
        f.write(contenido_corregido)
    
    print("✅ JAVASCRIPT CORREGIDO")
    print("Archivo: roxana_swipe_fixed.html")
    print("\nAhora ejecuta:")
    print("copy roxana_swipe_fixed.html index.html")
    print("git add .")
    print("git commit -m 'JavaScript corregido - datos dinámicos'")
    print("git push origin main")

if __name__ == "__main__":
    fix_javascript_data()