import os
import shutil
import re
from datetime import datetime

class SincronizadorDefinitivo:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.contenido = ""
        
    def ejecutar(self):
        print("SINCRONIZADOR DEFINITIVO")
        print("=" * 40)
        
        # Backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_sync_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup: {backup_name}")
        
        # Cargar
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
        
        while True:
            self.mostrar_menu()
            opcion = input("\nOpcion: ").strip()
            
            if opcion == '1':
                self.sincronizar_catalogo()
            elif opcion == '2':
                self.sincronizar_certificados()
            elif opcion == '3':
                self.sincronizar_eventos()
            elif opcion == '4':
                self.sincronizar_fotos_atelier()
            elif opcion == '5':
                self.sincronizar_todo()
            elif opcion == '6':
                self.limpiar_javascript()
            elif opcion == '7':
                self.mostrar_estado()
            elif opcion == '8':
                break
            
            if input("\nGuardar cambios? (s/n): ").lower() == 's':
                self.guardar()
    
    def mostrar_menu(self):
        print("\n" + "=" * 40)
        print("1. Sincronizar CATALOGO")
        print("2. Sincronizar CERTIFICADOS")
        print("3. Sincronizar EVENTOS") 
        print("4. Sincronizar FOTOS ATELIER")
        print("5. Sincronizar TODO")
        print("6. Limpiar JavaScript duplicado")
        print("7. Mostrar estado actual")
        print("8. Salir")
    
    def mostrar_estado(self):
        print("\nESTADO ACTUAL:")
        print("-" * 20)
        
        # Contar obras
        obras_match = re.search(r'const catalogWorks = \[(.*?)\];', self.contenido, re.DOTALL)
        if obras_match:
            obras_count = obras_match.group(1).count('path:')
            print(f"Obras en HTML: {obras_count}")
        
        # Contar certificados
        cert_match = re.search(r'const certificateData = \[(.*?)\];', self.contenido, re.DOTALL)
        if cert_match:
            cert_count = cert_match.group(1).count('"CERTIFICADOS/')
            print(f"Certificados en HTML: {cert_count}")
        
        # Contar eventos
        event_match = re.search(r'const eventData = \[(.*?)\];', self.contenido, re.DOTALL)
        if event_match:
            event_count = event_match.group(1).count('"title":')
            print(f"Eventos en HTML: {event_count}")
        
        # Contar archivos reales
        if os.path.exists('CATALOGO'):
            archivos_cat = len([f for f in os.listdir('CATALOGO') if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov'))])
            print(f"Archivos en CATALOGO: {archivos_cat}")
        
        if os.path.exists('CERTIFICADOS'):
            archivos_cert = len([f for f in os.listdir('CERTIFICADOS') if f.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf'))])
            print(f"Archivos en CERTIFICADOS: {archivos_cert}")
        
        if os.path.exists('fotos atelier'):
            archivos_atelier = len([f for f in os.listdir('fotos atelier') if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
            print(f"Archivos en fotos atelier: {archivos_atelier}")
        
        # Contar fotos hardcodeadas en HTML
        fotos_en_html = self.contenido.count('fotos atelier/')
        print(f"Fotos atelier en HTML: {fotos_en_html}")
        
        if os.path.exists('Datos Personales, declaración de artista y biografía'):
            archivos_datos = len([f for f in os.listdir('Datos Personales, declaración de artista y biografía') if f.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf', '.txt', '.docx'))])
            print(f"Archivos en Datos Personales: {archivos_datos}")
    
    def sincronizar_catalogo(self):
        print("\nSINCRONIZANDO CATALOGO...")
        
        if not os.path.exists('CATALOGO'):
            print("Carpeta CATALOGO no existe")
            return
        
        archivos = [f for f in os.listdir('CATALOGO') 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov'))]
        
        print(f"Archivos encontrados: {len(archivos)}")
        
        # Obtener obras actuales
        obras_actuales = self.extraer_obras_actuales()
        paths_actuales = [obra['path'] for obra in obras_actuales]
        
        # Detectar nuevos archivos
        nuevas_obras = []
        for archivo in archivos:
            path_completo = f"CATALOGO/{archivo}"
            if path_completo not in paths_actuales:
                print(f"  + Nuevo: {archivo}")
                nueva_obra = self.crear_obra_desde_archivo(archivo)
                nuevas_obras.append(nueva_obra)
        
        # Detectar archivos borrados
        obras_validas = []
        for obra in obras_actuales:
            archivo = os.path.basename(obra['path'])
            if archivo in archivos:
                obras_validas.append(obra)
            else:
                print(f"  - Eliminado: {archivo}")
        
        # Combinar y ordenar por año descendente
        todas_obras = obras_validas + nuevas_obras
        todas_obras_ordenadas = sorted(todas_obras, 
                                     key=lambda x: int(x['year']) if x['year'].isdigit() else 0, 
                                     reverse=True)
        
        # Actualizar HTML
        self.reemplazar_array_catalogo(todas_obras_ordenadas)
        print(f"Catalogo actualizado: {len(todas_obras_ordenadas)} obras")
    
    def extraer_obras_actuales(self):
        """Extrae obras del HTML actual"""
        obras = []
        
        match = re.search(r'const catalogWorks = \[(.*?)\];', self.contenido, re.DOTALL)
        if not match:
            return obras
        
        contenido_array = match.group(1)
        
        # Buscar cada objeto obra
        patron_obra = r'\{([^}]*)\}'
        objetos = re.findall(patron_obra, contenido_array)
        
        for obj_str in objetos:
            obra = {}
            
            # Extraer propiedades
            propiedades = ['path', 'type', 'title', 'technique', 'dimensions', 'year', 'collection']
            for prop in propiedades:
                patron = f'{prop}:\\s*"([^"]*)"'
                match_prop = re.search(patron, obj_str)
                obra[prop] = match_prop.group(1) if match_prop else ""
            
            if obra.get('path'):
                obras.append(obra)
        
        return obras
    
    def crear_obra_desde_archivo(self, archivo):
        """Crea objeto obra desde nombre de archivo"""
        nombre_base = os.path.splitext(archivo)[0]
        
        # Parsear nombre de archivo
        # Formato esperado: "TITULO - tecnica - dimensiones - año"
        partes = [p.strip() for p in nombre_base.split(' - ')]
        
        titulo = partes[0] if len(partes) > 0 else nombre_base
        tecnica = partes[1] if len(partes) > 1 else ""
        dimensiones = partes[2] if len(partes) > 2 else ""
        
        # Buscar año en cualquier parte
        año = ""
        for parte in partes:
            match_año = re.search(r'año\s*(\d{4})', parte)
            if match_año:
                año = match_año.group(1)
                break
            elif re.match(r'^\d{4}$', parte.strip()):
                año = parte.strip()
                break
        
        # Si no hay año, usar 2025
        if not año:
            año = "2025"
        
        # Detectar colección privada
        coleccion = ""
        if any("colección privada" in p.lower() or "coleccion privada" in p.lower() for p in partes):
            coleccion = "Colección privada"
        
        return {
            'path': f"CATALOGO/{archivo}",
            'type': 'video' if archivo.lower().endswith(('.mp4', '.mov')) else 'image',
            'title': titulo,
            'technique': tecnica,
            'dimensions': dimensiones,
            'year': año,
            'collection': coleccion
        }
    
    def reemplazar_array_catalogo(self, obras):
        """Reemplaza el array catalogWorks"""
        nuevo_array = "const catalogWorks = [\n"
        
        for i, obra in enumerate(obras):
            nuevo_array += "            {\n"
            nuevo_array += f'                path: "{self.escapar(obra["path"])}",\n'
            nuevo_array += f'                type: "{self.escapar(obra["type"])}",\n'
            nuevo_array += f'                title: "{self.escapar(obra["title"])}",\n'
            nuevo_array += f'                technique: "{self.escapar(obra["technique"])}",\n'
            nuevo_array += f'                dimensions: "{self.escapar(obra["dimensions"])}",\n'
            nuevo_array += f'                year: "{self.escapar(obra["year"])}",\n'
            nuevo_array += f'                collection: "{self.escapar(obra["collection"])}"\n'
            nuevo_array += "            }"
            
            if i < len(obras) - 1:
                nuevo_array += ","
            nuevo_array += "\n"
        
        nuevo_array += "        ];;"  # Mantener ;; como en original
        
        # Reemplazar en el HTML
        patron = r'const catalogWorks = \[.*?\];;'
        self.contenido = re.sub(patron, nuevo_array, self.contenido, flags=re.DOTALL)
    
    def sincronizar_certificados(self):
        print("\nSINCRONIZANDO CERTIFICADOS...")
        
        if not os.path.exists('CERTIFICADOS'):
            print("Carpeta CERTIFICADOS no existe")
            return
        
        archivos = [f for f in os.listdir('CERTIFICADOS') 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf'))]
        
        print(f"Archivos encontrados: {len(archivos)}")
        
        # Crear lista ordenada manteniendo prioridades
        certificados_ordenados = []
        
        # Buscar específicamente los certificados prioritarios
        diplomatura = None
        premio = None
        otros = []
        
        for archivo in archivos:
            nombre_lower = archivo.lower()
            if 'diplomatura' in nombre_lower and 'arteterapia' in nombre_lower:
                diplomatura = f"CERTIFICADOS/{archivo}"
                print(f"  1. {archivo} (PRIORITARIO)")
            elif 'primer premio' in nombre_lower and 'rostros universales' in nombre_lower:
                premio = f"CERTIFICADOS/{archivo}"
                print(f"  2. {archivo} (PRIORITARIO)")
            else:
                otros.append(f"CERTIFICADOS/{archivo}")
        
        # Construir lista final con prioridades
        if diplomatura:
            certificados_ordenados.append(diplomatura)
        if premio:
            certificados_ordenados.append(premio)
        certificados_ordenados.extend(sorted(otros))
        
        # Mostrar certificados que se eliminarán (están en HTML pero no en carpeta)
        cert_actuales = self.extraer_certificados_actuales()
        for cert in cert_actuales:
            archivo_nombre = cert.split('/')[-1]
            if archivo_nombre not in archivos:
                print(f"  - Eliminando: {archivo_nombre}")
        
        self.reemplazar_array_certificados(certificados_ordenados)
        print(f"Certificados actualizados: {len(certificados_ordenados)}")
    
    def extraer_certificados_actuales(self):
        """Extrae certificados del HTML actual"""
        match = re.search(r'const certificateData = \[(.*?)\];', self.contenido, re.DOTALL)
        if not match:
            return []
        
        contenido_array = match.group(1)
        return re.findall(r'"([^"]*)"', contenido_array)
    
    def reemplazar_array_certificados(self, certificados):
        """Reemplaza el array certificateData"""
        nuevo_array = "const certificateData = [\n"
        
        for i, cert in enumerate(certificados):
            nuevo_array += f'            "{self.escapar(cert)}"'
            if i < len(certificados) - 1:
                nuevo_array += ","
            nuevo_array += "\n"
        
        nuevo_array += "        ];"
        
        # Reemplazar
        patron = r'const certificateData = \[.*?\];'
        self.contenido = re.sub(patron, nuevo_array, self.contenido, flags=re.DOTALL)

    def sincronizar_eventos(self):
        print("\nSINCRONIZANDO EVENTOS...")
        
        if not os.path.exists('EVENTOS'):
            print("Carpeta EVENTOS no existe")
            return
        
        archivos = [f for f in os.listdir('EVENTOS') 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        print(f"Archivos encontrados: {len(archivos)}")
        
        nuevos_eventos = []
        for archivo in archivos:
            evento = self.crear_evento_desde_archivo(archivo)
            nuevos_eventos.append(evento)
            print(f"  + {evento['title']} - {evento['date']}")
        
        self.reemplazar_array_eventos(nuevos_eventos)
        print(f"Eventos actualizados: {len(nuevos_eventos)}")
    
    def crear_evento_desde_archivo(self, archivo):
        """Crea evento desde nombre de archivo"""
        nombre = os.path.splitext(archivo)[0]
        
        # Parsear nombre
        titulo = ""
        fecha = "Próximamente"
        lugar = ""
        descripcion = ""
        
        # Buscar patron de fecha
        if "setiembre" in nombre.lower() or "septiembre" in nombre.lower():
            if "2025" in nombre:
                fecha = "Setiembre 2025"
            else:
                fecha = "Setiembre"
        
        # Buscar URLs
        urls = re.findall(r'(www\.[^\s]+|https?://[^\s]+)', nombre)
        if urls:
            url = urls[0]
            if not url.startswith('http'):
                url = 'https://' + url
            descripcion = f'<a href="{url}" target="_blank">Más información</a>'
        
        # Extraer título (primera parte antes de guión o todo)
        if ' - ' in nombre:
            titulo = nombre.split(' - ')[0]
            resto = nombre.split(' - ', 1)[1]
            
            # Buscar lugar en el resto
            partes_resto = resto.split(' - ')
            if len(partes_resto) > 1:
                lugar = partes_resto[-1]  # Última parte como lugar
        else:
            titulo = nombre
        
        # Limpiar título
        if len(titulo) > 50:
            titulo = titulo[:50]
        
        return {
            'date': fecha,
            'title': titulo,
            'place': lugar,
            'description': descripcion
        }
    
    def reemplazar_array_eventos(self, eventos):
        """Reemplaza el array eventData"""
        nuevo_array = "const eventData = [\n"
        
        for i, evento in enumerate(eventos):
            nuevo_array += "        {\n"
            nuevo_array += f'            "date": "{self.escapar(evento["date"])}",\n'
            nuevo_array += f'            "title": "{self.escapar(evento["title"])}",\n'
            nuevo_array += f'            "place": "{self.escapar(evento["place"])}",\n'
            nuevo_array += f'            "description": "{self.escapar(evento["description"])}"\n'
            nuevo_array += "        }"
            
            if i < len(eventos) - 1:
                nuevo_array += ","
            nuevo_array += "\n"
        
        nuevo_array += "    ];"
        
        # Reemplazar
        patron = r'const eventData = \[.*?\];'
        self.contenido = re.sub(patron, nuevo_array, self.contenido, flags=re.DOTALL)
    
    def sincronizar_fotos_atelier(self):
        print("\nSINCRONIZANDO FOTOS ATELIER...")
        
        if not os.path.exists('fotos atelier'):
            print("Carpeta 'fotos atelier' no existe")
            return
        
        archivos = [f for f in os.listdir('fotos atelier') 
                   if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        print(f"Archivos encontrados: {len(archivos)}")
        
        # Buscar donde están las fotos hardcodeadas en el HTML
        # Están en las páginas createPage después de "Nueva página:"
        
        # Encontrar el bloque de fotos atelier
        patron_inicio = r'(// New page: Atelier Image 1.*?createPage\(`)'
        patron_fin = r'(createPage\(`.*?fotos atelier/atelier3\.jpg.*?`\), \+\+pageCounter\);)'
        
        match_inicio = re.search(patron_inicio, self.contenido, re.DOTALL)
        match_fin = re.search(patron_fin, self.contenido, re.DOTALL)
        
        if match_inicio and match_fin:
            inicio = match_inicio.start()
            fin = match_fin.end()
            
            # Generar nuevo código para las fotos
            nuevo_codigo = ""
            for i, archivo in enumerate(archivos, 1):
                nombre_display = archivo.replace('.jpg', '').replace('.jpeg', '').replace('.png', '')
                
                nuevo_codigo += f'''
            // New page: {nombre_display}
            createPage(`
                <div class="artwork-page">
                    <img data-src="fotos atelier/{archivo}" alt="{nombre_display}" class="artwork-image-zoomable">
                </div>
            `, ++pageCounter);
'''
            
            # Reemplazar el bloque
            self.contenido = (self.contenido[:inicio] + 
                            nuevo_codigo.strip() + 
                            self.contenido[fin:])
            
            print(f"Fotos atelier actualizadas: {len(archivos)} imágenes")
        else:
            print("No se encontró el bloque de fotos atelier en el HTML")
    
    def sincronizar_todo(self):
        print("\nSINCRONIZACION TOTAL...")
        self.sincronizar_catalogo()
        self.sincronizar_certificados()
        self.sincronizar_eventos()
        self.sincronizar_fotos_atelier()
        print("Sincronizacion completa")
    
    def limpiar_javascript(self):
        print("\nLIMPIANDO JAVASCRIPT DUPLICADO...")
        
        # Contar funciones duplicadas
        funciones_duplicadas = [
            'goToObras',
            'goToCertificados', 
            'goToEventos',
            'goToAtelier'
        ]
        
        for funcion in funciones_duplicadas:
            patron = f'function {funcion}\\(\\).*?\\}}'
            matches = re.findall(patron, self.contenido, re.DOTALL)
            print(f"  {funcion}: {len(matches)} ocurrencias")
            
            # Mantener solo la primera ocurrencia
            if len(matches) > 1:
                # Reemplazar todas las ocurrencias excepto la primera
                contador = 0
                def reemplazo(match):
                    nonlocal contador
                    contador += 1
                    return match.group(0) if contador == 1 else ""
                
                self.contenido = re.sub(patron, reemplazo, self.contenido, flags=re.DOTALL)
        
        # Limpiar líneas vacías excesivas
        self.contenido = re.sub(r'\n\s*\n\s*\n', '\n\n', self.contenido)
        
        print("JavaScript limpio")
    
    def escapar(self, texto):
        """Escapa caracteres para JavaScript"""
        if not isinstance(texto, str):
            return str(texto)
        return texto.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
    
    def guardar(self):
        """Guarda el archivo"""
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        print("Archivo guardado")

if __name__ == "__main__":
    sync = SincronizadorDefinitivo()
    sync.ejecutar()