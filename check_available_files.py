import os

def check_available_files():
    print("ARCHIVOS HTML DISPONIBLES")
    print("=" * 25)
    
    # Buscar todos los archivos HTML
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    if html_files:
        for i, archivo in enumerate(sorted(html_files), 1):
            size = os.path.getsize(archivo)
            print(f"{i}. {archivo} ({size:,} bytes)")
    else:
        print("No se encontraron archivos HTML")
    
    print(f"\nTotal archivos HTML: {len(html_files)}")
    
    # Verificar archivos específicos que hemos creado
    archivos_esperados = [
        "roxana_8_texto_9_fotos.html",
        "roxana_estructura_corregida.html", 
        "roxana_iconos_reales.html",
        "roxana_sin_page9.html"
    ]
    
    print("\n--- ARCHIVOS DEL PROYECTO ---")
    for archivo in archivos_esperados:
        if os.path.exists(archivo):
            size = os.path.getsize(archivo)
            print(f"✓ {archivo} ({size:,} bytes)")
        else:
            print(f"✗ {archivo}")

if __name__ == "__main__":
    check_available_files()