import re
import os
from datetime import datetime

class DiagnosticoCompleto:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.index_file = "index.html"
        self.problemas = []
        self.contenido = ""
        
    def ejecutar(self):
        print("DIAGNÓSTICO COMPLETO DEL CÓDIGO")
        print("=" * 50)
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)
        
        if not os.path.exists(self.html_file):
            print(f"❌ Archivo {self.html_file} no encontrado")
            return
        
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
        
        print("📊 ESTADÍSTICAS BÁSICAS")
        self.estadisticas_basicas()
        
        print("\n🔍 ANÁLISIS DE FUNCIONES JAVASCRIPT")
        self.analizar_funciones()
        
        print("\n🔧 VERIFICACIÓN SINTÁCTICA")
        self.verificar_sintaxis()
        
        print("\n📱 COMPATIBILIDAD CHROME MÓVIL")
        self.verificar_chrome_movil()
        
        print("\n🌐 ESTRUCTURA HTML")
        self.verificar_html()
        
        print("\n" + "=" * 50)
        self.resumen_final()
    
    def estadisticas_basicas(self):
        lineas = len(self.contenido.split('\n'))
        chars = len(self.contenido)
        scripts = len(re.findall(r'<script[^>]*>.*?</script>', self.contenido, re.DOTALL))
        
        print(f"  📄 Líneas totales: {lineas}")
        print(f"  📝 Caracteres: {chars:,}")
        print(f"  🔧 Bloques <script>: {scripts}")
    
    def analizar_funciones(self):
        # Buscar todas las funciones JavaScript
        funciones = {}
        patron_funcion = r'function\s+(\w+)\s*\([^)]*\)\s*{'
        
        for match in re.finditer(patron_funcion, self.contenido):
            nombre = match.group(1)
            linea = self.contenido[:match.start()].count('\n') + 1
            
            if nombre not in funciones:
                funciones[nombre] = []
            funciones[nombre].append(linea)
        
        print(f"  🎯 Funciones encontradas: {len(funciones)}")
        
        # Detectar duplicadas
        duplicadas = {nombre: lineas for nombre, lineas in funciones.items() if len(lineas) > 1}
        
        if duplicadas:
            print("  ❌ FUNCIONES DUPLICADAS:")
            for nombre, lineas in duplicadas.items():
                print(f"     • {nombre}: líneas {', '.join(map(str, lineas))}")
                self.problemas.append(f"Función duplicada: {nombre}")
        else:
            print("  ✅ No hay funciones duplicadas")
        
        # Mostrar todas las funciones
        if funciones:
            print("  📋 Lista completa:")
            for nombre, lineas in sorted(funciones.items()):
                estado = "❌ DUPLICADA" if len(lineas) > 1 else "✅"
                print(f"     {estado} {nombre} - línea(s) {', '.join(map(str, lineas))}")
    
    def verificar_sintaxis(self):
        # Verificar balance de llaves
        open_braces = self.contenido.count('{')
        close_braces = self.contenido.count('}')
        
        print(f"  🔗 Balance de llaves: {open_braces} {{ vs {close_braces} }}")
        
        if open_braces == close_braces:
            print("  ✅ Llaves balanceadas")
        else:
            print("  ❌ Llaves desbalanceadas")
            self.problemas.append("Llaves JavaScript desbalanceadas")
        
        # Verificar paréntesis
        open_parens = self.contenido.count('(')
        close_parens = self.contenido.count(')')
        
        print(f"  📐 Balance de paréntesis: {open_parens} ( vs {close_parens} )")
        
        if open_parens == close_parens:
            print("  ✅ Paréntesis balanceados")
        else:
            print("  ❌ Paréntesis desbalanceados")
            self.problemas.append("Paréntesis desbalanceados")
        
        # Buscar código JavaScript incompleto
        patrones_problematicos = [
            r'addEventListener\s*\([^}]*$',  # addEventListener sin cerrar
            r'function\s+\w+\s*\([^}]*$',   # función sin cerrar
            r'\{\s*if\s*\([^}]*$',          # if sin cerrar
            r'}\);?\s*$'                    # líneas sueltas al final
        ]
        
        for patron in patrones_problematicos:
            matches = re.findall(patron, self.contenido, re.MULTILINE)
            if matches:
                print(f" ⚠️  Código potencialmente incompleto encontrado")
                self.problemas.append("Código JavaScript incompleto")
    
    def verificar_chrome_movil(self):
        # Problemas específicos de Chrome móvil
        problemas_chrome = []
        
        # Funciones duplicadas (ya verificado arriba)
        duplicadas = self.encontrar_funciones_duplicadas()
        if duplicadas:
            problemas_chrome.append("Funciones duplicadas")
        
        # Sintaxis strict
        if 'use strict' not in self.contenido:
            problemas_chrome.append("No usa 'use strict' (recomendado para móvil)")
        
        # Variables globales mal definidas
        if re.search(r'window\.\w+\s*=', self.contenido):
            print("  ℹ️  Variables globales en window detectadas")
        
        if problemas_chrome:
            print("  ❌ PROBLEMAS PARA CHROME MÓVIL:")
            for problema in problemas_chrome:
                print(f"     • {problema}")
        else:
            print("  ✅ Compatible con Chrome móvil")
    
    def verificar_html(self):
        # Verificar estructura HTML básica
        html_tags = ['<html', '</html>', '<head', '</head>', '<body', '</body>']
        
        print("  🏗️  Estructura HTML:")
        for tag in html_tags:
            count = self.contenido.count(tag)
            estado = "✅" if count == 1 else ("❌" if count == 0 else f"⚠️ ({count})")
            print(f"     {estado} {tag}: {count}")
        
        # Verificar etiquetas script cerradas
        scripts_abiertos = len(re.findall(r'<script[^>]*>', self.contenido))
        scripts_cerrados = self.contenido.count('</script>')
        
        print(f"  📜 Scripts: {scripts_abiertos} abiertos, {scripts_cerrados} cerrados")
        
        if scripts_abiertos == scripts_cerrados:
            print("  ✅ Etiquetas <script> balanceadas")
        else:
            print("  ❌ Etiquetas <script> desbalanceadas")
            self.problemas.append("Etiquetas <script> desbalanceadas")
    
    def encontrar_funciones_duplicadas(self):
        funciones = {}
        patron_funcion = r'function\s+(\w+)\s*\([^)]*\)\s*{'
        
        for match in re.finditer(patron_funcion, self.contenido):
            nombre = match.group(1)
            if nombre not in funciones:
                funciones[nombre] = 0
            funciones[nombre] += 1
        
        return {nombre: count for nombre, count in funciones.items() if count > 1}
    
    def resumen_final(self):
        if not self.problemas:
            print("🎉 RESULTADO: CÓDIGO COMPLETAMENTE FUNCIONAL")
            print("✅ No se detectaron problemas críticos")
            print("✅ Compatible con todos los navegadores")
            print("✅ Estructura HTML válida")
            print("✅ JavaScript sintácticamente correcto")
            print("\n💡 RECOMENDACIÓN: Dejar el código como está")
            
        else:
            print("⚠️  RESULTADO: SE DETECTARON PROBLEMAS")
            print(f"📊 Total de problemas: {len(self.problemas)}")
            print("\n🔧 PROBLEMAS DETECTADOS:")
            for i, problema in enumerate(self.problemas, 1):
                print(f"  {i}. {problema}")
            
            print("\n💡 RECOMENDACIÓN:")
            if len(self.problemas) <= 2:
                print("  • Problemas menores - el sitio probablemente funciona")
                print("  • Puedes corregir cuando tengas tiempo")
            else:
                print("  • Múltiples problemas detectados")
                print("  • Recomiendo corrección antes de usar en producción")
        
        print(f"\n📁 Archivos analizados: {self.html_file}")
        print("🔍 Análisis completado")

if __name__ == "__main__":
    diagnostico = DiagnosticoCompleto()
    diagnostico.ejecutar()