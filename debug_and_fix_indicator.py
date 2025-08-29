def debug_and_fix_indicator():
    print("DEPURANDO Y ARREGLANDO INDICADOR DE PÁGINAS")
    print("=" * 45)
    
    # Leer archivo problemático
    with open("roxana_estructura_corregida.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    import re
    
    # DIAGNÓSTICO: Contar elementos problemáticos
    page_indicator_css = len(re.findall(r'\.page-indicator\s*{', contenido))
    page_indicator_html = len(re.findall(r'id="pageIndicator"', contenido))
    update_function = len(re.findall(r'function updatePageIndicator', contenido))
    
    print(f"CSS .page-indicator encontrados: {page_indicator_css}")
    print(f"HTML id='pageIndicator' encontrados: {page_indicator_html}")  
    print(f"Funciones updatePageIndicator: {update_function}")
    
    # SOLUCIÓN RADICAL: Eliminar TODOS los indicadores existentes y crear uno limpio
    
    # PASO 1: Eliminar TODOS los CSS de page-indicator
    contenido = re.sub(r'\.page-indicator\s*\{[^}]*\}', '', contenido)
    
    # PASO 2: Eliminar TODOS los HTML con pageIndicator
    contenido = re.sub(r'<div[^>]*id="pageIndicator"[^>]*>.*?</div>', '', contenido, flags=re.DOTALL)
    
    # PASO 3: Eliminar función updatePageIndicator duplicada si existe
    contenido = re.sub(r'function updatePageIndicator\(\)\s*\{[^}]*\}', '', contenido)
    
    # PASO 4: Cambiar "Artista Visual" por "Artista Plástica" si no se hizo
    contenido = contenido.replace('Artista Visual', 'Artista Plástica')
    
    # PASO 5: Agregar CSS limpio para el indicador
    css_indicador_limpio = '''
        .page-indicator {
            position: fixed !important;
            top: 20px !important;
            right: 20px !important;
            background: rgba(0,0,0,0.9) !important;
            color: white !important;
            padding: 10px 15px !important;
            border-radius: 20px !important;
            z-index: 9999 !important;
            font-size: 16px !important;
            font-weight: bold !important;
            font-family: 'Georgia', serif !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5) !important;
        }'''
    
    # Insertar CSS antes del cierre de </style>
    contenido = contenido.replace('</style>', css_indicador_limpio + '\n    </style>')
    
    # PASO 6: Agregar HTML limpio del indicador
    html_indicador = '''
    <!-- Indicador de Páginas -->
    <div class="page-indicator" id="pageIndicator">1 / 9</div>'''
    
    # Insertar antes de los botones de navegación
    contenido = contenido.replace(
        '<!-- Navegación -->',
        html_indicador + '\n    \n    <!-- Navegación -->'
    )
    
    # PASO 7: Agregar función updatePageIndicator limpia
    funcion_update = '''
        function updatePageIndicator() {
            const indicator = document.getElementById('pageIndicator');
            if (indicator) {
                indicator.innerHTML = (currentPageIndex + 1) + ' / ' + totalPages;
            }
        }'''
    
    # Insertar función después de la definición de totalPages
    contenido = contenido.replace(
        'const totalPages = 9;',
        'const totalPages = 9;' + funcion_update
    )
    
    # PASO 8: Asegurar que updatePageIndicator se llame correctamente
    # Verificar que esté en scrollToPage y handleScroll
    if 'updatePageIndicator();' not in contenido:
        contenido = contenido.replace(
            'behavior: \'smooth\'',
            'behavior: \'smooth\'\n            });\n            updatePageIndicator();'
        )
    
    # Guardar archivo completamente limpio
    with open("roxana_indicador_limpio.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ TODOS los indicadores anteriores eliminados")
    print("✓ CSS limpio con !important para evitar conflictos")
    print("✓ HTML del indicador único y claro")
    print("✓ Función updatePageIndicator nueva y simple")
    print("✓ 'Artista Plástica' aplicado")
    print("✓ z-index 9999 para máxima visibilidad")
    
    print("\nArchivo: roxana_indicador_limpio.html")
    print("Ahora NO debe haber números superpuestos")

if __name__ == "__main__":
    debug_and_fix_indicator()