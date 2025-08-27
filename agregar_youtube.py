import os
import shutil
from datetime import datetime

class AgregarYouTube:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.contenido = ""
        
    def ejecutar(self):
        print("AGREGAR YOUTUBE A DATOS PERSONALES")
        print("=" * 35)
        
        # Backup
        timestamp = datetime.now().strftime("%H%M%S")
        backup_name = f"backup_youtube_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup: {backup_name}")
        
        # Cargar HTML
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
        
        # Verificar si YouTube ya existe
        if '@roxanamatilderomano' in self.contenido and 'youtube' in self.contenido.lower():
            print("El enlace de YouTube ya existe en el HTML")
            return
        
        # Agregar YouTube
        if input("Agregar enlace de YouTube? (s/n): ").lower() == 's':
            self.agregar_youtube()
            if input("Guardar cambios? (s/n): ").lower() == 's':
                self.guardar()
    
    def agregar_youtube(self):
        """Agrega el enlace de YouTube después de Instagram"""
        print("Agregando enlace de YouTube...")
        
        # Buscar la sección de Instagram
        patron_instagram = r'(<div class="contact-item">.*?instagram.*?</div>)'
        
        import re
        match = re.search(patron_instagram, self.contenido, re.DOTALL | re.IGNORECASE)
        
        if match:
            seccion_instagram = match.group(1)
            posicion_fin = match.end()
            
            # HTML del enlace de YouTube
            youtube_html = '''
                <div class="contact-item">
                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                    </svg>
                    <p><a href="https://www.youtube.com/@roxanamatilderomano" target="_blank">@roxanamatilderomano</a></p>
                </div>'''
            
            # Insertar YouTube después de Instagram
            self.contenido = (self.contenido[:posicion_fin] + 
                            youtube_html + 
                            self.contenido[posicion_fin:])
            
            print("YouTube agregado después de Instagram")
            
        else:
            print("No se encontró la sección de Instagram")
            print("Buscando otra ubicación...")
            self.agregar_youtube_alternativo()
    
    def agregar_youtube_alternativo(self):
        """Método alternativo para agregar YouTube"""
        # Buscar cualquier contact-item
        patron_contact = r'(<div class="contact-item">.*?</div>)'
        
        import re
        matches = list(re.finditer(patron_contact, self.contenido, re.DOTALL))
        
        if matches:
            print(f"Encontrados {len(matches)} elementos de contacto")
            
            # Agregar después del último elemento de contacto
            ultimo_match = matches[-1]
            posicion_fin = ultimo_match.end()
            
            youtube_html = '''
                <div class="contact-item">
                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                    </svg>
                    <p><a href="https://www.youtube.com/@roxanamatilderomano" target="_blank">@roxanamatilderomano</a></p>
                </div>'''
            
            self.contenido = (self.contenido[:posicion_fin] + 
                            youtube_html + 
                            self.contenido[posicion_fin:])
            
            print("YouTube agregado al final de los datos de contacto")
        else:
            print("No se encontraron elementos de contacto")
    
    def guardar(self):
        """Guarda el archivo"""
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        print("Archivo guardado")
        
        # Verificar resultado
        if '@roxanamatilderomano' in self.contenido and 'youtube' in self.contenido.lower():
            print("YouTube agregado exitosamente")
        else:
            print("Verificación: No se pudo confirmar que YouTube se agregó")

if __name__ == "__main__":
    agregador = AgregarYouTube()
    agregador.ejecutar()