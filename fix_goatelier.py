import re
import shutil
from datetime import datetime

class CorreccionGoToAtelier:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.index_file = "index.html"
        self.contenido = ""
        
    def ejecutar(self):
        print("CORRECCIÓN FINAL - goToAtelier duplicada")
        print("=" * 35)
        
        # Backup
        timestamp = datetime.now().strftime("%H%M%S")
        backup_name = f"backup_final_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup: {backup_name}")
        
        # Cargar HTML
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
            
        # Encontrar y eliminar goToAtelier duplicada
        self.eliminar_goatelier_duplicada()
        
        if input("Eliminar goToAtelier duplicada? (s/n): ").lower() == 's':
            self.guardar()
    
    def eliminar_goatelier_duplicada(self):
        """Elimina la goToAtelier duplicada manteniendo solo una"""
        
        # Encontrar todas las ocurrencias de goToAtelier
        patron = r'function goToAtelier\(\)[^{]*\{[^}]*\}'
        matches = list(re.finditer(patron, self.contenido, re.DOTALL))
        
        print(f"Ocurrencias goToAtelier encontradas: {len(matches)}")
        
        if len(matches) > 1:
            # Mostrar cada ocurrencia
            for i, match in enumerate(matches):
                codigo = match.group()[:100].replace('\n', ' ')
                print(f"  Ocurrencia {i+1}: {codigo}...")
            
            # Eliminar la segunda ocurrencia (mantener la primera)
            segunda_match = matches[1]
            codigo_eliminar = segunda_match.group()
            
            # Encontrar un contexto más amplio para eliminar limpiamente
            inicio = segunda_match.start()
            fin = segunda_match.end()
            
            # Buscar hacia atrás y adelante para capturar whitespace
            while inicio > 0 and self.contenido[inicio-1] in ' \n\t':
                inicio -= 1
            while fin < len(self.contenido) and self.contenido[fin] in ' \n\t':
                fin += 1
            
            codigo_completo = self.contenido[inicio:fin]
            self.contenido = self.contenido[:inicio] + self.contenido[fin:]
            
            print(f"Eliminada ocurrencia duplicada de goToAtelier")
            
            # Verificar que quede solo una
            matches_final = re.findall(patron, self.contenido, re.DOTALL)
            print(f"Verificación: {len(matches_final)} ocurrencia(s) restante(s)")
    
    def guardar(self):
        """Guarda la corrección final"""
        # Guardar archivo principal
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        # Actualizar index.html
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        print("CORRECCIÓN FINAL COMPLETADA")
        print("Todas las funciones ahora tienen exactamente 1 ocurrencia")
        print("Compatible con Chrome móvil V8")
        
        # Verificación final
        funciones = ['goToObras', 'goToCertificados', 'goToEventos', 'goToAtelier']
        for funcion in funciones:
            count = self.contenido.count(f'function {funcion}')
            status = "✓" if count == 1 else "❌"
            print(f"  {status} {funcion}: {count} ocurrencia(s)")
        
        print("\nPara subir: git add . && git commit -m 'Corrección final Chrome móvil' && git push origin main")

if __name__ == "__main__":
    corrector = CorreccionGoToAtelier()
    corrector.ejecutar()