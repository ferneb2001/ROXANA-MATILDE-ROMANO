import os
import shutil
import re
from datetime import datetime

class CorregirImagenesMovil:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.index_file = "index.html"
        self.contenido = ""
        
    def ejecutar(self):
        print("CORREGIR IMÁGENES EN MÓVILES")
        print("=" * 30)
        
        # Backup
        timestamp = datetime.now().strftime("%H%M%S")
        backup_name = f"backup_img_fix_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup: {backup_name}")
        
        # Cargar HTML
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
        
        print("Aplicando corrección de imágenes móviles...")
        self.corregir_imagenes_movil()
        
        if input("Guardar cambios? (s/n): ").lower() == 's':
            self.guardar()
    
    def corregir_imagenes_movil(self):
        """Corrige específicamente las imágenes que se cortan en móvil"""
        
        # CSS específico para imágenes móviles
        css_imagenes_movil = """
        
        /* CORRECCIÓN ESPECÍFICA IMÁGENES MÓVILES */
        @media (max-width: 768px) {
            /* Todas las imágenes responsivas */
            img {
                max-width: 100% !important;
                height: auto !important;
                display: block !important;
                margin: 0 auto !important;
                box-sizing: border-box !important;
            }
            
            /* Contenedores de páginas */
            .page {
                width: 100% !important;
                max-width: 100% !important;
                padding: 10px !important;
                margin: 5px 0 !important;
                box-sizing: border-box !important;
                overflow: hidden !important;
            }
            
            /* Contenedor principal del libro */
            .book-container, .container {
                width: 100% !important;
                max-width: 100% !important;
                padding: 5px !important;
                margin: 0 !important;
                overflow-x: hidden !important;
            }
            
            /* Imágenes del catálogo */
            .work-item img, .catalog-image {
                width: 100% !important;
                max-width: 280px !important;
                height: auto !important;
                margin: 0 auto 10px auto !important;
            }
            
            /* Imágenes de certificados */
            .certificate-item img, .certificate-image {
                width: 100% !important;
                max-width: 250px !important;
                height: auto !important;
                margin: 0 auto !important;
            }
            
            /* Imágenes de eventos */
            .event-item img, .event-image {
                width: 100% !important;
                max-width: 240px !important;
                height: auto !important;
                margin: 0 auto 10px auto !important;
            }
            
            /* Imágenes del atelier */
            .atelier-image, .atelier-photo {
                width: 100% !important;
                max-width: 260px !important;
                height: auto !important;
                margin: 10px auto !important;
                display: block !important;
            }
            
            /* Corrección para imágenes dentro de divs */
            .page div img, .content img {
                width: 100% !important;
                max-width: 300px !important;
                height: auto !important;
            }
            
            /* Evitar desbordamiento horizontal */
            * {
                max-width: 100% !important;
                box-sizing: border-box !important;
            }
            
            html, body {
                overflow-x: hidden !important;
                width: 100% !important;
            }
        }
        
        @media (max-width: 480px) {
            /* Imágenes aún más pequeñas para celulares muy pequeños */
            .work-item img, .catalog-image {
                max-width: 240px !important;
            }
            
            .certificate-item img, .certificate-image {
                max-width: 220px !important;
            }
            
            .event-item img, .event-image {
                max-width: 200px !important;
            }
            
            .atelier-image, .atelier-photo {
                max-width: 220px !important;
            }
        }
        """
        
        # Buscar si ya existe CSS móvil y reemplazarlo
        if '/* OPTIMIZACIONES MÓVILES */' in self.contenido:
            # Reemplazar CSS móvil existente
            inicio = self.contenido.find('/* OPTIMIZACIONES MÓVILES */')
            if inicio != -1:
                # Buscar el final del bloque CSS móvil
                fin = self.contenido.find('</style>', inicio)
                if fin != -1:
                    # Reemplazar todo el CSS móvil
                    parte_antes = self.contenido[:inicio]
                    parte_despues = self.contenido[fin:]
                    self.contenido = parte_antes + css_imagenes_movil + '\n' + parte_despues
                    print("CSS móvil existente reemplazado con corrección de imágenes")
                else:
                    print("No se pudo encontrar el final del CSS")
            else:
                print("No se encontró el inicio del CSS móvil")
        else:
            # Agregar CSS móvil nuevo
            if '</style>' in self.contenido:
                self.contenido = self.contenido.replace('</style>', css_imagenes_movil + '\n</style>')
                print("CSS móvil para imágenes agregado")
            else:
                print("No se encontró tag </style>")
    
    def guardar(self):
        """Guarda ambos archivos"""
        # Guardar archivo principal
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        # Actualizar index.html
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        print("Archivos guardados")
        print("Prueba nuevamente en modo responsive del navegador")
        print("Para subir: git add . && git commit -m 'Corrección imágenes móvil' && git push origin main")

if __name__ == "__main__":
    corrector = CorregirImagenesMovil()
    corrector.ejecutar()