import re

def fix_photo_and_icons():
    print("CORRIGIENDO FOTO Y ICONOS")
    print("=" * 35)
    
    # Leer archivo actual
    with open("roxana_orden_corregido.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # 1. CORREGIR CSS DE LA FOTO - mejor centrado
    nuevo_css_foto = '''
        .profile-photo {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            object-position: center center;
            border: 4px solid white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            margin: 20px auto 30px auto;
            display: block;
        }'''
    
    # Reemplazar CSS de foto
    patron_css_foto = r'\.profile-photo \{[^}]*\}'
    contenido = re.sub(patron_css_foto, nuevo_css_foto.strip().replace('\n        ', '\n            '), contenido)
    
    # 2. MEJORAR ESTRUCTURA DE LA PÁGINA 1
    nueva_pagina_1 = '''        <!-- Página 1: Datos Personales -->
        <div class="page page1">
            <div class="content">
                <img src="FOTO RO.jpg" alt="Roxana Matilde Romano" class="profile-photo">
                <h1>ROXANA MATILDE ROMANO</h1>
                <p class="subtitle">Artista Visual</p>
                
                <div class="contact-info">
                    <div class="contact-item">
                        <a href="https://wa.me/5492615988180">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.570-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.890-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.488"/>
                            </svg>
                            +54 9 261-5988180
                        </a>
                    </div>
                    <div class="contact-item">
                        <a href="mailto:roxanamatilderomano@gmail.com">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.910 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/>
                            </svg>
                            roxanamatilderomano@gmail.com
                        </a>
                    </div>
                    <div class="contact-item">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
                        </svg>
                        Manuel A. Sáez 2101 - Las Heras - Mendoza
                    </div>
                    <div class="contact-item">
                        <a href="https://youtube.com/@roxanamatilderomano" target="_blank">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="#FF0000">
                                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                            </svg>
                            @roxanamatilderomano
                        </a>
                    </div>
                    <div class="contact-item">
                        <a href="https://instagram.com/roxanamatilderomano2017" target="_blank">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="url(#instagram-gradient)">
                                <defs>
                                    <linearGradient id="instagram-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                        <stop offset="0%" style="stop-color:#f09433"/>
                                        <stop offset="25%" style="stop-color:#e6683c"/>
                                        <stop offset="50%" style="stop-color:#dc2743"/>
                                        <stop offset="75%" style="stop-color:#cc2366"/>
                                        <stop offset="100%" style="stop-color:#bc1888"/>
                                    </linearGradient>
                                </defs>
                                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                            </svg>
                            @roxanamatilderomano2017
                        </a>
                    </div>
                </div>
            </div>
        </div>'''
    
    # Reemplazar página 1
    patron_pagina_1 = r'(\s*<!-- Página 1: Datos Personales -->.*?</div>\s*</div>)'
    contenido = re.sub(patron_pagina_1, nueva_pagina_1, contenido, flags=re.DOTALL)
    
    # 3. MEJORAR CSS DE CONTACT-ITEM PARA ICONOS
    nuevo_css_contact = '''
        .contact-item {
            background: rgba(255,255,255,0.1);
            padding: 15px 25px;
            border-radius: 25px;
            text-decoration: none;
            color: white;
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.2);
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            font-size: 16px;
        }
        
        .contact-item:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }
        
        .contact-item a {
            color: inherit;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 12px;
            width: 100%;
            justify-content: center;
        }
        
        .contact-item svg {
            flex-shrink: 0;
        }'''
    
    # Reemplazar CSS de contact-item
    patron_css_contact = r'\.contact-item \{[^}]*\}'
    contenido = re.sub(patron_css_contact, nuevo_css_contact.strip().replace('\n        ', '\n            '), contenido, flags=re.DOTALL)
    
    # También eliminar el CSS duplicado del contact-item a
    contenido = re.sub(r'\.contact-item a \{[^}]*\}', '', contenido, flags=re.DOTALL)
    
    # 4. MEJORAR ESPACIADO GENERAL DE LA PÁGINA
    contenido = contenido.replace('.content h1 {\n            font-size: 2.5em;\n            margin-bottom: 10px;\n        }',
                                '.content h1 {\n            font-size: 2.5em;\n            margin-bottom: 15px;\n            text-align: center;\n        }')
    
    contenido = contenido.replace('.subtitle {\n            font-size: 1.5em;\n            opacity: 0.9;\n            margin-bottom: 20px;\n        }',
                                '.subtitle {\n            font-size: 1.5em;\n            opacity: 0.9;\n            margin-bottom: 40px;\n            text-align: center;\n        }')
    
    # Guardar archivo corregido
    with open("roxana_foto_iconos_corregida.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Foto mejor centrada con object-position: center center")
    print("✓ Icono de teléfono cambiado a WhatsApp")
    print("✓ Iconos reales de YouTube (rojo) e Instagram (gradiente)")
    print("✓ Mejor alineación y espaciado del contenido")
    print("✓ Contact items centrados con iconos SVG")
    print("✓ Espaciado mejorado entre título y contacto")
    print("\nArchivo: roxana_foto_iconos_corregida.html")
    print("\nIconos incluidos:")
    print("- WhatsApp: Verde con icono real")
    print("- Email: Icono de sobre")  
    print("- Ubicación: Pin de mapa")
    print("- YouTube: Rojo oficial")
    print("- Instagram: Gradiente oficial")

if __name__ == "__main__":
    fix_photo_and_icons()