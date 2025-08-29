import os
import json
from datetime import datetime

def sync_all_folders():
    print("SINCRONIZANDO TODAS LAS CARPETAS")
    print("=" * 32)
    
    # Leer archivo HTML actual
    with open("index.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # 1. Sincronizar CATALOGO
    print("\n1. SINCRONIZANDO CATALOGO...")
    catalog_files = []
    if os.path.exists("CATALOGO"):
        for archivo in sorted(os.listdir("CATALOGO")):
            if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                catalog_files.append(f"CATALOGO/{archivo}")
                print(f"   ✓ {archivo}")
    
    # 2. Sincronizar CERTIFICADOS  
    print("\n2. SINCRONIZANDO CERTIFICADOS...")
    cert_files = []
    if os.path.exists("CERTIFICADOS"):
        for archivo in sorted(os.listdir("CERTIFICADOS")):
            if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                cert_files.append(f"CERTIFICADOS/{archivo}")
                print(f"   ✓ {archivo}")
    
    # 3. Sincronizar fotos atelier
    print("\n3. SINCRONIZANDO fotos atelier...")
    atelier_files = []
    if os.path.exists("fotos atelier"):
        for archivo in sorted(os.listdir("fotos atelier")):
            if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                atelier_files.append(f"fotos atelier/{archivo}")
                print(f"   ✓ {archivo}")
    
    # 4. Sincronizar EVENTOS
    print("\n4. SINCRONIZANDO EVENTOS...")
    eventos_activos = []
    if os.path.exists("EVENTOS/data"):
        for archivo in os.listdir("EVENTOS/data"):
            if archivo.endswith('.json'):
                try:
                    with open(f"EVENTOS/data/{archivo}", 'r', encoding='utf-8') as f:
                        evento = json.load(f)
                        if evento.get('estado') == 'activo':
                            eventos_activos.append(evento)
                            print(f"   ✓ {evento.get('titulo', archivo)}")
                except:
                    print(f"   ✗ Error leyendo {archivo}")
    
    # Actualizar certificateData en JavaScript
    import re
    cert_array = '[\n        "' + '",\n        "'.join(cert_files) + '"\n    ]'
    contenido = re.sub(
        r'const certificateData = \[[^\]]*\];',
        f'const certificateData = {cert_array};',
        contenido
    )
    
    # Generar eventos HTML
    eventos_html = '<div class="events-container">\\n                    <h3>Próximos Eventos</h3>\\n\\n'
    
    for evento in eventos_activos:
        titulo = evento.get('titulo', 'Evento')
        imagen = evento.get('imagen', '')
        tipo = evento.get('tipo', 'evento').title()
        
        eventos_html += f'''                    <div class="event-item">
                        <div class="event-flyer" onclick="openLightbox('{imagen}', '{titulo}', 'Flyer del evento')">
                            <img src="{imagen}" alt="{titulo}" loading="lazy">
                        </div>
                        <div class="event-info">
                            <div class="event-type">{tipo}</div>
                            <div class="event-title">{titulo}</div>
                            <div class="event-details">
                                <p>Haz click en el flyer para ver todos los detalles.</p>
                            </div>
                        </div>
                    </div>\\n\\n'''
    
    if not eventos_activos:
        eventos_html += '''                    <div class="event-item">
                        <div class="event-info">
                            <div class="event-title">Próximamente nuevos eventos</div>
                        </div>
                    </div>\\n\\n'''
    
    eventos_html += '                </div>'
    
    # Reemplazar eventos
    contenido = re.sub(
        r'<div class="events-container">.*?</div>',
        eventos_html,
        contenido,
        flags=re.DOTALL
    )
    
    # Actualizar galería atelier si cambió
    if atelier_files:
        atelier_html = ''
        for i, foto in enumerate(atelier_files):
            nombre = foto.split('/')[-1].split('.')[0].replace('_', ' ').title()
            atelier_html += f'''                        <div class="atelier-photo-small" onclick="openLightbox('{foto}', '{nombre}')">
                            <img src="{foto}" alt="{nombre}" loading="lazy">
                        </div>\\n'''
        
        # Reemplazar galería atelier
        contenido = re.sub(
            r'<div class="atelier-gallery-small">.*?</div>',
            f'<div class="atelier-gallery-small">\\n{atelier_html}                    </div>',
            contenido,
            flags=re.DOTALL
        )
    
    # Guardar archivo actualizado
    with open("index_synced.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print(f"\n✓ {len(catalog_files)} archivos en CATALOGO")
    print(f"✓ {len(cert_files)} certificados sincronizados")  
    print(f"✓ {len(atelier_files)} fotos atelier actualizadas")
    print(f"✓ {len(eventos_activos)} eventos activos")
    
    print(f"\nArchivo: index_synced.html")
    print("Para aplicar: copy index_synced.html index.html")
    print("Después: git add . && git commit -m 'Sync folders' && git push")

if __name__ == "__main__":
    sync_all_folders()