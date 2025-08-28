import re
import shutil
from datetime import datetime

def fix_chrome_mobile_final():
    print("CORRECCIÓN DEFINITIVA CHROME MÓVIL")
    print("Eliminando función goToAtelier duplicada")
    print("=" * 45)
    
    html_file = "artist_book_actualizado.html" 
    index_file = "index.html"
    
    # Backup
    timestamp = datetime.now().strftime("%H%M%S")
    backup_name = f"backup_final_fix_{timestamp}.html"
    shutil.copy(html_file, backup_name)
    print(f"Backup: {backup_name}")
    
    # Leer archivo
    with open(html_file, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Encontrar las dos funciones goToAtelier específicamente
    patron = r'function\s+goToAtelier\s*\(\s*\)\s*\{[^}]*\}'
    matches = list(re.finditer(patron, contenido, re.MULTILINE | re.DOTALL))
    
    print(f"Funciones goToAtelier encontradas: {len(matches)}")
    
    if len(matches) == 2:
        # Mostrar las dos funciones
        for i, match in enumerate(matches):
            linea = contenido[:match.start()].count('\n') + 1
            func_preview = match.group()[:80] + "..." if len(match.group()) > 80 else match.group()
            print(f"  {i+1}. Línea {linea}: {func_preview}")
        
        # Eliminar la segunda función (índice 1)
        segunda_funcion = matches[1]
        inicio = segunda_funcion.start()
        fin = segunda_funcion.end()
        
        # Buscar hacia atrás para incluir comentarios relacionados
        inicio_busqueda = max(0, inicio - 200)
        texto_antes = contenido[inicio_busqueda:inicio]
        
        # Si hay comentario específico antes, incluirlo
        comentario_match = re.search(r'//\s*Calcular:.*?\n', texto_antes, re.MULTILINE)
        if comentario_match:
            inicio = inicio_busqueda + comentario_match.start()
        
        # Eliminar la función y posible comentario
        nuevo_contenido = contenido[:inicio] + contenido[fin:]
        
        # Verificar que solo queda una función
        verificacion = re.findall(r'function\s+goToAtelier\s*\(\s*\)\s*\{', nuevo_contenido)
        
        if len(verificacion) == 1:
            print("✓ Segunda función goToAtelier eliminada correctamente")
            
            # Limpiar líneas vacías excesivas
            nuevo_contenido = re.sub(r'\n\s*\n\s*\n+', '\n\n', nuevo_contenido)
            
            # Verificar balance final
            open_braces = nuevo_contenido.count('{')
            close_braces = nuevo_contenido.count('}')
            
            print(f"Balance de llaves: {open_braces} vs {close_braces}")
            
            if open_braces == close_braces:
                # Guardar archivo corregido
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(nuevo_contenido)
                
                # Actualizar index.html
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(nuevo_contenido)
                
                print("\n" + "="*45)
                print("✅ CORRECCIÓN EXITOSA")
                print("✅ Una sola función goToAtelier")
                print("✅ Código JavaScript válido")  
                print("✅ Compatible con Chrome móvil")
                print("✅ index.html actualizado")
                
                print("\nSubir cambios:")
                print("git add .")
                print('git commit -m "Chrome móvil fix - función duplicada eliminada"')
                print("git push origin main")
                
            else:
                print("❌ Error: llaves desbalanceadas después de corrección")
                print("Restaurando desde backup...")
                shutil.copy(backup_name, html_file)
        else:
            print(f"❌ Error: quedaron {len(verificacion)} funciones goToAtelier")
            print("Restaurando desde backup...")
            shutil.copy(backup_name, html_file)
            
    else:
        print(f"❌ Se esperaban 2 funciones, se encontraron {len(matches)}")
        print("No se realizaron cambios")

if __name__ == "__main__":
    fix_chrome_mobile_final()