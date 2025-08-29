def fix_event_flyer_size():
    print("ARREGLANDO TAMAÑO DE FLYERS EN EVENTOS")
    print("=" * 37)
    
    # Leer el archivo generado por sync_all_folders
    with open("sync_all_folders.py", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Buscar y reemplazar el CSS problemático de eventos
    import re
    
    # Encontrar la sección de CSS y reemplazarla
    css_eventos_corregido = '''        /* Estilos para eventos con flyers - TAMAÑO CORREGIDO */
        .events-container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .event-item {
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 25px;
            display: flex;
            gap: 20px;
            align-items: flex-start;
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .event-flyer {
            flex: 0 0 150px;
            max-width: 150px;
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        
        .event-flyer img {
            width: 100%;
            height: auto;
            max-height: 200px;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        
        .event-flyer:hover img {
            transform: scale(1.05);
        }
        
        .event-info {
            flex: 1;
            min-width: 0;
        }
        
        .event-title {
            color: #d4af37;
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 10px;
            line-height: 1.3;
        }
        
        .event-details {
            line-height: 1.5;
            font-size: 0.95em;
        }
        
        .event-type {
            display: inline-block;
            background: #d4af37;
            color: #1a1a1a;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.75em;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        
        @media (max-width: 768px) {
            .event-item {
                flex-direction: column;
                text-align: center;
                padding: 15px;
            }
            
            .event-flyer {
                flex: none;
                max-width: 200px;
                margin: 0 auto;
            }
            
            .event-flyer img {
                max-height: 250px;
            }
        }'''
    
    # Reemplazar el CSS de eventos en el archivo
    contenido = re.sub(
        r"css_eventos_flyers = '''.*?'''",
        f"css_eventos_flyers = '''{css_eventos_corregido}'''",
        contenido,
        flags=re.DOTALL
    )
    
    # Guardar archivo corregido
    with open("sync_all_folders_fixed.py", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Flyer reducido a 150px de ancho")
    print("✓ Altura máxima 200px desktop, 250px móvil")
    print("✓ object-fit: cover para mantener proporciones")
    print("✓ Texto de evento más compacto")
    print("✓ Mejor responsive para móviles")
    
    print("\nArchivo: sync_all_folders_fixed.py")
    print("Reemplaza el script maestro anterior")
    print("Los flyers ahora son miniaturas clickeables")

if __name__ == "__main__":
    fix_event_flyer_size()