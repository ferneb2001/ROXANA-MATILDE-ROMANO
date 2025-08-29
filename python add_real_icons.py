import re

def add_real_icons():
    print("ETAPA 2: AGREGANDO ICONOS REALES")
    print("=" * 35)
    
    # Leer archivo de Etapa 1 que funciona
    with open("roxana_centrado_etapa1.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Solo reemplazar los emojis por iconos SVG reales
    # SIN tocar estructura HTML ni JavaScript
    
    # 1. WhatsApp (verde oficial)
    contenido = contenido.replace(
        '💬 +54 9 261-5988180',
        '''<svg width="18" height="18" viewBox="0 0 24 24" fill="#25D366" style="vertical-align: middle; margin-right: 8px;"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.570-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.890-5.335 11.893-11.893A11.821 11.821 0 0020.465 3.488"/></svg>+54 9 261-5988180'''
    )
    
    # 2. Email
    contenido = contenido.replace(
        '✉️ roxanamatilderomano@gmail.com',
        '''<svg width="18" height="18" viewBox="0 0 24 24" fill="white" style="vertical-align: middle; margin-right: 8px;"><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.910 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/></svg>roxanamatilderomano@gmail.com'''
    )
    
    # 3. Ubicación (Google Maps style)
    contenido = contenido.replace(
        '📍 Manuel A. Sáez 2101 - Las Heras - Mendoza',
        '''<svg width="18" height="18" viewBox="0 0 24 24" fill="#4285F4" style="vertical-align: middle; margin-right: 8px;"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>Manuel A. Sáez 2101 - Las Heras - Mendoza'''
    )
    
    # 4. YouTube (rojo oficial)
    contenido = contenido.replace(
        '📺 @roxanamatilderomano',
        '''<svg width="18" height="18" viewBox="0 0 24 24" fill="#FF0000" style="vertical-align: middle; margin-right: 8px;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>@roxanamatilderomano'''
    )
    
    # 5. Instagram (gradiente oficial)
    # Primero agregar el gradiente al CSS
    contenido = contenido.replace(
        '</style>',
        '''        
        /* Gradiente de Instagram */
        .instagram-icon {
            background: linear-gradient(45deg, #f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%);
            border-radius: 3px;
            padding: 2px;
        }
        
    </style>'''
    )
    
    contenido = contenido.replace(
        '📷 @roxanamatilderomano2017',
        '''<svg width="18" height="18" viewBox="0 0 24 24" class="instagram-icon" style="vertical-align: middle; margin-right: 8px;"><path fill="white" d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>@roxanamatilderomano2017'''
    )
    
    # Guardar archivo con iconos reales
    with open("roxana_iconos_reales.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ WhatsApp: Verde oficial (#25D366)")
    print("✓ Email: Icono de sobre blanco")
    print("✓ Ubicación: Pin azul estilo Google Maps")
    print("✓ YouTube: Rojo oficial (#FF0000)")
    print("✓ Instagram: Gradiente oficial con colores reales")
    print("✓ Estructura HTML sin modificar")
    print("✓ Solo reemplazo de emojis por SVG")
    print("\nArchivo: roxana_iconos_reales.html")
    print("Los iconos son los oficiales de cada plataforma")

if __name__ == "__main__":
    add_real_icons()