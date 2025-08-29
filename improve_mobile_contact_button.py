def improve_mobile_contact_button():
    print("MEJORANDO BOTÓN DE CONTACTO EN MÓVIL")
    print("=" * 35)
    
    # Leer archivo actual
    with open("roxana_page8_completa.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Agregar CSS para botón de contacto más grande en lightbox
    css_mobile_button = '''
        /* Botón de contacto mejorado en lightbox */
        .lightbox-contact-button {
            background: #25D366;
            color: white;
            padding: 12px 20px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 15px;
            transition: all 0.3s ease;
            border: none;
            box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);
        }
        
        .lightbox-contact-button:hover {
            background: #20b358;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(37, 211, 102, 0.4);
        }
        
        .whatsapp-icon {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }
        
        /* Mejorar el botón pequeño en las obras también */
        .contact-artist {
            width: 40px !important;
            height: 40px !important;
            font-size: 20px !important;
        }
        
        @media (max-width: 768px) {
            .lightbox-contact-button {
                padding: 15px 25px;
                font-size: 18px;
                width: 80%;
                justify-content: center;
                margin: 20px auto 0 auto;
            }
            
            .contact-artist {
                width: 45px !important;
                height: 45px !important;
                font-size: 22px !important;
            }
        }'''
    
    # Insertar CSS
    contenido = contenido.replace('</style>', css_mobile_button + '\n    </style>')
    
    # Modificar función openLightbox para incluir botón grande
    import re
    
    # Buscar la función openLightbox y modificarla
    patron_lightbox = r'(function openLightbox\(imgSrc, title, details\) \{.*?lightboxInfo\.innerHTML = `<h3>\$\{title\}</h3><p>\$\{details\}</p>`;)(.*?\})'
    
    nueva_lightbox = r'''\1
            
            // Crear botón de WhatsApp grande
            const whatsappMsg = `Hola Roxana, me interesa tu obra "${title}"`;
            const whatsappUrl = `https://wa.me/5492615988180?text=${encodeURIComponent(whatsappMsg)}`;
            
            const contactButton = `
                <a href="${whatsappUrl}" target="_blank" class="lightbox-contact-button">
                    <svg class="whatsapp-icon" viewBox="0 0 24 24">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.570-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.890-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.488"/>
                    </svg>
                    Consultar esta obra
                </a>
            `;
            
            lightboxInfo.innerHTML = `<h3>${title}</h3><p>${details}</p>${contactButton}`;
        \2'''
    
    contenido = re.sub(patron_lightbox, nueva_lightbox, contenido, flags=re.DOTALL)
    
    with open("roxana_mobile_optimized.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Botón de WhatsApp grande en lightbox")
    print("✓ Icono oficial de WhatsApp incluido")
    print("✓ Botón más grande en móvil (80% de ancho)")
    print("✓ Botones pequeños en obras también mejorados")
    print("✓ Hover effects y animaciones")
    print("✓ Color verde oficial de WhatsApp")
    print("✓ Mensaje personalizado con nombre de obra")
    
    print("\nArchivo: roxana_mobile_optimized.html")
    print("En móvil: botón grande y visible en lightbox")
    print("En obras: botones pequeños también más grandes")

if __name__ == "__main__":
    improve_mobile_contact_button()