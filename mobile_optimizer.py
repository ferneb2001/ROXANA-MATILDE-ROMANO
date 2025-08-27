import os
import shutil
import re
from datetime import datetime

class OptimizadorMovil:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.index_file = "index.html"
        self.contenido = ""
        
    def ejecutar(self):
        print("OPTIMIZADOR PARA DISPOSITIVOS MÓVILES")
        print("=" * 40)
        
        # Backup
        timestamp = datetime.now().strftime("%H%M%S")
        backup_name = f"backup_mobile_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup: {backup_name}")
        
        # Cargar HTML
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
        
        print("\nOpciones de optimización:")
        print("1. Agregar viewport responsivo")
        print("2. Optimizar CSS para móviles") 
        print("3. Ajustar navegación touch")
        print("4. Aplicar todas las optimizaciones")
        print("5. Solo mostrar problemas detectados")
        print("6. Salir")
        
        opcion = input("\nOpción: ").strip()
        
        if opcion == "1":
            self.agregar_viewport()
        elif opcion == "2":
            self.optimizar_css()
        elif opcion == "3":
            self.optimizar_navegacion()
        elif opcion == "4":
            self.aplicar_todas_optimizaciones()
        elif opcion == "5":
            self.detectar_problemas()
        elif opcion == "6":
            return
        else:
            print("Opción no válida")
            return
            
        if input("\nGuardar cambios? (s/n): ").lower() == 's':
            self.guardar()
    
    def detectar_problemas(self):
        """Detecta problemas comunes de responsive"""
        problemas = []
        
        # Verificar viewport
        if 'viewport' not in self.contenido.lower():
            problemas.append("❌ Falta meta viewport")
        else:
            problemas.append("✅ Meta viewport presente")
            
        # Verificar media queries
        if '@media' not in self.contenido:
            problemas.append("❌ Sin media queries para responsive")
        else:
            media_count = len(re.findall(r'@media', self.contenido))
            problemas.append(f"✅ {media_count} media queries encontradas")
            
        # Verificar anchos fijos
        anchos_fijos = re.findall(r'width:\s*\d+px', self.contenido)
        if anchos_fijos:
            problemas.append(f"⚠️  {len(anchos_fijos)} anchos fijos en px detectados")
        else:
            problemas.append("✅ Sin anchos fijos problemáticos")
            
        # Verificar tamaños de fuente
        fuentes_pequenas = re.findall(r'font-size:\s*[1-9]px', self.contenido)
        if fuentes_pequenas:
            problemas.append(f"⚠️  {len(fuentes_pequenas)} fuentes muy pequeñas para móvil")
        else:
            problemas.append("✅ Tamaños de fuente apropiados")
        
        print("\nPROBLEMAS DETECTADOS:")
        print("-" * 25)
        for problema in problemas:
            print(problema)
    
    def agregar_viewport(self):
        """Agrega meta viewport si no existe"""
        if 'viewport' in self.contenido.lower():
            print("Meta viewport ya existe")
            return
            
        # Buscar el </head>
        if '</head>' in self.contenido:
            viewport_tag = '    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">\n'
            self.contenido = self.contenido.replace('</head>', viewport_tag + '</head>')
            print("Meta viewport agregado")
        else:
            print("No se encontró tag </head>")
    
    def optimizar_css(self):
        """Optimiza CSS para dispositivos móviles"""
        print("Optimizando CSS para móviles...")
        
        # CSS móvil mejorado
        css_mobile = """
        
        /* OPTIMIZACIONES MÓVILES */
        @media (max-width: 768px) {
            body {
                font-size: 16px !important;
                line-height: 1.5 !important;
                padding: 10px !important;
                margin: 0 !important;
            }
            
            .container {
                width: 100% !important;
                max-width: 100% !important;
                padding: 10px !important;
                margin: 0 !important;
            }
            
            .page {
                width: 100% !important;
                min-height: auto !important;
                padding: 15px !important;
                margin: 10px 0 !important;
                box-sizing: border-box !important;
            }
            
            h1, h2, h3 {
                font-size: 1.5em !important;
                text-align: center !important;
                margin: 10px 0 !important;
            }
            
            /* Catálogo móvil */
            .catalog-grid {
                display: flex !important;
                flex-direction: column !important;
                gap: 20px !important;
            }
            
            .work-item {
                width: 100% !important;
                margin: 0 auto 20px auto !important;
                text-align: center !important;
            }
            
            .work-item img {
                width: 100% !important;
                max-width: 300px !important;
                height: auto !important;
                margin: 0 auto 10px auto !important;
                display: block !important;
            }
            
            .work-info {
                padding: 10px !important;
                text-align: left !important;
            }
            
            .work-info h3 {
                font-size: 1.2em !important;
                margin: 5px 0 !important;
            }
            
            .work-info p {
                font-size: 0.9em !important;
                margin: 3px 0 !important;
                line-height: 1.3 !important;
            }
            
            /* Navegación móvil */
            .nav-button {
                padding: 15px 20px !important;
                font-size: 16px !important;
                margin: 5px !important;
                min-height: 44px !important;
                touch-action: manipulation !important;
            }
            
            .nav-buttons {
                display: flex !important;
                flex-wrap: wrap !important;
                justify-content: center !important;
                gap: 10px !important;
                padding: 15px !important;
            }
            
            /* Certificados móvil */
            .certificates-grid {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                gap: 20px !important;
            }
            
            .certificate-item {
                width: 100% !important;
                max-width: 300px !important;
                text-align: center !important;
            }
            
            .certificate-item img {
                width: 100% !important;
                height: auto !important;
            }
            
            /* Eventos móvil */
            .event-item {
                width: 100% !important;
                margin: 15px 0 !important;
                padding: 15px !important;
                border: 1px solid #ddd !important;
                border-radius: 8px !important;
            }
            
            .event-item img {
                width: 100% !important;
                max-width: 250px !important;
                height: auto !important;
                margin: 0 auto 10px auto !important;
                display: block !important;
            }
            
            /* Datos personales móvil */
            .contact-item {
                display: flex !important;
                align-items: center !important;
                gap: 10px !important;
                padding: 10px !important;
                margin: 5px 0 !important;
            }
            
            .contact-item svg {
                width: 24px !important;
                height: 24px !important;
                flex-shrink: 0 !important;
            }
            
            .contact-item p {
                font-size: 14px !important;
                margin: 0 !important;
            }
            
            /* Atelier móvil */
            .atelier-photo {
                width: 100% !important;
                max-width: 280px !important;
                height: auto !important;
                margin: 10px auto !important;
                display: block !important;
            }
            
            /* Zoom móvil */
            .zoom-overlay {
                padding: 20px !important;
            }
            
            .zoomed-image {
                max-width: 90% !important;
                max-height: 90% !important;
            }
        }
        
        @media (max-width: 480px) {
            body {
                font-size: 14px !important;
                padding: 5px !important;
            }
            
            .page {
                padding: 10px !important;
                margin: 5px 0 !important;
            }
            
            h1, h2, h3 {
                font-size: 1.3em !important;
            }
            
            .nav-button {
                padding: 12px 15px !important;
                font-size: 14px !important;
            }
            
            .work-item img {
                max-width: 250px !important;
            }
        }
        """
        
        # Insertar CSS antes del </style>
        if '</style>' in self.contenido:
            self.contenido = self.contenido.replace('</style>', css_mobile + '\n</style>')
            print("CSS móvil agregado")
        else:
            print("No se encontró tag </style>")
    
    def optimizar_navegacion(self):
        """Optimiza la navegación para touch"""
        print("Optimizando navegación touch...")
        
        # Buscar y mejorar botones de navegación
        patron_botones = r'(<button[^>]*class="nav-button"[^>]*>)'
        botones = re.findall(patron_botones, self.contenido)
        
        for boton in botones:
            # Agregar atributos touch
            if 'style=' in boton:
                nuevo_boton = boton.replace('style="', 'style="touch-action: manipulation; min-height: 44px; ')
            else:
                nuevo_boton = boton.replace('>', ' style="touch-action: manipulation; min-height: 44px;">')
            
            self.contenido = self.contenido.replace(boton, nuevo_boton)
        
        print(f"Optimizados {len(botones)} botones para touch")
    
    def aplicar_todas_optimizaciones(self):
        """Aplica todas las optimizaciones móviles"""
        print("Aplicando todas las optimizaciones...")
        
        self.agregar_viewport()
        self.optimizar_css()
        self.optimizar_navegacion()
        
        print("Todas las optimizaciones aplicadas")
    
    def guardar(self):
        """Guarda los archivos"""
        # Guardar archivo principal
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        # Actualizar index.html
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        
        print("Archivos guardados")
        print("Para aplicar en web: git add . && git commit -m 'Optimización móvil' && git push origin main")

if __name__ == "__main__":
    optimizador = OptimizadorMovil()
    optimizador.ejecutar()