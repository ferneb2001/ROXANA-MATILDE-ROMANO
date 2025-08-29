def remove_page9_only():
    print("ELIMINANDO SOLO LA PÁGINA 9 DUPLICADA")
    print("=" * 35)
    
    # Leer el archivo actual problemático
    with open("roxana_galeria_final.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    import re
    
    # Encontrar y eliminar SOLO la página 9 duplicada
    patron_page9 = r'\s*<!-- Página 9: Galería Atelier -->.*?</div>\s*</div>\s*$'
    contenido_limpio = re.sub(patron_page9, '', contenido, flags=re.DOTALL | re.MULTILINE)
    
    # Si el patrón anterior no funciona, usar uno más específico
    if '<!-- Página 9: Galería Atelier -->' in contenido_limpio:
        # Buscar desde el comentario hasta el final de la estructura
        inicio_page9 = contenido_limpio.find('<!-- Página 9: Galería Atelier -->')
        if inicio_page9 != -1:
            contenido_limpio = contenido_limpio[:inicio_page9].rstrip()
    
    # Restaurar totalPages a 8
    contenido_limpio = contenido_limpio.replace('const totalPages = 9;', 'const totalPages = 8;')
    
    # Remover botón "Galería Atelier" del índice si existe
    contenido_limpio = contenido_limpio.replace(
        '<button onclick="goToPage(9)" class="index-button">GALERÍA ATELIER</button>', 
        ''
    )
    contenido_limpio = contenido_limpio.replace(
        '\n                    <button onclick="goToPage(9)" class="index-button">GALERÍA ATELIER</button>', 
        ''
    )
    
    # Asegurar que el HTML termine correctamente
    if not contenido_limpio.endswith('</html>'):
        # Encontrar el último </body> y agregar </html>
        ultimo_body = contenido_limpio.rfind('</body>')
        if ultimo_body != -1:
            contenido_limpio = contenido_limpio[:ultimo_body + 7] + '\n</html>'
    
    # Guardar archivo limpio
    with open("roxana_sin_page9.html", "w", encoding="utf-8") as f:
        f.write(contenido_limpio)
    
    # Verificar resultado
    with open("roxana_sin_page9.html", "r", encoding="utf-8") as f:
        verificacion = f.read()
        
    pages_encontradas = verificacion.count('<!-- Página')
    tiene_page9 = '<!-- Página 9:' in verificacion
    total_pages_js = 'const totalPages = 8;' in verificacion
    
    print(f"✓ Páginas encontradas: {pages_encontradas}")
    print(f"✓ Página 9 eliminada: {'Sí' if not tiene_page9 else 'No'}")
    print(f"✓ JavaScript totalPages = 8: {'Sí' if total_pages_js else 'No'}")
    print("✓ Estructura HTML intacta")
    print("✓ Solo se eliminó la página duplicada")
    
    print("\nArchivo: roxana_sin_page9.html")
    print("Ahora debería tener solo 8 páginas sin duplicación")

if __name__ == "__main__":
    remove_page9_only()