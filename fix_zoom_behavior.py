def fix_zoom_behavior():
    print("ARREGLANDO COMPORTAMIENTO DE ZOOM EN MÓVIL")
    print("=" * 42)
    
    # Usar archivo base que funciona
    with open("roxana_certificates_safe.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Cambiar el viewport para mejor control de zoom
    contenido = contenido.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=3.0, user-scalable=yes">'
    )
    
    # Agregar CSS para controlar el zoom y scroll
    css_zoom_control = '''
        /* Control de zoom y scroll */
        body {
            touch-action: pan-y pinch-zoom;
            -webkit-text-size-adjust: none;
        }
        
        .book-container {
            touch-action: pan-x;
        }
        
        /* Página específica permite zoom */
        .page {
            touch-action: pinch-zoom;
        }
        
        /* Elementos interactivos mantienen su comportamiento */
        .contact-item, .index-button, .obra-item {
            touch-action: manipulation;
        }
        
        /* Para Samsung A54 - elementos más grandes */
        @media (max-width: 768px) and (min-height: 750px) {
            .page1 {
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            
            .page1 .profile-photo {
                width: 220px;
                height: 220px;
                margin-bottom: 25px;
            }
            
            .page1 .content h1 {
                font-size: 2.4em;
                margin-bottom: 8px;
            }
            
            .page1 .subtitle {
                font-size: 1.8em;
                margin-bottom: 30px;
            }
            
            .page1 .contact-item {
                padding: 16px 22px;
                font-size: 16px;
                margin-bottom: 2px;
            }
            
            .page1 .contact-info {
                gap: 8px;
                margin-top: 20px;
            }
        }'''
    
    # Insertar CSS
    contenido = contenido.replace('</style>', css_zoom_control + '\n    </style>')
    
    # Agregar JavaScript para mejor control de gestos
    js_gesture_control = '''
        
        // Control de gestos para evitar conflictos zoom/swipe
        let isZooming = false;
        let zoomTimeout;
        
        document.addEventListener('touchstart', function(e) {
            if (e.touches.length > 1) {
                isZooming = true;
                clearTimeout(zoomTimeout);
            }
        });
        
        document.addEventListener('touchend', function(e) {
            if (isZooming) {
                zoomTimeout = setTimeout(() => {
                    isZooming = false;
                }, 300);
            }
        });
        
        // Prevenir scroll horizontal durante zoom
        const bookContainer = document.getElementById('bookContainer');
        if (bookContainer) {
            bookContainer.addEventListener('touchmove', function(e) {
                if (isZooming && e.touches.length > 1) {
                    e.preventDefault();
                }
            }, { passive: false });
        }'''
    
    # Insertar JavaScript antes del cierre del script existente
    contenido = contenido.replace(
        'document.addEventListener(\'keydown\'',
        js_gesture_control + '\n        \n        document.addEventListener(\'keydown\''
    )
    
    with open("roxana_zoom_fixed.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Viewport configurado para zoom controlado")
    print("✓ Touch-action configurado por elemento")
    print("✓ Detección de gestos multi-touch")
    print("✓ Elementos más grandes para Samsung A54")
    print("✓ Prevención de scroll durante zoom")
    print("✓ Página 1 centrada verticalmente")
    
    print("\nArchivo: roxana_zoom_fixed.html")
    print("Zoom debería funcionar sin irse a página 2")

if __name__ == "__main__":
    fix_zoom_behavior()