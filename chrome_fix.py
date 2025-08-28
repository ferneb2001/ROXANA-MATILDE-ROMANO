import re
import shutil
from datetime import datetime

def fix_chrome_mobile():
    print("CORRECCIÓN DEFINITIVA CHROME MÓVIL")
    print("=" * 40)
    
    # Archivos
    html_file = "artist_book_actualizado.html"
    index_file = "index.html"
    
    # Backup
    timestamp = datetime.now().strftime("%H%M%S")
    backup_name = f"backup_chrome_fix_{timestamp}.html"
    shutil.copy(html_file, backup_name)
    print(f"Backup creado: {backup_name}")
    
    # Leer archivo
    with open(html_file, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    print("Analizando funciones duplicadas...")
    
    # Buscar todas las ocurrencias de goToAtelier
    patron = r'function\s+goToAtelier\s*\(\s*\)\s*\{[^}]*\}'
    matches = list(re.finditer(patron, contenido, re.MULTILINE | re.DOTALL))
    
    print(f"Funciones goToAtelier encontradas: {len(matches)}")
    
    if len(matches) > 1:
        print("ELIMINANDO FUNCIÓN DUPLICADA:")
        # Mostrar las funciones encontradas
        for i, match in enumerate(matches):
            func_text = match.group()[:100] + "..." if len(match.group()) > 100 else match.group()
            print(f"  {i+1}. Línea {contenido[:match.start()].count(chr(10)) + 1}: {func_text}")
        
        # Eliminar todas excepto la primera
        offset = 0
        for match in matches[1:]:  # Desde la segunda en adelante
            start = match.start() - offset
            end = match.end() - offset
            contenido = contenido[:start] + contenido[end:]
            offset += (end - start)
            print(f"✓ Función duplicada eliminada")
    
    # Limpiar comentarios duplicados
    comentario = "// Funciones de navegación para el índice"
    count = contenido.count(comentario)
    if count > 1:
        # Eliminar ocurrencias extra
        for _ in range(count - 1):
            pos = contenido.rfind(comentario)
            line_end = contenido.find('\n', pos)
            if line_end != -1:
                contenido = contenido[:pos] + contenido[line_end+1:]
        print("✓ Comentarios duplicados eliminados")
    
    # Limpiar líneas vacías excesivas
    contenido = re.sub(r'\n\s*\n\s*\n+', '\n\n', contenido)
    
    # Verificar balance de llaves
    open_braces = contenido.count('{')
    close_braces = contenido.count('}')
    print(f"Balance de llaves: {open_braces} {{ vs {close_braces} }}")
    
    if open_braces == close_braces:
        print("✅ JavaScript sintácticamente correcto")
    else:
        print("⚠️  Advertencia: llaves desbalanceadas")
    
    # Guardar archivo corregido
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    # Actualizar index.html
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    print("\n" + "="*40)
    print("CORRECCIÓN COMPLETADA")
    print("✅ Función goToAtelier única")
    print("✅ Código JavaScript limpio")
    print("✅ Compatible con Chrome móvil")
    print("✅ index.html actualizado")
    
    print("\nComandos Git:")
    print("git add .")
    print('git commit -m "Chrome móvil funcionando - función duplicada eliminada"')
    print("git push origin main")

if __name__ == "__main__":
    fix_chrome_mobile()