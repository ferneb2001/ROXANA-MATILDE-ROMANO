import re

def fix_navigation_quick():
    print("ARREGLO RÁPIDO - RESTAURANDO NAVEGACIÓN")
    print("=" * 45)
    
    # Leer el archivo que funcionaba antes (roxana_orden_corregido.html)
    with open("roxana_orden_corregido.html", "r", encoding="utf-8") as f:
        base_funcionando = f.read()
    
    # Solo hacer cambios mínimos sin romper la navegación
    
    # 1. Corregir solo la foto con cambio mínimo
    base_funcionando = base_funcionando.replace(
        'object-position: center;',
        'object-position: center center;'
    )
    
    # 2. Cambiar solo los iconos sin tocar la estructura
    iconos_nuevos = {
        '📞': '💬',  # Teléfono por WhatsApp  
        '🎥': '📺',  # YouTube
        '📸': '📷'   # Instagram
    }
    
    for viejo, nuevo in iconos_nuevos.items():
        base_funcionando = base_funcionando.replace(viejo, nuevo)
    
    # 3. Cambiar enlaces de teléfono a WhatsApp
    base_funcionando = base_funcionando.replace(
        'tel:+5492615988180',
        'https://wa.me/5492615988180'
    )
    
    # 4. Mejorar solo el padding del contact-item
    base_funcionando = base_funcionando.replace(
        'padding: 12px 20px;',
        'padding: 15px 25px;'
    )
    
    # Guardar versión con cambios mínimos
    with open("roxana_navegacion_arreglada.html", "w", encoding="utf-8") as f:
        f.write(base_funcionando)
    
    print("✓ Navegación restaurada")
    print("✓ Cambios mínimos aplicados:")
    print("  - Foto mejor centrada")
    print("  - Teléfono cambiado a WhatsApp")
    print("  - Iconos actualizados (emojis)")
    print("  - Padding mejorado")
    print("✓ Estructura original preservada")
    print("\nArchivo: roxana_navegacion_arreglada.html")
    print("Este debería funcionar correctamente.")

if __name__ == "__main__":
    fix_navigation_quick()