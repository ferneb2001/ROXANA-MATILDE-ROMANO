import os
import shutil
import re
from datetime import datetime

class CorregirChromeSimple:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.index_file = "index.html"
        self.contenido = ""
        
    def ejecutar(self):
        print("CORRECTOR CHROME MOVIL - VERSION SIMPLE")
        print("=" * 40)
        
        # Backup
        timestamp = datetime.now().strftime("%H%M%S")
        backup_name = f"backup_chrome_simple_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup: {backup_name}")
        
        # Cargar HTML
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
        
        print("\nOpciones:")
        print("1. Diagnosticar problemas Chrome")
        print("2. Corregir caracteres especiales")
        print("3. Simplificar CSS problemático")
        print("4. Corregir JavaScript duplicado")
        print("5. Aplicar todas las correcciones")
        print("6. Salir")
        
        opcion = input("\nOpción: ").strip()
        
        if opcion == "1":
            self.diagnosticar()
        elif opcion == "2":
            self.corregir_caracteres()
        elif opcion == "3":
            self.simplificar_css()
        elif opcion == "4":
            self.corregir_js()
        elif opcion == "5":
            self.aplicar_todas()
        elif opcion == "6":
            return
        else:
            print("Opción no válida")
            return
            
        if input("\nGuardar cambios? (s/n): ").lower() == 's':
            self.guardar()
    
    def diagnosticar(self):
        """Diagnostica problemas comunes"""
        print("\nDIAGNÓSTICO:")
        print("-" * 20)
        
        # Caracteres problemáticos
        problemas_codificacion = self.contenido.count("Ã")
        if problemas_codificacion > 0:
            print(f"❌ {problemas_codificacion} caracteres mal codificados")
        else:
            print("✅ Codificación correcta")
        
        # CSS excesivo
        important_count = self.contenido.count("!important")
        if important_count > 50:
            print(f"⚠️  {important_count} !important (Chrome puede rechazar)")
        else:
            print(f"✅ CSS moderado ({important_count} !important)")
        
        # JavaScript duplicado
        if self.contenido.count("function goToObras") > 1:
            print("❌ Funciones JavaScript duplicadas")
        else:
            print("✅ JavaScript sin duplicados")
        
        # Viewport problemático
        if "user-scalable=no" in self.contenido:
            print("⚠️  user-scalable=no puede causar problemas")
        else:
            print("✅ Viewport OK")
    
    def corregir_caracteres(self):
        """Corrige caracteres especiales problemáticos"""
        print("Corrigiendo caracteres...")
        
        cambios = 0
        
        # Correcciones básicas sin caracteres conflictivos
        if "Ã³" in self.contenido:
            self.contenido = self.contenido.replace("Ã³", "ó")
            cambios += self.contenido.count("Ã³")
            
        if "Ã±" in self.contenido:
            self.contenido = self.contenido.replace("Ã±", "ñ")
            cambios += 1
            
        if "Ã©" in self.contenido:
            self.contenido = self.contenido.replace("Ã©", "é")
            cambios += 1
            
        if "Ã­" in self.contenido:
            self.contenido = self.contenido.replace("Ã­", "í")
            cambios += 1
            
        if "Ã¡" in self.contenido:
            self.contenido = self.contenido.replace("Ã¡", "á")
            cambios += 1
            
        if "Ãº" in self.contenido:
            self.contenido = self.contenido.replace("Ãº", "ú")
            cambios += 1
        
        print(f"Caracteres corregidos: {cambios}")
    
    def simplificar_css(self):
        """Simplifica CSS problemático para Chrome"""
        print("Simplificando CSS...")
        
        cambios = 0
        
        # Eliminar !important excesivos en reglas básicas
        css_simple = [
            ("width: 100% !important", "width: 100%"),
            ("max-width: 100% !important", "max-width: 100%"),
            ("height: auto !important", "height: auto"),
            ("display: block !important", "display: block")
        ]
        
        for problema, solucion in css_simple:
            if problema in self.contenido:
                self.contenido = self.contenido.replace(problema, solucion)
                cambios += 1
        
        print(f"CSS simplificado: {cambios} reglas")
    
    def corregir_js(self):
        """Corrige JavaScript duplicado"""
        print("Corrigiendo JavaScript...")
        
        # Buscar y eliminar funciones duplicadas
        if "window.window.pages" in self.contenido:
            self.contenido = self.contenido.replace("window.window.pages", "window.pages")
            print("Corregido: window.window.pages")
        
        # Contar funciones duplicadas
        funciones = [
            "function goToObras",
            "function goToCertificados", 
            "function goToEventos",
            "function goToAtelier"
        ]
        
        duplicados = 0
        for funcion in funciones:
            count = self.contenido.count(funcion)
            if count > 1:
                duplicados += count - 1
        
        if duplicados > 0:
            print(f"⚠️  {duplicados} funciones duplicadas detectadas")
            print("Se recomienda limpiar manualmente")
        else:
            print("JavaScript sin duplicados críticos")
    
    def aplicar_todas(self):
        """Aplica todas las correcciones"""
        print("Aplicando todas las correcciones...")
        
        self.corregir_caracteres()
        self.simplificar_css()
        self.corregir_js()
        
        # Mejorar viewport para Chrome móvil
        if "user-scalable=no" in self.contenido:
            self.contenido = self.contenido.replace("user-scalable=no", "user-scalable=yes")
            print("Viewport mejorado para Chrome")
        
        print("Todas las correcciones aplicadas")
    
    def guardar(self):
        """Guarda ambos archivos"""
        # Guardar archivo principal
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        # Actualizar index.html
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        print("Archivos guardados")
        print("Prueba en Chrome móvil")
        print("Para subir: git add . && git commit -m 'Chrome móvil fix' && git push origin main")

if __name__ == "__main__":
    corrector = CorregirChromeSimple()
    corrector.ejecutar()