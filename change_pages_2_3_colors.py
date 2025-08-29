def change_pages_2_3_colors():
    print("CAMBIANDO PÁGINAS 2 Y 3 A FONDO BLANCO")
    print("=" * 40)
    
    # Leer archivo actual
    with open("roxana_mobile_optimized.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Modificar CSS de páginas 2 y 3
    import re
    
    # Cambiar fondo de página 2 (Declaración de Artista)
    contenido = re.sub(
        r'\.page2 \{ background: linear-gradient\(135deg, #8e44ad 0%, #9b59b6 100%\); \}',
        '.page2 { background: white; color: black; }',
        contenido
    )
    
    # Cambiar fondo de página 3 (Sobre la Artista)
    contenido = re.sub(
        r'\.page3 \{ background: linear-gradient\(135deg, #8e44ad 0%, #9b59b6 100%\); \}',
        '.page3 { background: white; color: black; }',
        contenido
    )
    
    # Agregar estilos específicos para texto en páginas blancas
    css_paginas_blancas = '''
        /* Estilos para páginas 2 y 3 con fondo blanco */
        .page2 .content h2,
        .page3 .content h2 {
            color: #2c3e50;
            margin-bottom: 30px;
        }
        
        .page2 .artist-statement,
        .page3 .biografia-content {
            color: #333;
            line-height: 1.7;
        }
        
        .page2 .artist-statement blockquote {
            background: rgba(46, 62, 80, 0.1);
            color: #2c3e50;
            border-left: 4px solid #3498db;
        }
        
        .page2 .artist-statement p,
        .page3 .biografia-content p {
            color: #444;
            margin-bottom: 15px;
        }'''
    
    # Insertar CSS adicional
    contenido = contenido.replace('</style>', css_paginas_blancas + '\n    </style>')
    
    with open("roxana_white_pages.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Página 2: Fondo blanco, texto negro")
    print("✓ Página 3: Fondo blanco, texto negro") 
    print("✓ Títulos en azul oscuro (#2c3e50)")
    print("✓ Texto principal en gris oscuro (#444)")
    print("✓ Blockquote con borde azul")
    print("✓ Mejor legibilidad y contraste")
    print("✓ Otras páginas mantienen sus colores")
    
    print("\nArchivo: roxana_white_pages.html")
    print("Páginas 2-3: Fondo blanco, resto mantiene colores originales")

if __name__ == "__main__":
    change_pages_2_3_colors()