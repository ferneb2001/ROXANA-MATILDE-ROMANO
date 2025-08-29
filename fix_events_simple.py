def fix_events_simple():
    print("ARREGLANDO EVENTOS - SCRIPT LIMPIO")
    print("=" * 33)
    
    # Leer archivo HTML actual
    with open("index.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # CSS correcto para eventos - tamaño pequeño
    css_eventos_pequenos = '''
        /* Eventos con flyers pequeños */
        .events-container {
            max-width: 800px;
            margin: 0 auto;
            text-align: left;
        }
        
        .event-item {
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            display: flex;
            gap: 15px;
            align-items: flex-start;
        }
        
        .event-flyer {
            flex: 0 0 120px;
            width: 120px;
            border-radius: 8px;
            overflow: hidden;
            cursor: pointer;
        }
        
        .event-flyer img {
            width: 100%;
            height: auto;
            max-height: 160px;
            object-fit: cover;
        }
        
        .event-info {
            flex: 1;
        }
        
        .event-title {
            color: #d4af37;
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 8px;
        }
        
        .event-type {
            background: #d4af37;
            color: #000;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 0.7em;
            font-weight: bold;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 8px;
        }
        
        @media (max-width: 768px) {
            .event-item {
                flex-direction: column;
                text-align: center;
            }
            
            .event-flyer {
                margin: 0 auto;
                max-width: 150px;
            }
        }'''
    
    # Insertar CSS antes del cierre de </style>
    contenido = contenido.replace('</style>', css_eventos_pequenos + '\n    </style>')
    
    # HTML simple para eventos de prueba
    eventos_html_simple = '''<div class="events-container">
                    <h3>Próximos Eventos</h3>
                    
                    <div class="event-item">
                        <div class="event-flyer" onclick="openLightbox('EVENTOS/flyers/Muestra Itaka 001.jpg', 'Muestra Itaka', 'Flyer completo del evento')">
                            <img src="EVENTOS/flyers/Muestra Itaka 001.jpg" alt="Muestra Itaka" loading="lazy">
                        </div>
                        <div class="event-info">
                            <div class="event-type">Exposición</div>
                            <div class="event-title">Muestra Itaka 001</div>
                            <div class="event-details">
                                <p>Haz click en el flyer para ver todos los detalles del evento.</p>
                                <p>Consultas por WhatsApp.</p>
                            </div>
                        </div>
                    </div>
                </div>'''
    
    # Buscar y reemplazar la sección de eventos actual
    import re
    contenido = re.sub(
        r'<div class="events-container">.*?</div>',
        eventos_html_simple,
        contenido,
        flags=re.DOTALL
    )
    
    # Guardar archivo arreglado
    with open("index_events_fixed.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ CSS de eventos limpio y pequeño")
    print("✓ Flyer de 120px de ancho máximo")
    print("✓ Altura máxima 160px")
    print("✓ Evento de prueba agregado")
    print("✓ Click abre lightbox para ver completo")
    
    print("\nArchivo: index_events_fixed.html")
    print("Para aplicar: copy index_events_fixed.html index.html")

if __name__ == "__main__":
    fix_events_simple()