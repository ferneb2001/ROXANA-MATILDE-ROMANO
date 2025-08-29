def fix_from_working_base():
    print("ARREGLANDO DESDE BASE QUE FUNCIONA")
    print("=" * 35)
    
    # Usar roxana_iconos_reales.html que sabemos que funciona
    with open("roxana_iconos_reales.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    print("✓ Usando roxana_iconos_reales.html como base (funciona)")
    
    # SOLO DOS CAMBIOS MÍNIMOS:
    
    # 1. Cambiar "Artista Visual" por "Artista Plástica"
    contenido = contenido.replace(
        '<p class="subtitle">Artista Visual</p>',
        '<p class="subtitle">Artista Plástica</p>'
    )
    print("✓ Cambiado a 'Artista Plástica'")
    
    # 2. Arreglar SOLO el CSS del indicador para que no se superponga
    # Buscar el CSS actual del indicador y hacerlo más específico
    import re
    
    # Reemplazar CSS del indicador con uno más fuerte
    contenido = re.sub(
        r'\.page-indicator\s*\{[^}]*\}',
        '''.page-indicator {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0,0,0,0.85);
            color: white;
            padding: 8px 15px;
            border-radius: 15px;
            z-index: 10000;
            font-size: 14px;
            font-weight: bold;
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            min-width: 50px;
            text-align: center;
        }''',
        contenido
    )
    print("✓ CSS del indicador mejorado")
    
    # NO TOCAR NADA MÁS - mantener toda la funcionalidad existente
    
    with open("roxana_simple_fix.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("\n✓ CAMBIOS MÍNIMOS APLICADOS")
    print("✓ Navegación intacta")
    print("✓ JavaScript sin modificar")
    print("✓ Solo CSS del indicador mejorado")
    
    print("\nArchivo: roxana_simple_fix.html")
    print("Debería funcionar igual que antes pero con indicador legible")

if __name__ == "__main__":
    fix_from_working_base()