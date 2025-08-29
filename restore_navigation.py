def restore_navigation():
    print("RESTAURANDO NAVEGACIÓN POR SWIPE")
    print("=" * 32)
    
    # Leer archivo con indicador limpio pero sin navegación
    with open("roxana_indicador_limpio.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Verificar si las funciones de navegación existen
    has_previous = 'function previousPage()' in contenido
    has_next = 'function nextPage()' in contenido
    has_scroll = 'function scrollToPage' in contenido
    has_handle_scroll = 'function handleScroll' in contenido
    has_goto = 'function goToPage' in contenido
    
    print(f"previousPage(): {'✓' if has_previous else '✗'}")
    print(f"nextPage(): {'✓' if has_next else '✗'}")
    print(f"scrollToPage(): {'✓' if has_scroll else '✗'}")
    print(f"handleScroll(): {'✓' if has_handle_scroll else '✗'}")
    print(f"goToPage(): {'✓' if has_goto else '✗'}")
    
    # Agregar funciones de navegación faltantes
    navigation_functions = '''
        
        function previousPage() {
            if (currentPageIndex > 0) {
                currentPageIndex--;
                scrollToPage(currentPageIndex);
            }
        }
        
        function nextPage() {
            if (currentPageIndex < totalPages - 1) {
                currentPageIndex++;
                scrollToPage(currentPageIndex);
            }
        }
        
        function scrollToPage(pageIndex) {
            const container = document.getElementById('bookContainer');
            if (container) {
                const pageWidth = window.innerWidth;
                container.scrollTo({
                    left: pageIndex * pageWidth,
                    behavior: 'smooth'
                });
                updatePageIndicator();
            }
        }
        
        function goToPage(pageNum) {
            currentPageIndex = pageNum - 1;
            scrollToPage(currentPageIndex);
        }
        
        function handleScroll() {
            const container = document.getElementById('bookContainer');
            if (container) {
                const pageWidth = window.innerWidth;
                const scrollLeft = container.scrollLeft;
                const newPageIndex = Math.round(scrollLeft / pageWidth);
                
                if (newPageIndex !== currentPageIndex) {
                    currentPageIndex = newPageIndex;
                    updatePageIndicator();
                }
            }
        }'''
    
    # Insertar funciones después de updatePageIndicator
    contenido = contenido.replace(
        'updatePageIndicator();',
        'updatePageIndicator();' + navigation_functions,
        1  # Solo reemplazar la primera ocurrencia
    )
    
    # Asegurar que el event listener de scroll esté presente
    scroll_listener = '''
        
        document.addEventListener('DOMContentLoaded', function() {
            const container = document.getElementById('bookContainer');
            if (container) {
                container.addEventListener('scroll', handleScroll);
            }
            loadObras();
            loadCertificados();
            updatePageIndicator();
        });
        
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowLeft') previousPage();
            if (e.key === 'ArrowRight') nextPage();
        });'''
    
    # Agregar event listeners antes del cierre del script
    if 'addEventListener' not in contenido:
        contenido = contenido.replace('</script>', scroll_listener + '\n    </script>')
    
    # Verificar que currentPageIndex esté definido
    if 'let currentPageIndex = 0;' not in contenido:
        contenido = contenido.replace(
            'const totalPages = 9;',
            'let currentPageIndex = 0;\n        const totalPages = 9;'
        )
    
    # Guardar archivo con navegación restaurada
    with open("roxana_navegacion_restaurada.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("\n✓ Funciones de navegación agregadas")
    print("✓ Event listeners para scroll restaurados")
    print("✓ Variable currentPageIndex verificada")
    print("✓ Navegación por teclado habilitada")
    print("✓ Indicador limpio mantenido")
    
    print("\nArchivo: roxana_navegacion_restaurada.html")
    print("Ahora debería funcionar swipe + indicador correcto")

if __name__ == "__main__":
    restore_navigation()