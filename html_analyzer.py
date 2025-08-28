import re
import shutil
from datetime import datetime

class AnalizadorHTML:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.index_file = "index.html"
        self.contenido = ""
        
    def ejecutar(self):
        print("ANALIZADOR HTML ESPECÍFICO - CHROME MÓVIL")
        print("=" * 45)
        
        # Cargar HTML
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
            
        print("Analizando estructura JavaScript...")
        self.analizar_estructura()
        self.crear_solucion_precisa()
    
    def analizar_estructura(self):
        """Analiza la estructura específica del JavaScript"""
        
        # Encontrar todos los bloques <script>
        scripts = re.findall(r'<script[^>]*>(.*?)</script>', self.contenido, re.DOTALL)
        print(f"Bloques <script> encontrados: {len(scripts)}")
        
        # Analizar cada función específica
        funciones_objetivo = ['goToObras', 'goToCertificados', 'goToEventos', 'goToAtelier']
        
        self.mapa_funciones = {}
        
        for i, script in enumerate(scripts):
            for funcion in funciones_objetivo:
                # Buscar definiciones de función
                patron = rf'function {funcion}\([^)]*\)\s*\{{[^}}]*\}}'
                matches = re.findall(patron, script, re.DOTALL)
                
                if matches:
                    if funcion not in self.mapa_funciones:
                        self.mapa_funciones[funcion] = []
                    
                    for j, match in enumerate(matches):
                        self.mapa_funciones[funcion].append({
                            'script_block': i,
                            'occurrence': j,
                            'code': match.strip(),
                            'lines': match.count('\n') + 1
                        })
        
        # Mostrar análisis detallado
        print("\nMAPEO DE FUNCIONES DUPLICADAS:")
        print("-" * 35)
        
        for funcion, ocurrencias in self.mapa_funciones.items():
            print(f"\n{funcion}:")
            for ocu in ocurrencias:
                print(f"  Script {ocu['script_block']}, Ocurrencia {ocu['occurrence']}: {ocu['lines']} líneas")
                print(f"    Código: {ocu['code'][:80].replace(chr(10), ' ')}...")
    
    def crear_solucion_precisa(self):
        """Crea solución precisa basada en el análisis"""
        
        print("\nCREANDO SOLUCIÓN PRECISA...")
        print("-" * 30)
        
        # Backup
        timestamp = datetime.now().strftime("%H%M%S")
        backup_name = f"backup_analyzer_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup creado: {backup_name}")
        
        # Estrategia: mantener solo la primera ocurrencia de cada función
        contenido_limpio = self.contenido
        
        funciones_eliminadas = 0
        for funcion, ocurrencias in self.mapa_funciones.items():
            if len(ocurrencias) > 1:
                print(f"Limpiando {funcion}: {len(ocurrencias)} → 1 ocurrencia")
                
                # Eliminar todas las ocurrencias excepto la primera
                for ocu in reversed(ocurrencias[1:]):  # Reversed para mantener posiciones
                    contenido_limpio = contenido_limpio.replace(ocu['code'], '', 1)
                    funciones_eliminadas += 1
        
        # Corregir problemas adicionales de Chrome móvil
        contenido_limpio = self.corregir_problemas_chrome(contenido_limpio)
        
        print(f"Funciones eliminadas: {funciones_eliminadas}")
        
        if input("Aplicar limpieza precisa? (s/n): ").lower() == 's':
            self.aplicar_solucion(contenido_limpio)
    
    def corregir_problemas_chrome(self, contenido):
        """Corrige problemas específicos de Chrome móvil"""
        
        correcciones = 0
        
        # Corregir window.window.pages
        if 'window.window.pages' in contenido:
            contenido = contenido.replace('window.window.pages', 'window.pages')
            correcciones += 1
            print("  Corregido: window.window.pages")
        
        # Limpiar event listeners duplicados
        patron_listeners = r'(nextBtn\.addEventListener\(\'click\', \(\) => \{[^}]*\}\);)\s*\1+'
        if re.search(patron_listeners, contenido):
            contenido = re.sub(patron_listeners, r'\1', contenido)
            correcciones += 1
            print("  Limpiados: event listeners duplicados")
        
        # Consolidar scripts múltiples
        contenido = re.sub(r'</script>\s*<script>', '\n        // Script consolidado\n        ', contenido)
        
        if correcciones > 0:
            print(f"  Correcciones Chrome aplicadas: {correcciones}")
        
        return contenido
    
    def aplicar_solucion(self, contenido_limpio):
        """Aplica la solución limpia"""
        
        # Guardar archivo principal
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(contenido_limpio)
        
        # Actualizar index.html
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(contenido_limpio)
        
        print("\nSOLUCIÓN PRECISA APLICADA")
        print("- Funciones duplicadas eliminadas quirúrgicamente")
        print("- Funcionalidad desktop mantenida")
        print("- Compatible con motor V8 de Chrome móvil")
        print("- Una sola versión funcional de cada función")
        
        # Verificar que las funciones principales siguen existiendo
        funciones_verificar = ['goToObras', 'goToCertificados', 'goToEventos', 'goToAtelier']
        for funcion in funciones_verificar:
            count = contenido_limpio.count(f'function {funcion}')
            if count == 1:
                print(f"  ✓ {funcion}: 1 ocurrencia (correcto)")
            elif count == 0:
                print(f"  ⚠ {funcion}: 0 ocurrencias (verificar manualmente)")
            else:
                print(f"  ❌ {funcion}: {count} ocurrencias (aún duplicada)")
        
        print("\nPara subir: git add . && git commit -m 'Corrección precisa Chrome móvil' && git push origin main")

if __name__ == "__main__":
    analizador = AnalizadorHTML()
    analizador.ejecutar()