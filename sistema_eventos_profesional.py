import os
import shutil
import json
import re
from datetime import datetime
from pathlib import Path

class SistemaEventosProfesional:
    def __init__(self):
        self.html_file = "artist_book_actualizado.html"
        self.contenido = ""
        self.eventos_config = "eventos_config.json"
        
        # Estructura de carpetas profesional
        self.estructura_eventos = {
            'EVENTOS': 'Carpeta principal',
            'EVENTOS/flyers': 'Imágenes de eventos (flyers, panfletos)',
            'EVENTOS/data': 'Datos estructurados de eventos',
            'EVENTOS/archive': 'Eventos pasados'
        }
        
    def ejecutar(self):
        print("SISTEMA PROFESIONAL DE EVENTOS")
        print("=" * 40)
        
        # Backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_eventos_prof_{timestamp}.html"
        shutil.copy(self.html_file, backup_name)
        print(f"Backup: {backup_name}")
        
        # Cargar HTML
        with open(self.html_file, 'r', encoding='utf-8') as f:
            self.contenido = f.read()
        
        while True:
            self.mostrar_menu()
            opcion = input("\nOpción: ").strip()
            
            if opcion == '1':
                self.inicializar_estructura()
            elif opcion == '2':
                self.migrar_eventos_existentes()
            elif opcion == '3':
                self.agregar_evento_manual()
            elif opcion == '4':
                self.sincronizar_eventos_profesional()
            elif opcion == '5':
                self.mostrar_estado_eventos()
            elif opcion == '6':
                self.configurar_google_api()
            elif opcion == '7':
                break
                
            if opcion in ['2', '3', '4'] and input("\nGuardar cambios? (s/n): ").lower() == 's':
                self.guardar()
    
    def mostrar_menu(self):
        print("\n" + "=" * 40)
        print("SISTEMA PROFESIONAL DE EVENTOS")
        print("=" * 40)
        print("1. Inicializar estructura profesional")
        print("2. Migrar eventos existentes")
        print("3. Agregar evento manual")
        print("4. Sincronizar eventos (híbrido)")
        print("5. Mostrar estado actual")
        print("6. Preparar Google Calendar API")
        print("7. Salir")
    
    def inicializar_estructura(self):
        """Crea la estructura profesional de carpetas"""
        print("\nInicializando estructura profesional...")
        
        # Crear carpetas
        for carpeta, descripcion in self.estructura_eventos.items():
            if not os.path.exists(carpeta):
                os.makedirs(carpeta, exist_ok=True)
                print(f"✓ Creada: {carpeta} ({descripcion})")
            else:
                print(f"◦ Existe: {carpeta}")
        
        # Crear archivo de configuración
        config_inicial = {
            "version": "1.0",
            "tipos_evento": ["exposicion", "taller", "conferencia", "inauguracion", "reunion"],
            "google_calendar": {
                "enabled": False,
                "calendar_id": "",
                "api_key": ""
            },
            "formato_fecha": "%d/%m/%Y",
            "auto_archive": True,
            "notificaciones": {
                "enabled": False,
                "dias_previos": [7, 1]
            }
        }
        
        if not os.path.exists(self.eventos_config):
            with open(self.eventos_config, 'w', encoding='utf-8') as f:
                json.dump(config_inicial, f, indent=2, ensure_ascii=False)
            print(f"✓ Configuración creada: {self.eventos_config}")
        
        print("\nEstructura profesional lista")
    
    def migrar_eventos_existentes(self):
        """Migra eventos del sistema anterior al nuevo"""
        print("\nMigrando eventos existentes...")
        
        # Verificar que existe la carpeta EVENTOS original
        if not os.path.exists('EVENTOS'):
            print("No hay carpeta EVENTOS para migrar")
            return
        
        # Asegurar estructura nueva
        self.inicializar_estructura()
        
        # Obtener archivos de eventos existentes
        archivos_eventos = [f for f in os.listdir('EVENTOS') 
                           if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        if not archivos_eventos:
            print("No hay eventos para migrar")
            return
        
        eventos_migrados = []
        
        for archivo in archivos_eventos:
            print(f"\nMigrando: {archivo}")
            
            # Analizar archivo
            evento_data = self.analizar_archivo_evento(archivo)
            
            # Mover imagen a flyers
            origen = os.path.join('EVENTOS', archivo)
            destino = os.path.join('EVENTOS/flyers', archivo)
            shutil.copy2(origen, destino)
            print(f"  → Copiado a flyers/")
            
            # Crear archivo de datos
            archivo_data = os.path.splitext(archivo)[0] + '.json'
            ruta_data = os.path.join('EVENTOS/data', archivo_data)
            
            with open(ruta_data, 'w', encoding='utf-8') as f:
                json.dump(evento_data, f, indent=2, ensure_ascii=False)
            print(f"  → Datos guardados: {archivo_data}")
            
            eventos_migrados.append(evento_data)
        
        print(f"\n✓ Migrados {len(eventos_migrados)} eventos")
        return eventos_migrados
    
    def analizar_archivo_evento(self, archivo):
        """Analiza archivo de evento y extrae metadatos"""
        nombre_base = os.path.splitext(archivo)[0]
        
        # Estructura de datos del evento
        evento = {
            "id": self.generar_id_evento(),
            "titulo": "",
            "fecha": "",
            "hora": "",
            "lugar": "",
            "descripcion": "",
            "tipo": "exposicion",
            "imagen": f"EVENTOS/flyers/{archivo}",
            "url": "",
            "estado": "activo",
            "creado": datetime.now().isoformat(),
            "google_event_id": None
        }
        
        # Extraer información del nombre
        partes = [p.strip() for p in nombre_base.split(' - ')]
        
        # Título (primera parte)
        if partes:
            evento["titulo"] = partes[0]
        
        # Buscar fecha
        for parte in partes:
            if self.detectar_fecha(parte):
                evento["fecha"] = self.normalizar_fecha(parte)
                break
        
        # Buscar lugar
        for parte in partes:
            if any(palabra in parte.lower() for palabra in ['galeria', 'sala', 'centro', 'casa', 'museo']):
                evento["lugar"] = parte
                break
        
        # Buscar URL
        for parte in partes:
            if 'www.' in parte or 'http' in parte:
                url = parte
                if not url.startswith('http'):
                    url = 'https://' + url
                evento["url"] = url
                break
        
        # Detectar tipo de evento
        titulo_lower = evento["titulo"].lower()
        if any(palabra in titulo_lower for palabra in ['taller', 'clase', 'curso']):
            evento["tipo"] = "taller"
        elif any(palabra in titulo_lower for palabra in ['muestra', 'exposicion', 'exhibicion']):
            evento["tipo"] = "exposicion"
        elif any(palabra in titulo_lower for palabra in ['conferencia', 'charla']):
            evento["tipo"] = "conferencia"
        
        return evento
    
    def detectar_fecha(self, texto):
        """Detecta si un texto contiene información de fecha"""
        meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                'julio', 'agosto', 'septiembre', 'setiembre', 'octubre', 
                'noviembre', 'diciembre']
        
        texto_lower = texto.lower()
        return any(mes in texto_lower for mes in meses) or re.search(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', texto)
    
    def normalizar_fecha(self, fecha_texto):
        """Normaliza fecha a formato estándar"""
        # Mapeo de meses
        meses = {
            'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
            'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
            'septiembre': '09', 'setiembre': '09', 'octubre': '10',
            'noviembre': '11', 'diciembre': '12'
        }
        
        fecha_lower = fecha_texto.lower()
        
        # Buscar patrón "mes año"
        for mes_nombre, mes_num in meses.items():
            if mes_nombre in fecha_lower:
                # Buscar año
                match_año = re.search(r'(\d{4})', fecha_texto)
                if match_año:
                    año = match_año.group(1)
                    return f"01/{mes_num}/{año}"
                else:
                    return f"01/{mes_num}/2025"
        
        return fecha_texto
    
    def generar_id_evento(self):
        """Genera ID único para evento"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"evento_{timestamp}"
    
    def agregar_evento_manual(self):
        """Permite agregar evento manualmente"""
        print("\nAGREGAR EVENTO MANUAL")
        print("-" * 20)
        
        # Asegurar estructura
        self.inicializar_estructura()
        
        evento = {
            "id": self.generar_id_evento(),
            "creado": datetime.now().isoformat(),
            "estado": "activo",
            "google_event_id": None
        }
        
        # Solicitar datos
        evento["titulo"] = input("Título del evento: ").strip()
        evento["fecha"] = input("Fecha (DD/MM/YYYY) o texto libre: ").strip()
        evento["hora"] = input("Hora (opcional): ").strip()
        evento["lugar"] = input("Lugar: ").strip()
        evento["descripcion"] = input("Descripción: ").strip()
        
        print("\nTipos disponibles: exposicion, taller, conferencia, inauguracion, reunion")
        evento["tipo"] = input("Tipo [exposicion]: ").strip() or "exposicion"
        
        evento["url"] = input("URL (opcional): ").strip()
        
        # Preguntar por imagen
        usar_imagen = input("\n¿Tiene imagen/flyer? (s/n): ").lower() == 's'
        if usar_imagen:
            print("Coloca la imagen en EVENTOS/flyers/ y escribe el nombre:")
            imagen_archivo = input("Nombre del archivo: ").strip()
            if imagen_archivo:
                evento["imagen"] = f"EVENTOS/flyers/{imagen_archivo}"
        else:
            evento["imagen"] = ""
        
        # Guardar datos
        archivo_data = f"{evento['id']}.json"
        ruta_data = os.path.join('EVENTOS/data', archivo_data)
        
        with open(ruta_data, 'w', encoding='utf-8') as f:
            json.dump(evento, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Evento creado: {archivo_data}")
        return evento
    
    def sincronizar_eventos_profesional(self):
        """Sincronización híbrida de eventos"""
        print("\nSINCRONIZACIÓN HÍBRIDA DE EVENTOS")
        print("-" * 30)
        
        eventos_finales = []
        
        # 1. Cargar eventos de archivos JSON (datos estructurados)
        if os.path.exists('EVENTOS/data'):
            archivos_data = [f for f in os.listdir('EVENTOS/data') if f.endswith('.json')]
            
            for archivo_data in archivos_data:
                ruta_data = os.path.join('EVENTOS/data', archivo_data)
                try:
                    with open(ruta_data, 'r', encoding='utf-8') as f:
                        evento = json.load(f)
                    
                    # Verificar que la imagen existe si está especificada
                    if evento.get('imagen') and os.path.exists(evento['imagen']):
                        eventos_finales.append(evento)
                        print(f"✓ Cargado: {evento['titulo']}")
                    elif not evento.get('imagen'):
                        eventos_finales.append(evento)
                        print(f"✓ Cargado (sin imagen): {evento['titulo']}")
                    else:
                        print(f"⚠ Imagen faltante: {evento['titulo']}")
                        
                except Exception as e:
                    print(f"✗ Error cargando {archivo_data}: {e}")
        
        # 2. Procesar flyers sin datos estructurados
        if os.path.exists('EVENTOS/flyers'):
            archivos_flyers = [f for f in os.listdir('EVENTOS/flyers') 
                              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            
            # Buscar flyers sin archivo de datos correspondiente
            for flyer in archivos_flyers:
                archivo_data = os.path.splitext(flyer)[0] + '.json'
                ruta_data = os.path.join('EVENTOS/data', archivo_data)
                
                if not os.path.exists(ruta_data):
                    # Crear evento automáticamente
                    evento_auto = self.analizar_archivo_evento(flyer)
                    evento_auto["imagen"] = f"EVENTOS/flyers/{flyer}"
                    
                    # Guardar datos
                    with open(ruta_data, 'w', encoding='utf-8') as f:
                        json.dump(evento_auto, f, indent=2, ensure_ascii=False)
                    
                    eventos_finales.append(evento_auto)
                    print(f"✓ Auto-creado: {evento_auto['titulo']}")
        
        # 3. Actualizar HTML con eventos híbridos
        if eventos_finales:
            self.actualizar_html_eventos_profesional(eventos_finales)
            print(f"\n✓ Sincronizados {len(eventos_finales)} eventos")
        else:
            print("\nNo hay eventos para sincronizar")
    
    def actualizar_html_eventos_profesional(self, eventos):
        """Actualiza HTML con sistema profesional"""
        nuevo_array = "const eventData = [\n"
        
        for i, evento in enumerate(eventos):
            # Convertir evento a formato HTML
            fecha_display = evento.get('fecha', 'Próximamente')
            lugar_display = evento.get('lugar', '')
            if evento.get('hora'):
                lugar_display = f"{evento.get('hora')} - {lugar_display}".strip(' -')
            
            descripcion = evento.get('descripcion', '')
            if evento.get('url'):
                url = evento['url']
                if not url.startswith('http'):
                    url = 'https://' + url
                if descripcion:
                    descripcion += f' <a href="{url}" target="_blank">Más información</a>'
                else:
                    descripcion = f'<a href="{url}" target="_blank">Más información</a>'
            
            nuevo_array += "        {\n"
            nuevo_array += f'            "date": "{self.escapar(fecha_display)}",\n'
            nuevo_array += f'            "title": "{self.escapar(evento.get("titulo", ""))}",\n'
            nuevo_array += f'            "place": "{self.escapar(lugar_display)}",\n'
            nuevo_array += f'            "description": "{self.escapar(descripcion)}"\n'
            nuevo_array += "        }"
            
            if i < len(eventos) - 1:
                nuevo_array += ","
            nuevo_array += "\n"
        
        nuevo_array += "    ];"
        
        # Reemplazar en HTML
        patron = r'const eventData = \[.*?\];'
        self.contenido = re.sub(patron, nuevo_array, self.contenido, flags=re.DOTALL)
    
    def mostrar_estado_eventos(self):
        """Muestra estado detallado del sistema de eventos"""
        print("\nESTADO DEL SISTEMA DE EVENTOS")
        print("-" * 30)
        
        # Verificar estructura
        for carpeta, desc in self.estructura_eventos.items():
            existe = "✓" if os.path.exists(carpeta) else "✗"
            print(f"{existe} {carpeta}")
        
        # Contar archivos
        conteos = {}
        
        if os.path.exists('EVENTOS/data'):
            conteos['datos'] = len([f for f in os.listdir('EVENTOS/data') if f.endswith('.json')])
        
        if os.path.exists('EVENTOS/flyers'):
            conteos['flyers'] = len([f for f in os.listdir('EVENTOS/flyers') 
                                   if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        
        # Eventos en HTML
        match = re.search(r'const eventData = \[(.*?)\];', self.contenido, re.DOTALL)
        if match:
            conteos['html'] = match.group(1).count('"title":')
        
        print(f"\nEstadísticas:")
        for tipo, cantidad in conteos.items():
            print(f"  {tipo.capitalize()}: {cantidad}")
    
    def configurar_google_api(self):
        """Configuración inicial para Google Calendar API"""
        print("\nCONFIGURACIÓN GOOGLE CALENDAR API")
        print("-" * 30)
        print("Para integrar con Google Calendar necesitarás:")
        print("1. Crear proyecto en Google Cloud Console")
        print("2. Habilitar Calendar API")
        print("3. Crear credenciales de API")
        print("4. Obtener Calendar ID")
        print("\nEsto se configurará en la siguiente fase.")
        
        # Crear archivo de preparación
        google_setup = {
            "instrucciones": [
                "1. Ve a https://console.cloud.google.com",
                "2. Crea nuevo proyecto o selecciona existente",
                "3. Habilita Google Calendar API",
                "4. Crea credenciales (API Key o OAuth2)",
                "5. Obtén el Calendar ID de tu calendario",
                "6. Agrega credenciales al archivo eventos_config.json"
            ],
            "configuracion_requerida": {
                "google_calendar": {
                    "enabled": True,
                    "api_key": "TU_API_KEY_AQUI",
                    "calendar_id": "TU_CALENDAR_ID_AQUI",
                    "oauth_credentials": "ruta/a/credentials.json"
                }
            }
        }
        
        with open('google_calendar_setup.json', 'w', encoding='utf-8') as f:
            json.dump(google_setup, f, indent=2, ensure_ascii=False)
        
        print("✓ Archivo de preparación creado: google_calendar_setup.json")
    
    def escapar(self, texto):
        """Escapa caracteres para JavaScript"""
        if not isinstance(texto, str):
            return str(texto)
        return texto.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
    
    def guardar(self):
        """Guarda el archivo HTML"""
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(self.contenido)
        print("✓ HTML actualizado")

if __name__ == "__main__":
    sistema = SistemaEventosProfesional()
    sistema.ejecutar()