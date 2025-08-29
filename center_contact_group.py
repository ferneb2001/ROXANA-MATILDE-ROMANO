import re

def center_contact_group():
    print("ETAPA 1: CENTRANDO GRUPO DE CONTACTOS")
    print("=" * 40)
    
    # Leer archivo base funcional
    with open("roxana_ajuste_minimo.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # SOLO modificar CSS de contact-info y contact-item
    # SIN tocar HTML ni JavaScript
    
    # 1. Ajustar el contenedor de contact-info
    # Buscar y reemplazar el CSS existente de contact-info
    patron_contact_info = r'\.contact-info \{[^}]*\}'
    
    nuevo_css_contact_info = '''
        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-top: 25px;
            max-width: 380px;
            width: 100%;
            margin-left: auto;
            margin-right: auto;
        }'''
    
    contenido = re.sub(patron_contact_info, nuevo_css_contact_info.strip(), contenido)
    
    # 2. Ajustar contact-item para que estén más juntos
    patron_contact_item = r'\.contact-item \{[^}]*\}'
    
    nuevo_css_contact_item = '''
        .contact-item {
            background: rgba(255,255,255,0.1);
            padding: 11px 18px;
            border-radius: 25px;
            text-decoration: none;
            color: white;
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.2);
            text-align: center;
            display: block;
            width: 100%;
        }'''
    
    contenido = re.sub(patron_contact_item, nuevo_css_contact_item.strip(), contenido)
    
    # 3. Mantener el hover effect
    if '.contact-item:hover' not in contenido:
        contenido = contenido.replace(
            nuevo_css_contact_item.strip(),
            nuevo_css_contact_item.strip() + '''
        
        .contact-item:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }'''
        )
    
    # Guardar archivo con cambios mínimos
    with open("roxana_centrado_etapa1.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Gap reducido a 8px (estaban más separados)")
    print("✓ Max-width de contact-info reducido a 380px")
    print("✓ Padding de contact-item ajustado a 11px/18px")
    print("✓ Mejor centrado con margin: auto")
    print("✓ Estructura HTML sin tocar")
    print("✓ JavaScript intacto")
    print("\nArchivo: roxana_centrado_etapa1.html")
    print("\n¿Probamos este y si funciona seguimos con Etapa 2 (iconos reales)?")

if __name__ == "__mainñ__":
    center_contact_group()