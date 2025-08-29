import re

def conservative_page1_fix():
    print("ARREGLO CONSERVADOR - SOLO AJUSTES MÍNIMOS")
    print("=" * 45)
    
    # Volver a la base que funcionaba
    with open("roxana_navegacion_arreglada.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # SOLO cambios CSS mínimos sin tocar estructura HTML
    
    # 1. Ajustar tamaño de foto a algo razonable (estaba en 200px)
    contenido = contenido.replace(
        'width: 200px;\n            height: 200px;',
        'width: 180px;\n            height: 180px;'
    )
    
    # 2. Mejorar solo el centrado sin cambiar el resto
    contenido = contenido.replace(
        'object-position: center center;',
        'object-position: center top;'
    )
    
    # 3. Ajustar padding de contact-item para que se vea mejor
    contenido = contenido.replace(
        'padding: 15px 25px;',
        'padding: 12px 20px;'
    )
    
    # 4. Reducir gap entre contact items
    contenido = contenido.replace(
        'gap: 15px;',
        'gap: 10px;'
    )
    
    # 5. Ajustar margin-top del contact-info
    contenido = contenido.replace(
        'margin-top: 30px;',
        'margin-top: 20px;'
    )
    
    # Guardar con cambios mínimos
    with open("roxana_ajuste_minimo.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Cambios mínimos aplicados:")
    print("  - Foto reducida a 180px (era 200px)")
    print("  - Mejor posicionamiento de foto")
    print("  - Padding y spacing ajustados")
    print("✓ Estructura HTML intacta")
    print("✓ JavaScript sin tocar")
    print("✓ Navegación preservada")
    print("\nArchivo: roxana_ajuste_minimo.html")
    print("Debería mantener la navegación funcionando")

if __name__ == "__main__":
    conservative_page1_fix()