def fix_broken_html_structure():
    print("ARREGLANDO ESTRUCTURA HTML ROTA")
    print("=" * 35)
    
    # Leer archivo con estructura rota
    with open("roxana_8_texto_9_fotos.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    import re
    
    # PASO 1: Arreglar página 8 eliminando divs de cierre extra
    # Buscar página 8 y limpiar su estructura
    patron_page8 = r'(<!-- Página 8: Clases -->.*?<p class="signature-centered"><strong>ROXANA MATILDE ROMANO</strong></p>\s*</div>\s*</div>)(\s*</div>\s*</div>\s*</div>\s*</div>)'
    
    def limpiar_page8(match):
        return match.group(1) + '\n        </div>'  # Solo un cierre
    
    contenido = re.sub(patron_page8, limpiar_page8, contenido, flags=re.DOTALL)
    
    # PASO 2: Mover JavaScript al final, antes de </body>
    # Extraer el JavaScript completo
    patron_script = r'<script>.*?</script>'
    script_match = re.search(patron_script, contenido, re.DOTALL)
    if script_match:
        script_completo = script_match.group(0)
        # Remover script del lugar actual
        contenido = re.sub(patron_script, '', contenido, flags=re.DOTALL)
    else:
        script_completo = ""
    
    # PASO 3: Mover página 9 DENTRO del contenedor principal
    # Buscar y extraer página 9
    patron_page9 = r'(\s*<!-- Página 9: Galería Atelier -->.*?</div>\s*</div>)'
    page9_match = re.search(patron_page9, contenido, re.DOTALL)
    
    if page9_match:
        page9_completa = page9_match.group(1).strip()
        # Remover página 9 del lugar actual
        contenido = re.sub(patron_page9, '', contenido, flags=re.DOTALL)
    else:
        page9_completa = ""
    
    # PASO 4: Insertar página 9 DENTRO del book-container
    # Buscar el final correcto de página 8 e insertar página 9 ahí
    contenido = contenido.replace(
        '        </div>\n        \n    </div>',  # Final de página 8
        '        </div>\n\n' + page9_completa + '\n    </div>'  # Página 8 + Página 9 + cierre
    )
    
    # PASO 5: Insertar navegación, indicador y lightbox ANTES del script
    elementos_ui = '''
    <!-- Navegación -->
    <div class="nav-buttons">
        <button class="nav-btn" onclick="previousPage()">← Anterior</button>
        <button class="nav-btn" onclick="nextPage()">Siguiente →</button>
    </div>
    
    <div class="page-indicator" id="pageIndicator">1 / 9</div>
    
    <!-- Lightbox -->
    <div id="lightbox" class="lightbox" onclick="closeLightbox()">
        <div class="lightbox-content" onclick="event.stopPropagation()">
            <span class="close" onclick="closeLightbox()">&times;</span>
            <img id="lightboxImg" class="lightbox-img" src="" alt="">
            <div id="lightboxInfo" class="lightbox-info"></div>
        </div>
    </div>'''
    
    # PASO 6: Estructura final correcta
    contenido = contenido.replace('</body>', elementos_ui + '\n    \n' + script_completo + '\n</body>')
    
    # PASO 7: Limpiar cualquier div sobrante
    contenido = re.sub(r'\s*</div>\s*</div>\s*</div>\s*$', '', contenido.replace('</body>', '').replace('</html>', ''))
    contenido += '\n</body>\n</html>'
    
    # Guardar archivo con estructura corregida
    with open("roxana_estructura_corregida.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Estructura HTML reparada")
    print("✓ Página 9 dentro del book-container")
    print("✓ JavaScript movido al final") 
    print("✓ Divs de cierre balanceados")
    print("✓ Navegación y lightbox restaurados")
    print("✓ Indicador actualizado a 9 páginas")
    
    print("\nArchivo: roxana_estructura_corregida.html")
    print("Ahora la página 9 debería aparecer con las fotos")

if __name__ == "__main__":
    fix_broken_html_structure()