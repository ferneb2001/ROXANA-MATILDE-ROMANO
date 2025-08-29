def minimal_samsung_fix():
    print("ARREGLO MÍNIMO PARA SAMSUNG SIN ROMPER CERTIFICADOS")
    print("=" * 50)
    
    # Usar el archivo que funcionaba con certificados
    with open("roxana_address_fixed.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Solo agregar CSS muy específico para aumentar tamaño SIN tocar JavaScript
    css_minimal = '''
        /* Solo escalado de página 1 para Samsung A54 */
        @media (max-width: 768px) and (min-height: 750px) {
            .page1 .profile-photo {
                width: 200px;
                height: 200px;
            }
            
            .page1 .content h1 {
                font-size: 2.2em;
            }
            
            .page1 .subtitle {
                font-size: 1.6em;
            }
            
            .page1 .contact-item {
                padding: 14px 20px;
                font-size: 15px;
            }
            
            .page1 .contact-info {
                gap: 10px;
            }
        }'''
    
    # Insertar CSS antes del cierre
    contenido = contenido.replace('</style>', css_minimal + '\n    </style>')
    
    with open("roxana_certificates_safe.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Base: roxana_address_fixed.html (certificados funcionaban)")
    print("✓ Solo CSS para página 1 más grande")
    print("✓ JavaScript de certificados intacto")
    print("✓ Media query más restrictivo (750px+ altura)")
    print("✓ Sin tocar loadCertificados() ni contenedores")
    
    print("\nArchivo: roxana_certificates_safe.html") 
    print("Mantiene certificados + página 1 más grande para Samsung")

if __name__ == "__main__":
    minimal_samsung_fix()