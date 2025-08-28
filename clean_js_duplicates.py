import re
import shutil
from datetime import datetime

class LimpiarJSDuplicado:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.index_file = "index.html"
        self.contenido = ""
        
    def ejecutar(self):
        print("LIMPIAR JAVASCRIPT DUPLICADO - CHROME MOBILE")
        print("=" * 45)
        
        # Backup
        timestamp = datetime.now().strftime("%H%M%S")
        backup_name = f"backup_js_clean_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup: {backup_name}")
        
        # Cargar HTML
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
            
        print("Limpiando funciones JavaScript duplicadas...")
        self.limpiar_funciones_duplicadas()
        
        if input("Guardar cambios? (s/n): ").lower() == 's':
            self.guardar()
    
    def limpiar_funciones_duplicadas(self):
        """Elimina funciones JavaScript duplicadas específicamente"""
        
        # Funciones que aparecen duplicadas
        funciones_problema = [
            'goToObras',
            'goToCertificados', 
            'goToEventos',
            'goToAtelier'
        ]
        
        for funcion in funciones_problema:
            # Buscar todas las ocurrencias de la función
            patron = rf'function {funcion}\(\)[^}}]*}}'
            matches = re.findall(patron, self.contenido, re.DOTALL)
            
            if len(matches) > 1:
                print(f"Función {funcion} encontrada {len(matches)} veces - eliminando duplicados")
                
                # Mantener solo la primera ocurrencia
                primera_match = matches[0]
                
                # Eliminar todas las ocurrencias
                self.contenido = re.sub(patron, '', self.contenido, flags=re.DOTALL)
                
                # Reinsertar solo una vez en el lugar correcto (dentro del primer script)
                script_pattern = r'(<script>.*?)(</script>)'
                def reemplazar_script(match):
                    script_inicio = match.group(1)
                    script_fin = match.group(2)
                    
                    # Agregar la función limpia al final del script
                    return script_inicio + f'\n    function {funcion}() {{\n        window.currentPageIndex = 5;\n        window.updatePages();\n    }}\n' + script_fin
                
                self.contenido = re.sub(script_pattern, reemplazar_script, self.contenido, count=1, flags=re.DOTALL)
        
        # Limpiar event listeners duplicados problemáticos
        self.limpiar_event_listeners()
        
        # Eliminar JavaScript duplicado al final del archivo
        self.eliminar_js_final_duplicado()
        
    def limpiar_event_listeners(self):
        """Limpia event listeners duplicados"""
        print("Limpiando event listeners duplicados...")
        
        # Buscar bloques de código repetido
        patrones_duplicados = [
            r'nextBtn\.addEventListener.*?}\);',
            r'prevBtn\.addEventListener.*?}\);',
            r'updatePages\(\);.*?updatePages\(\);'
        ]
        
        for patron in patrones_duplicados:
            matches = re.findall(patron, self.contenido, re.DOTALL)
            if len(matches) > 1:
                # Mantener solo la primera ocurrencia
                primera_match = matches[0]
                # Eliminar todas las ocurrencias
                self.contenido = re.sub(patron, '', self.contenido, flags=re.DOTALL)
                # Reinsertar solo una vez
                script_end = self.contenido.rfind('</script>')
                if script_end != -1:
                    self.contenido = self.contenido[:script_end] + '\n' + primera_match + '\n' + self.contenido[script_end:]
    
    def eliminar_js_final_duplicado(self):
        """Elimina JavaScript duplicado al final del archivo"""
        print("Eliminando JavaScript duplicado al final...")
        
        # Buscar múltiples bloques </script> seguidos
        patron_scripts_multiples = r'(</script>\s*<script>.*?function.*?</script>)'
        matches = re.findall(patron_scripts_multiples, self.contenido, re.DOTALL)
        
        if matches:
            print(f"Eliminando {len(matches)} bloques de script duplicados")
            for match in matches[1:]:  # Mantener solo el primero
                self.contenido = self.contenido.replace(match, '')
        
        # Verificar funciones duplicadas restantes
        funciones_restantes = [
            'goToObras',
            'goToCertificados', 
            'goToEventos',
            'goToAtelier'
        ]
        
        for funcion in funciones_restantes:
            count = self.contenido.count(f'function {funcion}')
            if count > 1:
                print(f"ADVERTENCIA: {funcion} aún aparece {count} veces")
            elif count == 1:
                print(f"✓ {funcion} limpia (1 ocurrencia)")
            else:
                print(f"⚠ {funcion} no encontrada")
    
    def guardar(self):
        """Guarda ambos archivos"""
        # Guardar archivo principal
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        # Actualizar index.html
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        print("Archivos guardados - JavaScript duplicado eliminado")
        print("Esto debería resolver el problema de Chrome móvil")
        print("Para subir: git add . && git commit -m 'Eliminación JS duplicado Chrome' && git push origin main")

if __name__ == "__main__":
    limpiador = LimpiarJSDuplicado()
    limpiador.ejecutar()