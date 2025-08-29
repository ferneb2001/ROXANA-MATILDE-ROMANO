def scale_for_samsung_a54():
    print("ESCALANDO PARA SAMSUNG A54 Y SIMILARES")
    print("=" * 35)
    
    # Leer archivo actual
    with open("roxana_address_fixed.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # CSS específico para dispositivos altos como Samsung A54
    css_mobile_scale = '''
        /* Escalado para pantallas altas (Samsung A54, etc.) */
        @media (max-width: 768px) and (min-height: 700px) {
            .profile-photo {
                width: 200px !important;
                height: 200px !important;
            }
            
            .content h1 {
                font-size: 2.3em !important;
                margin-bottom: 15px !important;
            }
            
            .subtitle {
                font-size: 1.7em !important;
                margin-bottom: 25px !important;
            }
            
            .contact-info {
                margin-top: 35px !important;
                gap: 12px !important;
            }
            
            .contact-item {
                padding: 14px 20px !important;
                font-size: 16px !important;
            }
            
            .page {
                padding: 25px !important;
            }
            
            .content h2 {
                font-size: 2.3em !important;
            }
            
            .obras-grid {
                gap: 15px !important;
            }
            
            .obra-item {
                padding: 18px !important;
            }
            
            .obra-img {
                height: 180px !important;
            }
        }
        
        /* Para pantallas muy altas (como A54 en vertical) */
        @media (max-width: 768px) and (min-height: 800px) {
            .profile-photo {
                width: 220px !important;
                height: 220px !important;
            }
            
            .content h1 {
                font-size: 2.5em !important;
            }
            
            .subtitle {
                font-size: 1.8em !important;
            }
            
            .contact-item {
                padding: 16px 22px !important;
                font-size: 17px !important;
            }
        }'''
    
    # Insertar CSS antes del cierre de </style>
    contenido = contenido.replace('</style>', css_mobile_scale + '\n    </style>')
    
    with open("roxana_samsung_optimized.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Foto más grande: 220px en pantallas altas")
    print("✓ Títulos más grandes: 2.5em")
    print("✓ Contact items con más padding")
    print("✓ Texto más legible: 17px")
    print("✓ Espaciado aumentado")
    print("✓ Específico para pantallas 700px+ de altura")
    print("✓ Mantiene responsive para otras pantallas")
    
    print("\nArchivo: roxana_samsung_optimized.html")
    print("Optimizado para Samsung A54 y dispositivos similares")

if __name__ == "__main__":
    scale_for_samsung_a54()