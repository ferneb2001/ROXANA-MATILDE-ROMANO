def fix_touch_actions():
    print("CORRIGIENDO TOUCH ACTIONS - RESTAURANDO FUNCIONALIDAD")
    print("=" * 52)
    
    # Volver a archivo base que funcionaba
    with open("roxana_certificates_safe.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Cambiar viewport para permitir zoom pero con mejor control
    contenido = contenido.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=yes, viewport-fit=cover">'
    )
    
    # CSS muy conservador - solo elementos más grandes, sin restricciones de touch
    css_simple = '''
        /* Solo escalado para Samsung A54 - SIN restricciones de touch */
        @media (max-width: 768px) and (min-height: 750px) {
            .page1 .profile-photo {
                width: 210px;
                height: 210px;
            }
            
            .page1 .content h1 {
                font-size: 2.3em;
                line-height: 1.2;
            }
            
            .page1 .subtitle {
                font-size: 1.7em;
                margin-bottom: 25px;
            }
            
            .page1 .contact-item {
                padding: 15px 20px;
                font-size: 15px;
                margin-bottom: 4px;
            }
            
            .page1 .contact-info {
                margin-top: 25px;
                gap: 6px;
            }
        }
        
        /* Mejorar el scroll horizontal para que sea más suave */
        .book-container {
            scroll-behavior: smooth;
        }'''
    
    # Solo agregar CSS sin tocar JavaScript ni touch-action
    contenido = contenido.replace('</style>', css_simple + '\n    </style>')
    
    with open("roxana_touch_restored.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Base: archivo que funcionaba con certificados")
    print("✓ Viewport permite zoom hasta 2x")
    print("✓ SIN restricciones touch-action")
    print("✓ SIN JavaScript de control de gestos")
    print("✓ Solo elementos más grandes para Samsung")
    print("✓ Swipe debería funcionar normal")
    print("✓ Zoom debería funcionar normal")
    
    print("\nArchivo: roxana_touch_restored.html")
    print("Funcionalidad básica restaurada + elementos más grandes")

if __name__ == "__main__":
    fix_touch_actions()